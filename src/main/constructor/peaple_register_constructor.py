from src.views.peaple_register_view import PeapleRegisterView

def peaple_register_constructor():
    peaple_register_view = PeapleRegisterView()

    # controller

    new_person_informations = peaple_register_view.register_person_view()

    # envia para o controller

