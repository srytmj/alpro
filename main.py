makanan_data = ["Bakso", "Mie Yamin"]
makanan_harga = [9000, 8000]

minuman_data = ["Es Jeruh", "Es Teh"]
minuman_harga = [3000, 2000]

pesan_makan = {}
pesan_minum = {}

def pesan(data, harga, pesan):
    if data == makanan_data:
        aa = "Makanan"
    else:
        aa = "Minuman"

    print(f"""=============================================\nMenu {aa}""")

    for x, y, z in zip(range(0,len(data)), data, harga):
        print(f"{x+1}. {y} - {z}")

    if data == makanan_data:
        w = "Porsi"
    else:
        w = "Gelas"

    input_data = int(input("Pilih menu : "))
    input_jumlah = int(input(f"{w} : "))
    pesan[len(pesan)] = [data[input_data-1], input_jumlah, input_jumlah*harga[input_data-1]]

def struk():
    print("""============ Pembelian ============""")
    total_beli = 0
    for x in pesan_makan:
        data = pesan_makan[x]

        menu = data[0]
        jumlah = data[1]
        total_harga = data[2]
        print(f"""{jumlah}x {menu} 
        Rp.{total_harga}""")
        total_beli += total_harga

    print("\nTotal harus Dibayar: Rp",total_beli)
    uang=int(input("Uang Tunai Pembeli: Rp "))
    
    if uang < total_beli:
        print("Maaf uang anda tidak cukup")
        quit()
        
    kembalian=int(uang-total_beli)
    print("Kembalian :",kembalian)


def end():
    choice = input("Ingin pesan kembali? [y/n]\n").lower()
    if choice == "y":
        main()

    else:
        struk()

def main():
    menu = int(input("""====== Selamat datang di Resto Apadaya ======
1. Pesan Makan
2. Pesan Minum\nInput = """))

    if menu == 1:
        pesan(makanan_data, makanan_harga, pesan_makan)
        end()   
        
    if menu == 2:
        pesan(minuman_data, minuman_harga, pesan_minum)
        end()

main()
