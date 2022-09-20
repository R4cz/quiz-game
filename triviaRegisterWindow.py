from tkinter import *
from tkinter import ttk

class RegisterWindow:
    # Se crea la ventana de Registro para que al terminar el juego el jugador quede
    # registrado en el ranking.
    def __init__(self, root):
        self.register = Toplevel(root)
        self.register.title( "Register Player")
        self.register.config( background= "#27272a")
        self.register.resizable(0,0)

        self.name_label = Label( self.register, text="Name:", background="#27272a", foreground="#ffffff", font="Nunito 12 normal").grid( column=0, row=0, padx=5, pady=5)
        self.age_label = Label( self.register, text="Age:", background="#27272a", foreground="#ffffff", font="Nunito 12 normal").grid( column=0, row=1, padx=5, pady=5)

        self.name = StringVar()
        self.name_entry = Entry( self.register, width=15, textvariable=self.name, background="#27272a")
        self.name_entry.grid( column=1, row=0, padx=5, pady=5)
        self.name_entry.config( font="Nunito 14 normal", relief="ridge", background="#27272a", foreground="#ffffff")
        self.age = StringVar()
        self.age_entry = Entry( self.register, width=15, textvariable=self.age)
        self.age_entry.grid( column=1, row=1, padx=5, pady=5)
        self.age_entry.config( font="Nunito 14 normal", relief="ridge", background="#27272a", foreground="#ffffff")

        self.register_player_button = Button( self.register, text="Submit", command=self.submit, relief="flat", font="Nunito 12 normal", bg="#18181b", fg="#ffffff").grid( column=0, row=2, pady=5, columnspan=2)

        self.register.protocol("WM_DELETE_WINDOW", self.submit)
        self.register.grab_set()
    # Espera que se cierre la ventana de registro para mandar los datos de name y age.
    def get_data(self):
        self.register.wait_window()
        return (self.name.get(), self.age.get())
    # Destruye/cierra la ventana.
    def submit(self):
        self.register.destroy()