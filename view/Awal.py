import os
class Awal:
    
    @staticmethod
    def hapusLayar():
        if os.name == 'posix':
            os.system('clear')
        else:
            os.system('cls')


    @staticmethod
    def home():
        Awal.hapusLayar()
        print(f"Selamat datang di Aplikasi Pencatat Kalori\n"
        f"silahkan Pilih Menu Dibawah ini : \n"
        f"1. Login\n"
        f"2. Register\n"
        f"3. Exit dari Program \n")

    @staticmethod
    def login():
        Awal.hapusLayar()
        print(F"Silahkan masukan Username dan password\n"
        f"format Username;Password\n")
    
    @staticmethod
    def register():
        Awal.hapusLayar()
        print(F"Selamat datang di menu Registrasi \n"
        f"Silahkan isikan username dan password anda untuk bergabung \n"
        f"Format Username;Password\n")
    
    @staticmethod
    def menu():
        Awal.hapusLayar()
        print(f"Silahkan memilih menu yang diinginkan:\n"
        f"1. Tambah Konsumsi Kalori Per Hari \n"
        f"2. Lihat Riwayat Konsumsi Kalori \n"
        f"3. Keluar")

    @staticmethod
    def tambahKalori():
        Awal.hapusLayar()
        print(f"Silahkan masukan kalori yang anda konsumsi hari ini  \n")

    @staticmethod
    def lihatKalori():
        Awal.hapusLayar()
        print(f"Selamat datang di menu lihat Kalori")

    @staticmethod
    def keluar():
        Awal.hapusLayar()
        print(f"++++ terimakasih sudah menggunakan Aplikasi Pencatat Kalori Ini ++++")
    
    @staticmethod
    def berhasilLogin():
        Awal.hapusLayar()
        print(f"Berhasil Login")

    @staticmethod
    def gagalLogin():
        Awal.hapusLayar()
        print(f"Login Gagal Username / Password salah")

    @staticmethod
    def userError():
        Awal.hapusLayar()
        print(f"maaf Format masukan salah")

    @staticmethod
    def berhasilRegister():
        Awal.hapusLayar()
        print(f"Selamat anda berhasil Register \n"
        f"Sesaat lagi anda akan di redireksi ke halaman awal.. ")
    
    @staticmethod
    def gagalRegister():
        Awal.hapusLayar()
        print(f"Maaf Anda Gagal Register")

    @staticmethod
    def berhasilTambah():
        Awal.hapusLayar()
        print(f"data kalori berhasil ditambahkan untuk saat ini \n"
        f"ketik enter untuk kembali ke menu sebelumnya \n"
        f"atau ketik 'exit' untuk keluar dari program")

    @staticmethod
    def gagalTambah():
        Awal.hapusLayar()
        print(f"data kalori gagal ditambah \n anda akan di redirect kembali ke halaman sebelumnya")
   