import sqlite3

class KonekDB:
    def __init__(self):
        self.filename = None
        self.conn = None
    
    def setDB(self,name):
        self.filename = name
    
    def dbCon(self):
        try:
            self.conn = sqlite3.connect(self.filename)
        except :
            print("File Tidak ditemukan")
        