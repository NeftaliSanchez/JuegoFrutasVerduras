import customtkinter
from game import Game
from camera import Camera

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.cap = Camera().start()
        print(type(self.cap))

        self.title("Juego de frutas y verduras")
        # self.minsize(200,200)
        self.geometry("200x200")
        self.set_appearance_mode("system")

        self.btnFruits = customtkinter.CTkButton(master=self, text="Frutas", command=self.runfruits)
        self.btnFruits.pack(padx=20, pady=20)
        self.btnVegetables = customtkinter.CTkButton(master=self, text="Vegetales", command=self.runvegetables)
        self.btnVegetables.pack(padx=20, pady=20)
        self.btnconfig = customtkinter.CTkButton(master=self, text="Configuración", command=self.config)
        self.btnconfig.pack(padx=40, pady=20)

    def runfruits(self):
        game = Game()
        game.cap = self.cap
        game.initialize()
        game.loop()
    
    def runvegetables(self):
        game = Game()
        game.cap = self.cap
        game.initialize(type="vegetables")
        game.loop()
    
    def config(self):
        self.cap.config()

if __name__ == "__main__":
    app = App()
    app.mainloop()