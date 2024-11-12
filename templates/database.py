import sqlite3
db_name = 'wordle.sqlite'
conn = None
curor = None

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
    do('''PRAGMA foriegn_key = on ''')

    do('''CREATE TABLE IF NOT EXITST worlde (
        id INTERGER PRIMARY KEY,
        words VARCHAR)''')

    do('''CREATE TABLE IF NOT EXITST leaderboard(
        id INTERGER PRIMARY KEY,
        name VARCHAR,
        attemps INTERGER,
        word_id INTERGER,
        FORIEGN KEY (word_id) REFERENCES wordle (id))''')
    close()

def add_words():
    open()
    words= [('hamburger',), 
            ('pizza',),
            ('audio',),
            ('playstation',),
            ('silly',),
            ('cook',),
            ('laptop',),
            ('screen',),
            ('account',),
            ('Table',),
            ]

    cursor.executemany('INSERT INTO wordle (words) VALUES(?)', words)
    conn.commit()
    close()