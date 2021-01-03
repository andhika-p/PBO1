from login import LoginProses
from view import Awal
from .Kalori import Kalori
import time

class MainControl:
    def __init__(self):
        self.session = None
        self.login = LoginProses()
        self.user = None
        self.passwd = None

    def eksekusiLogin(self,user,passwd):
        self.login.setUser(user)
        self.login.setPassword(passwd)
        self.login.auth()


    def sessRegister(self):
        while True:
            Awal.register()
            masukan = input(f"atau Ketik Exit untuk Keluar\n")
            try:
                user = masukan.split(";")[0]
                passwd = masukan.split(";")[1]
                hasil = self.login.register(user,passwd)
                if hasil == 1:
                    Awal.berhasilRegister()
                    time.sleep(2)
                    return 1
            except :
                if masukan.lower()== 'exit':
                    Awal.keluar()
                    return 0 
                else:
                    Awal.userError()
                    time.sleep(1)
                    

    def sessLogin(self):
        while True:
            Awal.login()
            masukan = input(f"atau Ketik Exit untuk Keluar\n")
            try:
                self.user = masukan.split(";")[0]
                self.passwd = masukan.split(";")[1]
                self.login.resetErrorLogin()
                self.eksekusiLogin(self.user,self.passwd)
                self.session = self.login.getSess()
                if self.session == 1:
                    Awal.berhasilLogin()
                    time.sleep(.5)
                    outSess = self.sessMenu()
                    if outSess == 0:
                        return 0 
                else:
                    Awal.gagalLogin()
                    time.sleep(.5)
                    # self.run()
            except :
                if masukan.lower()== 'exit':
                    Awal.keluar()
                    return 0
                else:
                    pass
                    # Awal.userError()
                    # time.sleep(0.5)
                
            
    def sessMenu(self):
        while True:
            try:
                Awal.menu()
                masukan = input(f"masukan pilihan \n")
                while masukan not in ['1','2','3']:
                    masukan = input(f"input salah mohon masukan kembali ")
            
                if masukan == '3':
                    Awal.keluar()
                    return 0
                if masukan =='1':
                    outsess = self.sessTambahKalori()
                    if outsess == 0:
                        return 0
                if masukan == '2':
                    outShow = self.sessShowKalori()
                    if outShow == 0:
                        return 0
            except Exception as e:
                print(e)
                time.sleep(1)

    def sessTambahKalori(self):
        kal = Kalori()
        while True:
            Awal.tambahKalori()
            masukan = input(f"atau Ketik exit untuk keluar\n")
            try:
                masukan = float(masukan)
                outkal = kal.insertKalori(masukan,self.user)
                if outkal == 1:
                    Awal.berhasilTambah()
                    pilihan = input()
                    if pilihan == "":
                        return 1
                    if pilihan == "exit":
                        Awal.keluar()
                        return 0
                else :
                    Awal.gagalTambah()
                    return 1
            except :
                if masukan.lower() == 'exit':
                    Awal.keluar()
                    return 0
                else:
                    Awal.userError()
                    time.sleep(1)

    def sessShowKalori(self):
        kal = Kalori()
        while True:
            kal.showKalori(self.user)
            masukan = input()
            try:
                while masukan not in ["","exit"]:
                    masukan = input(f"masukan salah mohon diulangi")
                if masukan == "":
                    return 1
                elif masukan.lower() == "exit":
                    Awal.keluar()
                    return 0                
            except:
                pass

            

    def run(self):
        while True:
            Awal.home()
            pilihan = input(f"masukan inputan (Ketik exit untuk keluar) ")
            while pilihan not in ['1','2','3']:
                pilihan = input(f"input salah mohon masukan kembali ")
            if pilihan == '3':
                Awal.keluar()
                return 
            if pilihan == '1':
                hasilLogin = self.sessLogin()
                if hasilLogin ==0:
                    return
            if pilihan == '2':
                hasilRegist = self.sessRegister()
                if hasilRegist == 0:
                    return 

        


