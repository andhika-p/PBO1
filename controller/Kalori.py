from login import LoginProses
import datetime
from view import Awal
class Kalori:
    def __init__(self):
        try:
            self.log = LoginProses() 
            self.db = self.log.getKonek()
            self.username = self.log.getUser()
        except Exception as e:
            print(e)
        
    def insertKalori(self,nilaiKalori,user):
        try:
            c = self.db.conn.cursor()
            c.execute('INSERT INTO kalori(user,kalori,tanggal) VALUES("%s","%s","%s")' % (user,nilaiKalori,datetime.datetime.now()))
            self.db.conn.commit()
            return 1
        except :
            return 0

    def showKalori(self,user):
        try:
            c = self.db.conn.cursor()
            c.execute("SELECT * FROM kalori where user='%s'"%(user))
            tampil = c.fetchall()
            Awal.lihatKalori()
            if len(tampil) > 0 :
                print(f"Data Riwayat kalori untuk user '%s'" %(user))
                print(f"| Nomor\t | Kalori\t | Tanggal & Waktu\t\t |")
                for i in range(len(tampil)):
                    nomor = i+1
                    kalori = tampil[i][2]
                    tanggal = tampil[i][3]
                    print(f"| '%s'\t | '%s'\t | '%s'\t |" % (nomor,kalori,tanggal))
                print(f"\ntekan enter untuk kembali ke menu sebelumnya"
                f"\natau tekan exit untuk keluar")
                return 1
            else:
                print(f"\ntidak ada riwayat ditemukan\n"
                f"mohon mengisi data terlebih dahulu")
                print(f"\ntekan enter untuk kembali ke menu sebelumnya"
                f"\natau tekan exit untuk keluar")
        except :
            return 0
