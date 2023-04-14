import os
import subprocess
import tempfile
import pandas as pd
import psycopg2
from misc import nls, bcolors
import environ
from pathlib import Path


def extract_tables(dump_file, output_folder_name):
    env = environ.Env()

    BASE_DIR = Path(__file__).resolve().parent
    environ.Env.read_env(os.path.join(BASE_DIR, ".env"))

    PGUSER = env("PGUSER")
    PGPASS = env("PGPASS")

    # print(BASE_DIR, PGUSER, PGPASS)

    # Create the output folder if it doesn't exist
    nls("Checking if output folder exists...")
    os.makedirs(output_folder_name, exist_ok=True)

    # Create a temporary PostgreSQL database
    nls(f"{bcolors.FAIL}Creating the temporary database{bcolors.ENDC}")
    with tempfile.TemporaryDirectory() as tmpdir:
        os.environ["PGDATA"] = tmpdir
        nls(f"{bcolors.HEADER}Running db init{bcolors.ENDC}")
        subprocess.run(["initdb"])
        nls(f"{bcolors.HEADER}Running pg_ctl start{bcolors.ENDC}")
        subprocess.run(["pg_ctl", "start"])
        nls(f"{bcolors.HEADER}Running createdb{bcolors.ENDC}")
        subprocess.run(["createdb", "tempdb"])

        # Load the dump file into the temporary database
        nls(f"{bcolors.HEADER}Loading dumpfile into temporary database{bcolors.ENDC}")
        subprocess.run(["pg_restore", "-U", "postgres", "-d", "tempdb", dump_file])
        nls(f"{bcolors.OKGREEN}COMPLETE!{bcolors.ENDC}")

        # Connect to the temporary database with pguser
        nls(f"{bcolors.HEADER}Connecting to temp db with user postgres{bcolors.ENDC}")
        with psycopg2.connect(dbname="tempdb", user=PGUSER, password=PGPASS) as conn:
            with conn.cursor() as cur:
                # Get the list of tables
                nls(f"{bcolors.HEADER}Getting list of tables{bcolors.ENDC}")
                cur.execute(
                    "SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'"
                )
                table_names = [row[0] for row in cur.fetchall()]

                # Export each table as a CSV file

                nls(f"{bcolors.HEADER}Exporting tables as CSV files{bcolors.ENDC}")
                for table_name in table_names:
                    nls(f"{bcolors.HEADER}Exporting {table_name}...{bcolors.ENDC}")
                    df = pd.read_sql(f"SELECT * FROM {table_name}", conn)
                    df.to_csv(f"{output_folder_name}/{table_name}.csv", index=False)
                    nls(f"{bcolors.OKGREEN}COMPLETE!{bcolors.ENDC}")

        # Shutdown the temporary PostgreSQL database
        nls(f"{bcolors.HEADER}Shutting down temporary database{bcolors.ENDC}")
        subprocess.run(["pg_ctl", "stop"])


if __name__ == "__main__":
    extract_tables("sdis.dump", "extracted_table_data")
