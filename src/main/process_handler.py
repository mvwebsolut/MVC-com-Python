from .constructor.introduction_process import introduction_process
from .constructor.peaple_finder_constructor import peaple_finder_constructor
from .constructor.peaple_register_constructor import peaple_register_constructor

def start() -> None:
    while True:
        command = introduction_process()
        if command == "1": peaple_register_constructor()
        elif command == "2": peaple_finder_constructor()
        elif command == "5": exit()
        else: print("\n Comando não encontrado ! \n\n")


