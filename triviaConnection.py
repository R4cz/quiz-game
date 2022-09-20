import sqlite3

class Connection:

    def open( self):
        connection = sqlite3.connect( "./QUIZ.db")
        return connection

    def recover_qa( self, var, table, id):
        try:
            con = self.open()
            cursor = con.cursor()
            sql = f"select {id},{var} from {table} where id={id}"
            cursor.execute( sql)
            return cursor.fetchall()
        finally:
            con.close()

    def consultation(self, table, id):
        try:
            con = self.open()
            cursor = con.cursor()
            sql = f"select answer from {table} where id={id} and value='correct'"
            cursor.execute( sql)
            return cursor.fetchall()
        finally:
            con.close()
    
    def add_to_ranking(self, data):
        con = self.open()
        cursor = con.cursor()
        sql = f"insert into TriviaRanking( name, age, time_elapsed, correct, category) values {data}"
        cursor.execute(sql)
        con.commit()
        con.close()

    def recover_ranking(self):
        try:
            con = self.open()
            cursor = con.cursor()
            sql = "select name,age,time_elapsed,correct,category from TriviaRanking"
            cursor.execute( sql)
            return cursor.fetchall()
        finally:
            con.close()