import sys, os
import gc
import misc
from ChoiceViewer import ChoiceViewer
from ChoiceLauncher import ChoiceLauncher
from FileHandler import FileHandler
from Extractor import Extractor
from Transformer import Transformer
from Loader import Loader
import pandas as pd


class Migrator:
    def __init__(self):
        self.main_looping = True
        self.choice_viewer = None
        self.choice_launcher = None
        self.file_handler = None
        self.extractor = None
        self.transformer = None
        self.loader = None
        self.extraction_functions = None
        self.transformation_functions = None
        self.loading_functions = None
        self.project = None
        self.projects_list = {
            "1": "SPMS",
            "2": "SPECIFY",
            # "3": so on
        }

    def display_projects(self):
        self.kawaii_print(list(self.projects_list.values()))

    def kawaii_print(self, lst):
        num_columns = (len(lst) + 3) // 4
        num_rows = 4

        new_list = [
            lst[num * num_rows : (num + 1) * num_rows] for num in range(num_columns)
        ]

        if not lst:
            print("No choices.")
            return

        col_width = max(len(word) for row in new_list for word in row) + 4

        misc.nls("Which project would you like to perform operations on?")
        print("CHOICES AVAILABLE:")
        for row in range(num_rows):
            for col in range(num_columns):
                if row < len(new_list[col]):
                    index = row + col * num_rows
                    key = list(self.projects_list.keys())[index]
                    value = new_list[col][row]
                    print(f"{key}) {value.ljust(col_width)}", end="")
            print()

    def select_project(self):
        choices = list(self.projects_list.keys())
        selection = None
        while selection not in choices:
            selection = input("Type '1' for SPMS, or '2' for 'SPECIFY':\n")
        self.project = self.projects_list[selection]
        misc.cls()
        print(f"{misc.bcolors.OKGREEN}{self.project} SELECTED!{misc.bcolors.ENDC}")

    def instantiate_classes(self):
        self.file_handler = (
            FileHandler(project=self.project, pd=pd, os=os, misc=misc)
            if self.file_handler == None
            else self.file_handler
        )
        self.extractor = Extractor(self.file_handler, misc)
        self.transformer = Transformer(self.file_handler, misc)
        self.loader = Loader(self.file_handler, misc)
        self.extraction_functions = self.extractor.functions
        self.transformation_functions = self.transformer.functions
        self.loading_functions = self.loader.functions
        self.choice_viewer = ChoiceViewer(
            misc,
            ef=self.extraction_functions,
            tf=self.transformation_functions,
            lf=self.loading_functions,
            file_handler=self.file_handler,
        )
        self.choice_launcher = ChoiceLauncher(misc, self.choice_viewer)

    def main_loop(self):
        self.instantiate_classes()
        self.choice_launcher.choice_viewer.check_view_input()
        self.main_looping = (
            self.choice_launcher.choice_viewer.display_functions_for_choice()
        )
        self.clean_up()

    def clean_up(self):
        del self.choice_launcher
        del self.choice_viewer
        # del self.file_handler
        del self.extractor
        del self.transformer
        del self.loader
        self.extraction_functions = None
        self.transformation_functions = None
        self.loading_functions = None
        gc.collect()


if __name__ == "__main__":
    misc.title(f"{misc.bcolors.WARNING}ETL Migrator{misc.bcolors.ENDC}")
    print(
        f"{misc.bcolors.HEADER}IMPORTANT: Please make sure you are in the correct directory for this file.{misc.bcolors.ENDC}"
    )
    migrator = Migrator()
    migrator.display_projects()
    migrator.select_project()
    while migrator.main_looping:
        migrator.main_loop()
    print("Exiting...")
