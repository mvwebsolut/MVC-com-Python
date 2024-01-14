import os
from typing import Dict

class PeapleFinderView:

    def find_person_view(self) -> Dict:
        os.system("cls||clear")
        print("Buscar pessoas \n\n")
        name = input("Nome da pessoa: ")

        person_finder_information = {
            "name": name
        }

        return name