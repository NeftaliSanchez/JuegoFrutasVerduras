#!/usr/bin/python
import customtkinter
import os

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.geometry("400x240")

def run_fruits():
    run_game('fruits')

def run_vegetables():
    run_game('vegetables')

def run_game(chosse: str) -> None:
    absolutepath = os.path.abspath(__file__)
    # print(absolutepath)
    fileDirectory = os.path.dirname(absolutepath)
    # print(fileDirectory)
    rpython = f'{fileDirectory}\\env\\Scripts\\python.exe'
    if chosse == 'fruits': 
        fgame = f'{fileDirectory}\\game_fruits.py'
    elif chosse == 'vegetables':
        fgame = f'{fileDirectory}\\game_vefetables.py'
    os.system(rpython +' '+ fgame)


btnFruits = customtkinter.CTkButton(master=app, text="Frutas",command=run_fruits)
btnFruits.place(relx=0.5, rely=0.2, anchor=customtkinter.CENTER)

btnVegetables = customtkinter.CTkButton(master=app, text="Vegetales",command=run_vegetables)
btnVegetables.place(relx=0.5, rely=0.6, anchor=customtkinter.CENTER)
# btnPlay.pack()
app.mainloop()