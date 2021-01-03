from LoginProses import LoginProses

class LogoutProses:
    def __init__(self):
        self.user = None
        self.sess = 0
        self.login = LoginProses()
        
    
    def logout(self):
        self.login.setSess(self.sess)