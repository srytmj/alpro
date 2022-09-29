import os

def clear():
    os.system('clear')
    print("""
  _______ _ _        _   
 |__   __(_) |      | |  
    | |   _| | _____| |_ 
    | |  | | |/ / _ \ __|
    | |  | |   <  __/ |_ 
    |_|  |_|_|\_\___|\__|
    """)

tdewasa = [100]
tanak = [100]

def count(x,y,z):
    ax = x * 20000
    ay = y * 5000
    xy = ax + ay
    az = z - xy

    if z < xy :
        clear()
        input("Maaf Uang anda tidak mencukupi yang tandanya kamu sangant miskin, tekan Enter untuk kembali")
        main()
    else:
        clear()
        print(f"""
Jumlah tiket yang akan dibeli : 
{x}x Dewasa = {ax}
{y}x Anak-anak = {ay}
Total = {xy}
=====================
Uang pembayaran = {z}
        """)
        if not az == 0:
            print(f"Kembali = {az}")
        count.ans = input("Apakah pesanan sudah benar? [ y / n ]\nInput : ")
        return

def menu(x):
    if x == '1':
        clear()
        print("""
Daftar harga tiket
    1x Dewasa = Rp. 20.000
    1x Anak-anak = Rp. 5.000
        """)
        x = int(input("Berapa Tiket Dewasa Yang akan dibeli \nInput : "))
        y = int(input("Berapa Tiket anak-anak Yang akan dibeli \nInput : "))
        z = int(input("Masukan jumlah nominal uang anda \nInput : "))

        count(x,y,z)

        if count.ans == "y" :
            clear()
            print("terimakasih sudah membeli tiket kami yang tidak jelas tiket apa")
            tdewasa.append(x)
            tanak.append(y)
            print(f"""
Jumlah penipuan jual beli tiket hari ini 
dewasa : {sum(tdewasa)} tiket
anak-anak : {sum(tanak)} tiket""")
        # elif ans == "n" :
        #     main()
        else: 
            main()

    elif x == "2":
        print("letter is Suzuki")
    
    elif x == "3":
        print("fruit is Yamaha")

def main():
    if __name__ == "__main__":
        clear()
        print("""
    hello selamat welkom
    pilih menu anda
    --------------------
    1. Pesan tiket
    2. Menu Admin
        """)
        x = input("Masukan Nilai Input : ")
        menu(x)

main()
