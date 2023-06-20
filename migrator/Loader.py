class Loader:
    def __init__(self, file_handler, misc):
        self.misc = misc
        self.file_handler = file_handler
        self.specify_source = ""
        self.spms_source = ""
        self.spms_functions = [
            {"name": "Load Business Areas", "function": self.load_business_areas},
            {"name": "Loader Function Two", "function": self.test_loader_function_two},
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

    def load_business_areas(self):
        self.file_handler.clean_directory
        print("loader function one successful")

    def test_loader_function_two(self):
        print("loader function two successful")
