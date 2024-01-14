import os
from typing import Dict

class PeapleRegisterView:

    def register_person_view(self) -> Dict:
        os.system("cls||clear")
        print("Registrar pessoa \n\n")
        name = input("Nome da pessoa: ")
        age = input("Idade da pessoa: ")
        height = input("Altura da pessoa: ")

        new_person_informations = {
            "name": name,
            "age": age,
            "height": height,
        }

        return new_person_informations