import sqlite3

class Database:
    def __init__(self):
        self.conn = sqlite3.connect('mouse_data.db', check_same_thread=False)
        self.c = self.conn.cursor()
        self.c.execute('''CREATE TABLE IF NOT EXISTS mouse_data (x INTEGER, y INTEGER, image_path TEXT)''')
        self.conn.commit()

    def save_mouse_data(self, x, y, image_path):
        self.c.execute("INSERT INTO mouse_data (x, y, image_path) VALUES (?, ?, ?)", (x, y, image_path))
        self.conn.commit()
