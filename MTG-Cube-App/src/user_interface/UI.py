from entities.cube import Cube
import entities.card as Card
import data.saver_loader as saver
import os
from printer.printer import print_list_imgs, print_list_table
import filter.filter as filter
from user_interface.filter_ui import filter_ui
INITIAL_ACTIONS = {
    1: "luo uusi cube",
    2: "lataa vanha cube",
    3: "luo cube tiedostosta",
    0: "lopeta"
}

CUBE_ACTIONS = {
    1: "1 lisää kortti",
    2: "2 poista kortti",
    3: "3 printtaa cube tekstinä",
    4: "4 printtaa cube kuvina",
    5: "5 tallenna cube",
    6: "6 suodata cube",
    0: "0 lopeta"
}


def initialUI():
    while True:
        for i in INITIAL_ACTIONS:
            print(f"'{i}' : {INITIAL_ACTIONS[i]}")
        action = int(input("Anna komento: "))
        if action == 0:
            print("Heippa!")
            break
        if action == 1:
            name = input("Nimeä Cube: ")
            new_cube = Cube(name)
            cubeUI(new_cube)
        if action == 2:
            name = input("Ladattava Cube: ")
            cubeUI(saver.load(name))
        if action == 3:
            txt_file_name = input("Tiedostonimi, josta lista haetaan: ")
            if os.path.exists("src/card_list_text_files/"+txt_file_name):
                name_for_cube = input("Nimi luotavalle Cubelle: ")
                cubeUI(saver.load_from_list(name_for_cube, txt_file_name))
            else:
                print("Tällä nimellä ei löytynyt listaa. Sisällytithän '.txt' syötteeseen?"+"\n")

def cubeUI(cube: Cube):
    while True:
        for i in CUBE_ACTIONS:
            print(f"'{i}' : {CUBE_ACTIONS[i]}")
        action = int(input("Anna komento: "))
        if action == 0:
            print("Palataan")
            break
        if action == 1:
            name = input("Kortin nimi: ")
            if Card.card_test(name) == True:
                cube.add_card(name)
            else:
                print("Kortin nimellä haku ei onnistunut")
        if action == 2:
            name = input("Kortin nimi: ")
            cube.remove_card(name)
        if action == 3:
            print_list_table(cube)
        if action == 4:
            print_list_imgs(cube)
        if action == 5:
            if os.path.exists(f"src/data/Saved_Cubes/{cube.name}.db"):
                confirmation = input(
                    "Tällä nimellä on jo cube olemassa. Haluatko varmasti tallentaa sen päälle? Y/n: ")
                if confirmation == "Y":
                    print("Tallennettu")
                    os.remove(f"src/data/Saved_Cubes/{cube.name}.db")
                    saver.save(cube)
                    print("Tallennettu")
                else:
                    print("Ei tallennettu")
            else:
                saver.save(cube)
                print("Tallennettu")
        if action == 6:
            cube = filter_ui(cube)

# os.remove("src/entities/Saved_Cubes/Pallo.db")

# kuutio = cube_and_cards.Cube("Pallo")
# kuutio.add_card("Black Lotus")
# kuutio.add_card("vampiric tutor")
# kuutio.add_card("island")
# kuutio.add_card("plains")
# kuutio.add_card("forest")
# print(kuutio.collection)
# saver.save(kuutio)
# for i in kuutio.collection:
#     print(i)
# lataus = load("Pallo")
# print(lataus)
# print(type(lataus))
# print(lataus.collection)
# for i in lataus.collection:
#     print(i)
