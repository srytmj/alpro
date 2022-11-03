from discount import *
from admin import *
from os import system

def clear():
    system('clear')

def inp():
    y = int(input("Input : "))
    return y

def get_datas():
    x =  open('/workspaces/machinery/laundry/datas/settings.json')
    data = json.load(x)
    for x in data['settings']:
        if x == 'perkilos':
            perkilos = x['perkilos']
            break

        else:
            continue

    return

def menu1():
    print("""
    Laundry Uhuy
    """)
    weight = int(input("Masukan berat laundry : "))
    prices = weight * 5000 # perkilos
    method = input("""
Pilih Metode Pencucian
1. Kilat (1 hari)
2. Super Cepat (1-2 hari)
3. Cepat (2-3 hari)
4. Biasa (3-5 hari)
""")
    name = input("Atas Nama : ")

    # m_id, m_name, m_date = look_member(name)
    # print(m_id, m_name, m_date)

    # # convert membership year and month to month only so it can be subtracted to look membership type
    # membership_date = int(m_date[0:4]) * 12 + int(m_date[5:7])
    # converted_date = int(date[0:4]) * 12 + int(date[5:7])
    # membership_counter = converted_date - membership_date

    generate_discount_price(name, method, prices)

    return 

def menu2():
    print("""

    Pilih Menu
    1. Tambah Member Baru
    2. Lihat List Member
    3. Cari Member
    4. Hapus Member

            """)
    
    x = inp()
    match x:
        case 0:
            quit()

        case 1:
            new_member()
            back()

        case 2:
            read_member()
            back()
        
        case 3:
            x = input("masukan nama yang ingin dicari : ")
            m_id, m_name, m_date = look_member(x)
            print(f"""
==========================
{m_name} Data [{m_id}]
Terdatar pada {m_date}
==========================
        """)
            back()

        case 4:
            print("delete")
            
def back():
    x = input("Kembali ? [ y : n ]")
    if x == 'y':
        main()
    else:
        quit()

try:
    def main():
        clear()
        print("""
==========================
    Wilujeng Sumping    
                        
    1. Laundry          
    2. Admin            
                        
    0. Exit             
==========================""")
        x = inp()
        match x:
            case 0:
                quit()
            
            case 1:
                menu1()

            case 2:
                menu2()


except ValueError:
    print('program crashed')



if __name__ == "__main__":
    # main()
    get_datas()