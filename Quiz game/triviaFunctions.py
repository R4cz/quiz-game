from random import shuffle

from triviaFunctions import *
from triviaGameWindow import *
from triviaConnection import *
from triviaRankingWindow import *
from triviaRegisterWindow import *

class Functions:

    connection2 = Connection()
    # Mezcla números del 1 al 20 en una lista y devuelve los primeros 5 números.
    def shuffle_id_list(self):
        id_list = list( range( 1, 20))
        shuffle(id_list)
        return id_list[:5]

    def recover_game_data(self, random_id, table_name):
        # Recupera el ID y la pregunta en un conjunto [( ID, Pregunta),...]
        random_questions_list = []
        for id in random_id:
            math_question = self.connection2.recover_qa( "question", f"{table_name}Questions", f"{id}")
            random_questions_list.append(math_question)
        # Recupera tres conjuntos, los cuales tienen el mismo ID y una respuesta correcta,
        # las otras dos son incorrectas. [[( ID, Respuesta), ( ID, Respuesta), ( ID, Respuesta)],...]
        random_answers_list = []
        for id in random_id:
            math_answer = self.connection2.recover_qa( "answer", f"{table_name}Answers", f"{id}")
            random_answers_list.append(math_answer)
        # Recupera la lista de preguntas y respuestas seleccionadas previamente.
        return (random_questions_list, random_answers_list)
    #creates the window of the next question once the previous one is finished, it also adds the answers of each question in a list.
    # Crea la ventana de la siguiente pregunta una vez que la anterior haya finalizado, también añade la respuesta de cada pregunta en una lista.
    def play_the_game(self, root, questions_list, answers_list, random_id):
        player_responses = []
        for x in range( len(random_id)):
            create_window = GameWindow( root, questions_list, answers_list, x)
            player_responses.append(create_window.get_answer())
        return player_responses
    # Convierte los segundos, controlados por el cronómetro, en minutos.
    def time_converter( self, time):
        x = 0
        if time >= 60:
            while time>= 60:
                x+= 1
                time-=60
            if len( str(time)) == 1:
                return str(x)+":0"+str(time)
            elif len( str(time)) == 2:
                return str(x)+":"+str(time)
        else:
            if len( str(time)) == 1:
                return "0:0"+str(time)
            elif len( str(time)) == 2:
                return "0:"+str(time)
    # Compara las respuestas del jugador con las respuestas correctas de la base de datos
    # y los cuenta, pudiendo añadir al jugador al ranking de acuerdo a sus respuestas.
    def correct_questions(self, player_responses, random_id, table_name):
        correct_answer_counter = 0

        correct_answer_list = []
        # Recupera las respuestas correctas de la base de datos.
        for id in random_id:
            correct_answer = self.connection2.consultation( f"{table_name}Answers", f"{id}")
            correct_answer_list.append(correct_answer)
        # Compara la respuesta del jugador con la respuesta correcta de la base de datos.
        for x in range( len(random_id)):
            if str(player_responses[x]) == str(correct_answer_list[x][0][0]):
                correct_answer_counter+= 1
        # Recupera la cantidad de respuestas correctas del jugador.
        return correct_answer_counter
    #OPTIONS BUTTONS
    def register_player(self, root):
        self.register = RegisterWindow(root)
        # Espera que la ventana de registro se cierre para almacenar los datos.
        self.name_player, self.age_player = self.register.get_data()
    # Recupera los datos del jugador desde otro Objeto.
    def get_player_data(self):
        return (self.name_player, self.age_player)
        
    def show_ranking(self, root):
        # Recupera los datos del Ranking de la base de datos.
        players_ranking = self.connection2.recover_ranking()
        # Ordena a los jugadores de acuerdo a las respuestas correctas.
        for k in range( len( players_ranking) - 1):
            for x in range( len( players_ranking) - (k + 1)):
                if players_ranking[x][3] < players_ranking[x+1][3]:
                    aux = players_ranking[x]
                    players_ranking[x] = players_ranking[x+1]
                    players_ranking[x+1] = aux
        # Si tuvieran la misma cantidad de respuestas correctas se compara el tiempo
        # que les tomó completar el juego.
        for k in range( len( players_ranking) - 1):
            for x in range( len( players_ranking) - (k +1)):
                if players_ranking[x][3] == players_ranking[x+1][3] and players_ranking[x][2] > players_ranking[x+1][2]:
                    aux = players_ranking[x]
                    players_ranking[x] = players_ranking[x+1]
                    players_ranking[x+1] = aux
        # Crea la ventana del Ranking a partir de la lista ordenada que se le brinda.
        RankingWindow( root, players_ranking)