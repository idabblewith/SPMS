class Extractor:
    def __init__(self, file_handler, misc):
        self.misc = misc
        self.file_handler = file_handler
        self.spms_functions = [
            {
                "name": "Extractor Function One",
                "function": self.test_extractor_function_one,
            },
            {
                "name": "Extractor Function Two",
                "function": self.test_extractor_function_two,
            },
            {
                "name": "Extractor Function Three",
                "function": self.test_extractor_function_three,
            },
        ]
        self.specify_functions = [
            {
                "name": "Extractor Function Four",
                "function": self.test_extractor_function_four,
            },
            {
                "name": "Extractor Function Five",
                "function": self.test_extractor_function_five,
            },
            {
                "name": "Extractor Function Six",
                "function": self.test_extractor_function_six,
            },
            {
                "name": "Extractor Function Seven",
                "function": self.test_extractor_function_seven,
            },
        ]
        self.functions = []
        self.set_func = self.determine_functions(self.file_handler.project)

    def determine_functions(self, project):
        funcs = []
        if project == "SPMS":
            funcs = self.spms_functions
        elif project == "SPECIFY":
            funcs = self.specify_functions

        self.functions = funcs

    def test_extractor_function_one(self):
        print("Extractor function one successful")

    def test_extractor_function_two(self):
        print("Extractor function two successful")

    def test_extractor_function_three(self):
        print("Extractor function three successful")

    def test_extractor_function_four(self):
        print("Extractor function four successful")

    def test_extractor_function_five(self):
        print("Extractor function five successful")

    def test_extractor_function_six(self):
        print("Extractor function six successful")

    def test_extractor_function_seven(self):
        print("Extractor function seven successful")
