def count(x,y):
        if x == 1:
            x = 15000

        elif x == 2:
            x = 20000

        elif x == 3:
            x = 30000

        elif x == 4:
            x = 45000

        else:
            quit()

        if y > 48 :
            yz = (y - 48) # jam lembur
            xy = yz * 10000 # upah jam lembur
            y = (y - yz) * x # jam kerja bersih (tanpa lembur)
            print("gajimu segini ajh : Rp.", y + xy)

        else:
            y = y * x # jam kerja bersih (tanpa lembur)
            print("gajimu segini ajh : Rp.", y)



def main():
    try:
        x = int(input("golongan : "))

        y = int(input("jam kerja : "))

        count(x,y)

    except Exception as error:
        print('Error: ' + repr(error))
        # main() loop kekw

if __name__ == "__main__":
    main()
