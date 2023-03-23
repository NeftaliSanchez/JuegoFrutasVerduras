import customtkinter
import runpy

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.geometry("400x240")


def run_fruits():
    runpy.run_module("game_fruits")
    

def run_vegetables():
    runpy.run_module("game_vefetables")


btnFruits = customtkinter.CTkButton(master=app, text="Frutas",command=run_fruits)
btnFruits.place(relx=0.5, rely=0.2, anchor=customtkinter.CENTER)

btnVegetables = customtkinter.CTkButton(master=app, text="Vegetales",command=run_vegetables)
btnVegetables.place(relx=0.5, rely=0.6, anchor=customtkinter.CENTER)
# btnPlay.pack()
app.mainloop()