username = ("informatika")
password = ("12345678")

v = 1

while(v <= 3):
    inUser = input("masukkan username : ")
    inPassword = input("masukkan password : ")

    if(inUser == username and inPassword == password):
        print("Login Berhasil!!")
        break
    elif(v == 3):
        print("Akun terblokir!!")
        break
    else:
        print("Username dan password yang anda masukkan salah coba lagi")
        v += 1