import customtkinter
from game import Game
from camera import Camera

class Messege(customtkinter.CTkFrame):
    def __init__(self,master,title,msg):
        super().__init__(master)
        self.title = title
        self.msg = msg

        self.title = customtkinter.CTkLabel(self,text=self.title, fg_color="gray30", corner_radius=6)
        self.title.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="ew", columnspan=2)
        self.ms = customtkinter.CTkLabel(self,text=self.msg,justify ="left")
        self.ms.grid(row=1, column=0, padx=10, pady=(10, 0), sticky="ew", columnspan=2)
        

class ChosseFrame(customtkinter.CTkFrame):
    def __init__(self, master, title, values, orientaton):
        super().__init__(master)
        self.grid_columnconfigure(5, weight=1)
        self.values = values
        self.title = title
        self.orientaton = orientaton
        self.radiobuttons = []
        self.variable = customtkinter.StringVar(value="")

        self.title = customtkinter.CTkLabel(self, text=self.title, fg_color="gray30", corner_radius=6)
        if self.orientaton == "vertical":
            self.title.grid(row=0, column=0, padx=10, pady=10, sticky="ew")
        else: 
             self.title.grid(row=0, column=0, padx=10, pady=10, sticky="ew", columnspan=len(self.values))

        for i, value in enumerate(self.values):
            radiobutton = customtkinter.CTkRadioButton(self, text=value, value=value, variable=self.variable)
            if self.orientaton == "vertical":
                radiobutton.grid(row=i + 1, column=0, padx=10, pady=(10, 0), sticky="w")
            else:
                radiobutton.grid(row=4, column=i+1, padx=10, pady=10, sticky="w")
            self.radiobuttons.append(radiobutton)

    def getdif(self):
        if (len(self.variable.get()) == 0) or (self.variable.get() == "Facil"): return 0
        elif self.variable.get() == "Normal": return 1
        else: return 2

    def gettype(self):
        if self.variable.get() == "Verduras": return "vegetables"
        else: return "fruits"

    def getcam(self):
        if len(self.variable.get()) == 0: return "0"
        else: return self.variable.get()

    def set(self, value):
        self.variable.set(value)


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Juego de frutas y verduras")
        self.geometry("350x650")
        self.set_appearance_mode("system")
        self.grid_columnconfigure((1, 1), weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.cap = Camera()
        self.flag = False



        msggame = '''
1. Antes de jugar debes configurar la camara, prueba 
seleccionando un número de camara y luego da en el 
botón Configura camara. Si se muestra tu rostro sigue 
con el siguiente paso, de no ser así prueba con otro 
número de camara hasta que veas video.

2. Una vez configurada la camara, puedes seleccinar el 
nivel de dificultad y el modelo con el que quieras jugar. 
Puedes cambiar estos valores las veces que quieras.

** Con la tecla r puedes reniciar la partida mientras 
estas dentro del juego.

'''
        self.intromsg = Messege(self,title='¿Como jugar?',msg=msggame)
        self.intromsg.grid(row=0, column=0, padx=10, pady=10, sticky="ew", columnspan=2)

        # Camera configuration
        self.game_camera = ChosseFrame(self,"Número de camara",values=["0","1","2"],orientaton ="horizontal")
        self.game_camera.grid(row=1, column=0, padx=10, pady=10, sticky="nsew", columnspan=2)
        self.config = customtkinter.CTkButton(master=self, text="Configurar camara", command=self.conf)
        self.config.grid(row=2, column=0, padx=10, pady=10, sticky="ew", columnspan=2)

        # Game configuration
        self.dif_frame = ChosseFrame(self, "Dificultad", values=["Facil", "Normal","Dificil"],orientaton ="vertical")
        self.dif_frame.grid(row=3, column=0, padx=(0, 10), pady=(10, 0), sticky="nsew")
        self.game_frame = ChosseFrame(self,"Modo",values=["Frutas", "Verduras"],orientaton ="vertical")
        self.game_frame.grid(row=3, column=1, padx=(0, 10), pady=(10, 0), sticky="nsew")    

        self.play = customtkinter.CTkButton(master=self, text="Jugar", command=self.play)
        self.play.grid(row=4, column=0, padx=10, pady=10, sticky="ew", columnspan=2)

    def play(self):
        if self.flag == False: 
            self.cap.start()
            self.flag = True
        game = Game(dificult=self.dif_frame.getdif())
        game.cap = self.cap
        game.initialize(type=self.game_frame.gettype())
        game.loop()
    
    def conf(self):
        self.cap.numcamera = int(self.game_camera.getcam())
        self.cap.config()

if __name__ == "__main__":
    app = App()
    app.mainloop()