import customtkinter
from game import Game

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Juego de frutas y verduras")
        # self.minsize(400, 300)
        self.geometry("400x240")
        self.set_appearance_mode("system")

        self.btnFruits = customtkinter.CTkButton(master=self, text="Frutas", command=self.runfruits)
        self.btnFruits.pack(padx=20, pady=20)
        self.btnVegetables = customtkinter.CTkButton(master=self, text="Vegetales", command=self.runvegetables)
        self.btnVegetables.pack(padx=20, pady=20)

    def runfruits(self):
        game = Game().loop()
    
    def runvegetables(self):
        game = Game().loop(type="vegetables")
 


if __name__ == "__main__":
    app = App()
    app.mainloop()