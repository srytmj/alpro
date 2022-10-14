from ast import Pass
import os
import pandas as pd
import getpass
import pytz
from datetime import datetime
from tabulate import tabulate

# B Surya Atmaja
# 6703220051
# suryatmaja@student.telkomuniversity.ac.id

def sysclear():
    os.system('clear')
    print("""
  _______ _ _        _   
 |__   __(_) |      | |  
    | |   _| | _____| |_ 
    | |  | | |/ / _ \ __|
    | |  | |   <  __/ |_ 
    |_|  |_|_|\_\___|\__|
    """)

date = ["test"]
tdewasa = [100]
tanak = [100]
pw = "adadeh"

def count(x,y,z):
    
    ax = x * 20000
    ay = y * 5000
    xy = ax + ay
    az = z - xy

    if y == 2:        # discount 20% if buy 2 children ticket, simple
        ay = ay / 0.2

    if z < xy :
        sysclear()
        input("Maaf Uang anda tidak mencukupi yang tandanya kamu sangant miskin, tekan Enter untuk kembali")
        main()
        
    else:
        sysclear()
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
        
        ans = input("Apakah pesanan sudah benar? [ y / n ]\nInput : ")
        
        if ans == 'y' :
            tdewasa.append(x)
            tanak.append(y)
            date.append(str(datetime.now(pytz.timezone('Etc/GMT+8')).strftime("%m/%d/%Y %H:%M:%S")))
            buy()
            
        else: 
            main()

        return
        
        
def buy():
    sysclear()
    print("terimakasih sudah membeli tiket kami yang tidak jelas tiket apa")
    
    a = input("Ingin kembali ke menu utama? [ y / n ]\nInput : ")
    if a == 'y':
        main()
    else :
        quit()

        
def menu(x):
    try:
        if x == '1':
            sysclear()
            print("""
    Daftar harga tiket
        1x Dewasa = Rp. 20.000
        1x Anak-anak = Rp. 5.000
            """)
            x = int(input("Berapa Tiket Dewasa Yang akan dibeli \nInput : "))
            y = int(input("Berapa Tiket anak-anak Yang akan dibeli \nInput : "))
            z = int(input("Masukan jumlah nominal uang anda \nInput : "))

            count(x,y,z)

        elif x == "2":
            sysclear()
            pasw = getpass.getpass('?')
            
            if pasw.lower() == pw:
                sysclear()

                d = {'Tanggal Jual': date, 'Tiket Dewasa': tdewasa, 'Tiket Anak-anak': tanak}
                pdtabulate = lambda df: tabulate(df, headers='keys', tablefmt='pretty', showindex=False)
                df = pdtabulate(d)

                print(f"""
{df}
- - - - - - - - - - - - - - - - - - - - - - - - -
Jumlah penipuan jual beli tiket hari ini 
dewasa : {sum(tdewasa)} tiket
anak-anak : {sum(tanak)} tiket
- - - - - - - - - - - - - - - - - - - - - - - - -
Total untung : Rp.{(sum(tdewasa) * 20000) + (sum(tanak) * 5000)}
                """)
                input()
                main()
                
            else:
                sysclear()
                input(f"{pasw}, really? did you just input this things into my program?")
                main()
        
        elif x == "0":
            quit()

        else :
            sysclear()
            print("Input anda diluar nalar")
            input()
            main()

    except Exception as error:
        sysclear()
        print('Error: ' + repr(error))
        input("TLDR Input anda diluar nalar yang menjadikan program error \ntekan Enter untuk kembali ke menu utama....")
        main()


def main():
    sysclear()
    print("""
    hello selamat welkom
    pilih menu anda
    --------------------
    1. Pesan tiket
    2. Menu Admin


    0. Tutup Program
    """)
    menu(input("Masukan Nilai Input : "))

if __name__ == "__main__":
    main()
