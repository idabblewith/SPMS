from datetime import datetime as dt
import importlib.util


class Loader:
    def __init__(
        self,
        file_handler,
        misc,
        psycopg2,
        tqdm,
        pd,
        os,
        load_dotenv,
        parent_directory,
    ):
        self.os = os
        self.load_dotenv = load_dotenv
        self.tqdm = tqdm
        self.pd = pd
        self.psycopg2 = psycopg2
        self.misc = misc

        self.parent_directory = parent_directory

        self.file_handler = file_handler
        self.specify_source = ""
        self.spms_source = ""
        self.spms_functions = [
            {
                "name": "Create Super User",
                "function": self.spms_create_super_user,
            },
            {
                "name": "Create DBCA Entity",
                "function": self.spms_create_dbca_entity,
            },
            {
                "name": "Create DBCA Branches",
                "function": self.spms_create_dbca_branches,
            },
            {
                "name": "Create DBCA Divisions",
                "function": self.spms_create_dbca_divisions,
            },
            {
                "name": "Load DBCA Projects",
                "function": self.spms_create_dbca_projects,
            },
            {
                "name": "Load DBCA Project Teams",
                "function": self.spms_create_dbca_project_teams,
            },
            # {
            #     "name": "Load Users",
            #     "function": self.spms_create_users,
            # },
            # {
            #     "name": "Load Business Areas",
            #     "function": self.spms_create_business_areas,
            # },
            # {
            #     "name": "Loader Function Two",
            #     "function": self.test_loader_function_two,
            # },
        ]
        self.specify_functions = []
        self.functions = []
        self.set_func = self.determine_functions(self.file_handler.project)

    def determine_functions(self, project):
        funcs = []
        if project == "SPMS":
            funcs = self.spms_functions
        elif project == "SPECIFY":
            funcs = self.specify_functions

        self.functions = funcs

    # HELPER FUNCTIONS =============================================================

    def display_columns_available_in_df(self, df):
        for i, column in enumerate(df.columns):
            print(f"{i + 1}. {column}")

    def alter_column_check(self, df):
        these_columns_okay = self.misc.nli(
            "Continue with these columns?\nType 'y' for yes or press enter for no:"
        )

        # If altering columns
        if these_columns_okay not in self.misc.yes_array:
            # Prompt user for columns to remove
            columns_to_remove = (
                input("Enter the column numbers to remove (comma-separated): ")
                .strip()
                .split(",")
            )

            # Convert user input to a list of integers
            columns_to_remove = [int(col.strip()) - 1 for col in columns_to_remove]

            # Remove selected columns from the DataFrame
            df.drop(df.columns[columns_to_remove], axis=1, inplace=True)

            # Check if user wishes to change column names
            # after displaying available columns
            self.display_columns_available_in_df(df)

            these_column_names_okay = self.misc.nli(
                "Continue with these column names?\nType 'y' for yes or press enter for no:"
            )

            # If altering columns
            if these_column_names_okay not in self.misc.yes_array:
                # Prompt user for columns to rename
                columns_to_rename = (
                    input("Enter the column numbers to rename (comma-separated): ")
                    .strip()
                    .split(",")
                )

                for column_num in columns_to_rename:
                    try:
                        column_num = int(column_num.strip()) - 1
                        old_column_name = df.columns[column_num]
                        new_column_name = input(
                            f"Enter new name for column '{old_column_name}': "
                        )

                        # Rename the column
                        df.rename(
                            columns={old_column_name: new_column_name}, inplace=True
                        )
                        print(
                            f"Column '{old_column_name}' renamed to '{new_column_name}'"
                        )
                    except (ValueError, IndexError):
                        print(f"Invalid column number: {column_num}")

        return df

    def establish_spms_db_connection_and_return_cursor_conn(self):
        # Load the .env file
        self.misc.nls("Loading .env")
        self.load_dotenv()

        try:
            # Establish a connection to the PostgreSQL database
            self.misc.nls("Establishing conn")
            connection = self.psycopg2.connect(
                host=self.os.getenv("SPMS_HOST"),
                port=self.os.getenv("SPMS_PORT"),
                database=self.os.getenv("SPMS_DB"),
                user=self.os.getenv("SPMS_USER"),
                password=self.os.getenv("SPMS_PASSWORD"),
            )

            # Create a cursor object to execute SQL queries
            self.misc.nls("Creating cursor")
            cursor = connection.cursor()

            return cursor, connection

        except Exception as e:
            print(f"Error establishing database connection: {e}")
            raise

    # SPMS FUNCTIONS ===============================================================

    def spms_create_super_user(self, auto=True):
        # Establishing connection:
        connection = self.establish_spms_db_connection()

        # Loading environment variables:
        if auto == True:
            print("Loading Environment variables...")
            env_fn = self.os.getenv("SPMS_SUPERUSER_FIRST_NAME")
            env_ln = self.os.getenv("SPMS_SUPERUSER_LAST_NAME")
            env_email = self.os.getenv("SPMS_SUPERUSER_EMAIL")
            env_username = self.os.getenv("SPMS_SUPERUSER_USERNAME")
            env_pass = self.os.getenv("SPMS_SUPERUSER_PASSWORD")

        else:
            print("Seeking details...")
            env_fn = self.misc.nli("Provide a first name:")
            env_ln = self.misc.nli("Provide a last name:")
            env_email = self.misc.nli("Provide an email:")
            env_username = self.misc.nli("Provide a username:")
            env_pass = self.misc.nli("Provide a password:")

        print("Creating Super user...")

        # Get the current date and time
        current_datetime = dt.now()

        try:
            # Start a transaction
            connection.autocommit = False
            cursor = connection.cursor()

            # Construct the SQL query
            sql = """
                BEGIN;
                INSERT INTO users_user (
                    username, email, first_name, last_name, password,
                    is_superuser, is_staff, is_active, date_joined
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);
                COMMIT;
            """

            # Execute the query with the user data
            cursor.execute(
                sql,
                (
                    env_username,
                    env_email,
                    env_fn,
                    env_ln,
                    env_pass,
                    True,
                    True,
                    True,
                    current_datetime,
                ),
            )

            print("Super user created.")

        except Exception as e:
            print(f"Error creating super user: {str(e)}")
            # Rollback the transaction
            connection.rollback()

        finally:
            # Close the cursor and connection
            cursor.close()
            connection.close()

    def spms_create_users(self):
        # Create super user first
        # self.spms_create_super_user(auto=True)

        # Import models required for load operation
        User = self.import_model("users", "User")

        # Load the file into a data frame
        file_path = self.os.path.join(
            self.file_handler.clean_directory, "pythia_program.csv"
        )
        df = self.file_handler.read_csv_and_prepare_df(file_path)

        # id,password,last_login,is_superuser,username,title,
        # first_name,middle_initials,last_name,image,email,phone,phone_alt,
        # fax,program_id,work_center_id,profile_text,expertise,curriculum_vitae,
        # projects,author_code,publications_staff,publications_other,
        # is_staff,is_active,is_external,agreed,date_joined,is_group,group_name,
        # affiliation
        pass

    def spms_create_business_areas(self):
        BusinessArea = self.import_model("entities", "BusinessArea")
        Entity = self.import_model("entities", "Entity")
        User = self.import_model("users", "User")
        BusinessAreaPhoto = self.import_model("medias", "BusinessAreaPhoto")

        # Load the file into a data frame
        file_path = self.os.path.join(
            self.file_handler.clean_directory, "pythia_program.csv"
        )
        df = self.file_handler.read_csv_and_prepare_df(file_path)

        # Display the columns available in file
        self.display_columns_available_in_df(df)

        # Check if continuing with these columns or not
        df = self.alter_column_check(df)

        # Establish DB connection
        cursor, connection = self.establish_spms_db_connection_and_return_cursor_conn()

        # Get the entity with the name "DBCA" if it exists
        try:
            dbca_entity = Entity.objects.get(name="DBCA")
        except Entity.DoesNotExist:
            # If the entity does not exist, create it
            user, _ = User.objects.get_or_create(
                email="jarid.prince@dbca.wa.gov.au", username="jp"
            )
            user.set_password("1")
            user.is_superuser = True
            user.is_staff = True
            user.save()

            dbca_entity = Entity.objects.create(name="DBCA", key_stakeholder=user)

        # Insert data from the DataFrame into the BusinessArea model
        try:
            for row in df.itertuples(index=False):
                # Calculate the current year
                current_year = dt.now().year

                # Create the BusinessArea object
                business_area = BusinessArea(
                    old_pk=row.id,
                    entity_id=dbca_entity.id,
                    name=row.name,
                    slug=row.slug,
                    published=row.published,
                    is_active=row.is_active,
                    leader=row.leader_id,
                    finance_admin=row.finance_admin_id,
                    data_custodian=row.data_custodian_id,
                    focus=row.focus,
                    introduction=row.introduction,
                    image=None
                    # image=row.image,
                )

                business_area.save()

                # Save the BusinessArea object first
                business_area.save()

                # Create or get the BusinessAreaPhoto object
                business_area_photo, created = BusinessAreaPhoto.objects.get_or_create(
                    file=row.image,
                    defaults={
                        "year": current_year,
                        "business_area": business_area,
                        "uploader": dbca_entity.key_stakeholder,
                    },
                )

                # Assign the BusinessAreaPhoto to the BusinessArea
                business_area.image = business_area_photo
                business_area.save()

        except Exception as e:
            print(e)

        # Commit the changes and close the cursor and connection
        connection.commit()
        cursor.close()
        connection.close()

        print("Business Area Load operation finished.")

    def test_loader_function_two(self):
        print("loader function two successful")
