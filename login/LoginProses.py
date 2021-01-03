from database import KonekDB
from view import Awal
import time
class LoginProses:
    def __init__(self):
        self.username = None
        self.password = None
        self.sess = 0
        self.errorLogin = None
        self.konek = KonekDB()
        self.c = None
        self.konek.setDB("projek.db")
        self.konek.dbCon()
        self.c = self.konek.conn.cursor()

    def resetErrorLogin(self):
        self.errorLogin = 0 

    def getUser(self):
        return self.username

    def getKonek(self):
        return self.konek

    def getErrorLogin(self):
        return self.errorLogin

    def setUser(self,user):
        self.username = user
    
    def setSess(self,sess):
        self.sess = sess

    def setPassword(self,passwd):
        self.password = passwd

    def getSess(self):
        return self.sess
    

    def register(self,user,passwd):
        try:
            self.c.execute("INSERT INTO login(username,password) VALUES('%s','%s')" % (user,passwd))
            self.konek.conn.commit()
            return 1
        except :
            return 0

    def auth(self):
        self.errorLogin = 0
        self.c.execute("SELECT * from login WHERE username = '%s' and password = '%s' " % (self.username,self.password))
        if self.c.fetchone() is not None:
            self.sess = 1
            Awal.berhasilLogin()
        else:
            Awal.gagalLogin()