from tkinter import *
from tkinter import ttk

class GameWindow:
    
    def __init__(self, root, questions_list, answers_list, x):
        self.game_window = Toplevel(root)
        self.game_window.resizable(0,0)
        # Imprime la pregunta en la ventana.
        ttk.Label( self.game_window, text=f"Question {x+1}").grid( column=0, row=0)
        ttk.Label( self.game_window, text=f"{questions_list[x][0][1]}").grid( column=0, row=1)
        # Enlista las respuestas en un RadioButton para que solo puede elegir una respuesta.
        self.selector = StringVar()
        self.selector.set(-1)
        for y in range( len( answers_list[x])):
            ttk.Radiobutton( self.game_window, text=f"{answers_list[x][y][1]}", variable=self.selector, value=answers_list[x][y][1]).grid( column=0, row= y + 2)

        ttk.Button( self.game_window, text="Submit", command=self.submit).grid( column=0, row= y + 3)
    # Espera que se cierre la ventana de juego para mandar la opción seleccionada.
    def get_answer(self):
        self.game_window.wait_window()
        return self.selector.get()
    # Destruye/cierra la ventana.
    def submit(self):
        self.game_window.destroy()