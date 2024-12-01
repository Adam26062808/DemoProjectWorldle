import sqlite3

db_name = 'wordle.db'
conn = None
cursor = None

def open():
    global conn, cursor
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

def close():
    cursor.close()
    conn.close()

def do(query):
    cursor.execute(query)
    conn.commit()

def make_table():
    open()
    do('''PRAGMA foreign_keys=on''')

    do('''CREATE TABLE IF NOT EXISTS wordle (
       id INTEGER PRIMARY KEY AUTOINCREMENT,
       words VARCHAR)''')
    
    do('''CREATE TABLE IF NOT EXISTS leaderboard ( 
       id INTEGER PRIMARY KEY AUTOINCREMENT, 
       name VARCHAR, 
       attempts INTEGER, 
       word_id INTEGER, 
       FOREIGN KEY (word_id) REFERENCES wordle (id))''')
    close()

def add_words():
    open()
    words = [('hamburger',),
             ('pizza',),
             ('audio',),
             ('playstation',),
             ('silly',),
             ('cook',),
             ('laptop',),
             ('screen',),
             ('account',),
             ('Table',),
             ('uniform',),
             ('unique',),
             ('galaxy',),
             ('Earth',),
             ('smartphone',),
             ('image',),
             ('mouse',),
             ('shark',),
             ('diamond',),
             ('dream',),
             ('imagine',),
             ('smile',),
             ('celebration',),
             ('kindness',),
             ('love',),
             ('applause',),
             ('balloon',),
             ('sunshine',),
             ('moonlight',),
             ('adventure',),
             ('explore',),
             ('incredible',),
             ('raspberry',),
             ('pineapple',),
             ('Cherry',),
             ('Snake',),
             ('Sugar',),
             ('running',),
             ('keyboard',),
             ('chocolate',),
             ('line',),
             ('basketball',),
             ('soccer',),
             ('arrow',),
             ('water',),
             ('lava',),
             ('gold',),
             ('iron',),
             ('crystal',),
             ('stone',),
             ('dirt',)]
        
    cursor.executemany('INSERT INTO wordle (words) VALUES (?)', words)
    conn.commit()
    close()

def get_words():
    open()
    cursor.execute('SELECT * FROM wordle')
    wordle_data = cursor.fetchall()
    close()
    return wordle_data


def get_player():
    open()
    cursor.execute('SELECT * FROM leaderboard')
    leaderboard_data = cursor.fetchall()
    close()
    return leaderboard_data

def make_datebase():
    make_table()
    add_words()

def add_player(name, attempts, word_id):
    open()
    cursor.execute("INSERT INTO leaderboard (name, attempts, word_id) VALUES (?,?,?)", (name, attempts, word_id))
    conn.commit()
    print(f"The player: {name}, takes {attempts} attemps to finish this {word_id} word")
    close()
def get_leaderboard(word_id):
    open()
    cursor.execute(f"SELECT * FROM leaderboard WHERE word_id = {word_id} ORDER BY attempts ASC")
    data = cursor.fetchall()
    close()
    return data