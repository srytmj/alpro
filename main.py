#import func
import datetime

waktu = datetime.datetime.utcnow()+datetime.timedelta(hours=7)

hari=int(waktu.strftime("%d"))
bulan=(waktu.strftime("%m"))
tahun=(waktu.strftime("%y"))

print(f'tanggal: {hari}/{bulan}/{tahun}')
print(waktu)

kuota_biasa = [0,0,0]

#menu paket kuota (dika)

def input_kuota(kuota, hari, harga):
    print(f"Kuota yang anda pilih: {kuota}GB - {hari} Hari -Rp. {harga}")
    pilihan = input('Konfimasi pembelian (y/n) :').lower()
    
    if (pilihan=='y'):
        print('SELAMAT,paket anda telah di tambahkan')
        print('Mengembalikan anda ke menu awal')
        kuota_biasa.clear()
        # 
        kuota_biasa.append(kuota)
        kuota_biasa.append(hari)
        kuota_biasa.append(harga)

    else:
        print("pembelian digagalkan, kembali ke menu utama")
        return 0, 0, 0


def beli_kuota():
    kuota1 = '42Gb 30hr 100rb'
    kuota2 = '30Gb 15hr 75rb'
    kuota3 = '25Gb 30hr 25rb(spesial)'
    kuota4 = '117Gb 30hr 117rb'

    print(f"""
        1.{kuota1}
        2.{kuota2}
        3.{kuota3}
        4.{kuota4}
        0. Kembali
         """)
    paket = int(input("pilih paket :"))
    
    if (paket==1):
        paket = [42, 30, 100000]
        print(f'apakah anda yakin membeli paket {kuota1}?')
        input_kuota(paket[0], paket[1], paket[2])   

    elif (paket==2):
        paket = [30, 15, 75000]
        print(f'apakah anda yakin membeli paket {kuota2}?')

        input_kuota(paket[0], paket[1], paket[2])
        
    elif (paket==3):
        paket = [25, 30, 25000]
        print(f'apakah anda yakin membeli paket {kuota3}?')

        input_kuota(paket[0], paket[1], paket[2])
        
    elif (paket==4):
        paket = [117, 30, 117000]
        print(f'apakah anda yakin membeli paket {kuota4}?')

        input_kuota(paket[0], paket[1], paket[2])


#menu custom kuota
def custom_kuota():
    kuota_custom=int(input("pilih jumlah Gigabyte kuota (2000/Gb): "))
    masa_aktif=int(input("pilih masa aktif (1000/Hari): "))
    harga= ((kuota_custom*2000)+(masa_aktif*1000))
    print(f'Beli kuota sebesar {kuota_custom}Gb dengan masa aktif {masa_aktif}hr, total pembayaran sebesar : {harga}?')
    konfirmasi=input("1.Beli\n2.menu\n pilih opsi: ")
    if (konfirmasi=='1'):
        print(f'selamat pembelian kuota anda sebesar {kuota_custom} Gigabyte dengan masa aktif {masa_aktif} hari berhasil!')
        print("mengembalikan ke menu")
        return kuota_custom, masa_aktif
        
    elif (konfirmasi=='2'):
        custom_kuota()
    else:
        print("input tidak ditemukan, mengalihkan anda ke menu awal")
        
    
#menu ekstensi masa aktif(reni/manda)
def cek_masa_aktif():
    masa_aktif=0
    hari_tambah= int(input("tambah brp hari?"))
    masa_aktif+hari_tambah
    
#cek kuota aktif
# def cek_kuota_aktif():

#     x = beli_kuota
#     kuota_paket,masa_paket= input_kuota(x)
#     print (f"Sisa kuota anda adalah {kuota_paket} | dengan masa berlaku {masa_paket} hari (aktif sampai dengan )")


#main page(beli paket kuota, beli custom kuota, ekstensi masa aktif, cek kuota aktif, keluar)
def mainpage():

    print ("---------------------------\n 1.Beli paket kuota\n 2.Beli custom kuota\n 3.Ekstensi masa aktif\n 4.Cek kuota aktif\n 5.Keluar\n ---------------------------")
    menu = int(input("pilih menu :"))
    if (menu==1):
        beli_kuota()

    elif (menu==2):
        custom_kuota()
    elif (menu==3):
        cek_masa_aktif()
    elif (menu==4):
        print(f"{kuota_biasa[0]}GB - {kuota_biasa[1]}Hari -Rp. {kuota_biasa[2]}")
    elif (menu==5):
        quit()
    else:
        print ("error")


while True:
    mainpage()
