class Mahasiswa:
    alamat = "Jl. Jendral Soedirman"
    hp = "12345678910"

    def __init__(self, nama, nim, jumlah_sks, ipk):
        self.nama = nama
        self.nim  = nim
        self.jumlah_sks = jumlah_sks
        self.ipk = ipk

    def print_out(self):
        print("Nama       : ", self.nama)
        print("NIM        : ", self.nim)
        print("Alamat     : ", self.alamat)
        print("No. HP     : ", self.hp)
        print("Jumlah sks : ", self.jumlah_sks)
        print("IPK        : ", self.ipk)

    def info(self):
        print("Good Job Boy!!") 

Data = Mahasiswa("Fadiel Nurdiansyah", "121140143", 90, 3.30)
Data.print_out()
Data.info()