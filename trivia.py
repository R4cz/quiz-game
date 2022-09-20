from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
from time import time

from triviaFunctions import *
from triviaGameWindow import *
from triviaConnection import *
from triviaRankingWindow import *
from triviaRegisterWindow import *

class App:

    def __init__(self):
        self.root = Tk()
        self.root.title("Trivia")
        self.root.resizable(0,0)
        self.root.config( background= "#27272a")
        # Creamos objetos de Conexión y Funciones para acceder a ellas.
        self.connection1 = Connection()

        self.functions = Functions()
        self.functions.register_player(self.root)

        self.categories_interface()

        self.root.mainloop()
    # MAIN WINDOW
    # Creamos la pantalla de inicio del juego donde, por ahora, solo hay dos categorías jugables.
    def categories_interface(self):
        Label( self.root, text="CATEGORIES", font="Nunito 14 normal", bg="#27272a", fg="#52b788").grid( column=0, row=0, padx=5, pady=15, columnspan=2)

        Label( self.root, text="Select a category. Five questions will be assigned to you randomly.\nOnce you have answered the question, press the 'Submit' button.", bg="#27272a", font="Nunito 12 normal", fg="#ffffff").grid( column=0, row=1, padx=15, columnspan=2)
        # Usamos la función lambda para ejecutar la misma función para
        # ambos botones pero con distintos datos brindados.
        Button( self.root, text="MATHEMATICS", command=lambda: self.play_category("Math"), width=15, height=5, background="#52b788", font="Nunito 14 normal", fg="#18181b", relief="flat").grid( column=0, row=2, padx=5, pady=35)
        Button( self.root, text="MISCELLANY", command=lambda: self.play_category("Miscellany"), width=15, height=5, background="#52b788", font="Nunito 14 normal", fg="#18181b", relief="flat").grid( column=1, row=2, padx=5, pady=35)

        self.options_labelframe = Label( self.root, bg="#27272a")
        self.options_labelframe.grid( column=0, row=3, padx=5, pady=5, columnspan=2)
        # Usamos la función lambda para brindar el dato que querramos
        # a la función que necesitemos.
        Button( self.options_labelframe, text="Register player", command=lambda: self.functions.register_player(self.root), font="Nunito 14 normal", bg="#18181b", fg="#ffffff", relief="flat").grid( column=0, row=0, padx=5, pady=5)
        Button( self.options_labelframe, text="Ranking", command=lambda: self.functions.show_ranking(self.root), font="Nunito 14 normal", bg="#18181b", fg="#ffffff", relief="flat").grid( column=1, row=0, padx=5, pady=5)

    # GAME WINDOW
    """ 
    Usamos una sola función para jugar cualquier categoría seleccionada. Inicamos el
    cronómetro, mezclamos números para obtener IDs de las preguntas y respuestas al azar,
    recuperamos las preguntas y respuestas, imprimimos las ventanas con las preguntas y
    vamos respondiendo una tras otra recuperdando las respuestas. Una vez respondidas todas
    las preguntas finalizamos el cronómetro. 

    Tomamos todos los datos del jugador, almacenados previamente, para añadirlo al ranking
    del juego. Finalmente mostramos un mensaje de Felicitaciones al jugador por completar
    el juego.
    """
    def play_category(self , table_name):
        # Iniciamos el cronómetro
        start_time = time()
        # Mezcla numeros del 1 al 20 y toma los primeros 5 de la lista para que
        # sean las preguntas y respuestas del juego.
        random_id = self.functions.shuffle_id_list()
        # Brindando las id y el nombre de la tabla, recuperamos la lista de
        # preguntas y respuestas. De acuerdo a la categoría elegida para jugar.
        questions_list, answers_list = self.functions.recover_game_data(random_id, table_name)
        # La función nos creará tantas ventanas como largo sea "random_id" una tras
        # otra. Tras responder cada pregunta, las respuestas se irán almacenando en
        # una lista para luego ser comparadas con las respuestas correctas.
        self.player_responses = self.functions.play_the_game( self.root, questions_list, answers_list, random_id)
        # Finalizamos el cronómetro.
        finish_time = time()
        # Encontramos el tiempo total que le tomó al jugador terminar el juego.
        total_time = finish_time - start_time
        self.time_elapsed = self.functions.time_converter(int(total_time))
        # Almacenamos la cantidad de respuestas correctas para añadir al jugador
        # al ranking del juego. Después de ser comparadas las respuestas.
        self.correct_answer_counter = self.functions.correct_questions(self.player_responses, random_id, table_name)
        # Tomamos los datos de nombre y edad del jugador almacenados previamente
        # para añadirlo al ranking del juego.
        name_player, age_player = self.functions.get_player_data()
        # Enviamos los datos recopilados necesarios para añadir al jugador al ranking.
        data = ( name_player, age_player, self.time_elapsed, self.correct_answer_counter, table_name)
        self.connection1.add_to_ranking(data)
        # Mostramos un mensaje de Felicitaciones al jugador por completar el juego.
        mb.showinfo("Congratulations!", "Well done!\nYou were added to the ranking of users who finished the game.")
# MAIN BLOCK
app1 = App()