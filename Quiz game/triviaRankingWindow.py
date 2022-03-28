from tkinter import *
from tkinter import ttk

class RankingWindow:

    def __init__(self, root, players_ranking):
        self.ranking_window = Toplevel(root)
        self.ranking_window.title("Ranking")
        self.ranking_window.resizable(0,0)
        self.ranking_window.config( background= "#27272a")

        self.ranking_label = Label( self.ranking_window, text="RANKING", bg="#27272a", fg="#ffffff", font="Nunito 12 normal")
        self.ranking_label.grid( column=0, row=0)
        # Creamos la tabla donde se colocarán los datos del ranking.
        self.ranking_table = ttk.Treeview( self.ranking_window, columns=('#0','#1','#2','#3','#4'))
        self.ranking_table.grid( column=0, row=1)

        self.ranking_table.heading("#0", text="Top")
        self.ranking_table.heading("#1", text="Name")
        self.ranking_table.heading("#2", text="Age")
        self.ranking_table.heading("#3", text="Time")
        self.ranking_table.heading("#4", text="Correct")
        self.ranking_table.heading("#5", text="Category")
        # Tomamos la lista de ranking brindada y acomodamos cada
        # dato de la persona en su respectiva categoría.
        for x in range( len(players_ranking)):
            self.ranking_table.insert( "", END, text=f"{x+1}", values= (players_ranking[x][0], players_ranking[x][1], players_ranking[x][2], players_ranking[x][3], players_ranking[x][4]))