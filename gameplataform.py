import customtkinter
from game import Game
from camera import Camera

class DificultFrame(customtkinter.CTkFrame):
    def __init__(self, master, title, values):
        super().__init__(master)
        self.grid_columnconfigure(0, weight=1)
        self.values = values
        self.title = title
        self.radiobuttons = []
        self.variable = customtkinter.StringVar(value="")

        self.title = customtkinter.CTkLabel(self, text=self.title, fg_color="gray30", corner_radius=6)
        self.title.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="ew")

        for i, value in enumerate(self.values):
            radiobutton = customtkinter.CTkRadioButton(self, text=value, value=value, variable=self.variable)
            radiobutton.grid(row=i + 1, column=0, padx=10, pady=(10, 0), sticky="w")
            self.radiobuttons.append(radiobutton)

    def get(self):
        if (len(self.variable.get()) == 0) or (self.variable.get() == "Facil"): return 0
        elif self.variable.get() == "Normal": return 1
        else: return 2

    def set(self, value):
        self.variable.set(value)

class GameType(customtkinter.CTkFrame):
    def __init__(self, master, title, values):
        super().__init__(master)
        self.grid_columnconfigure(0, weight=1)
        self.values = values
        self.title = title
        self.radiobuttons = []
        self.variable = customtkinter.StringVar(value="")

        self.title = customtkinter.CTkLabel(self, text=self.title, fg_color="gray30", corner_radius=6)
        self.title.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="ew")

        for i, value in enumerate(self.values):
            radiobutton = customtkinter.CTkRadioButton(self, text=value, value=value, variable=self.variable)
            radiobutton.grid(row=i + 1, column=0, padx=10, pady=(10, 0), sticky="w")
            self.radiobuttons.append(radiobutton)

    def get(self):
        if self.variable.get() == "Verduras": return "vegetables"
        else: return "fruits"

    def set(self, value):
        self.variable.set(value)

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.cap = Camera().start()
        self.title("Juego de frutas y verduras")
        self.geometry("350x240")
        self.set_appearance_mode("system")

        self.dif_frame = DificultFrame(self, "Dificultad", values=["Facil", "Normal","Dificil"])
        self.dif_frame.grid(row=1, column=0, padx=(0, 10), pady=(10, 0), sticky="nsew")
        self.game_frame = GameType(self,"Modo",values=["Frutas", "Verduras"])
        self.game_frame.grid(row=1, column=1, padx=(0, 10), pady=(10, 0), sticky="nsew")

        self.play = customtkinter.CTkButton(master=self, text="Jugar", command=self.play)
        self.play.grid(row=2, column=0, padx=10, pady=10, sticky="ew", columnspan=2)
        self.config = customtkinter.CTkButton(master=self, text="Configurar camara", command=self.conf)
        self.config.grid(row=3, column=0, padx=10, pady=10, sticky="ew", columnspan=2)

    def play(self):
        game = Game(dificult=self.dif_frame.get())
        game.cap = self.cap
        game.initialize(type=self.game_frame.get())
        game.loop()
    
    def conf(self):
        self.cap.config()

if __name__ == "__main__":
    app = App()
    app.mainloop()