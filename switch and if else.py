gol1 = 15000
gol2 = 20000
gol3 = 30000
gol4 = 45000

def main():

    x = input("golongan : ")

    y = int(input("jam kerja : "))

    def call(ans):
        print("gajimu segini ajh : Rp.", ans)
    
    match x:

        case '1':

            if y > 48 :
                yz = (y - 48) # jam lembur
                xy = yz * 10000 # upah jam lembur
                y = (y - yz) * gol1 # jam kerja bersih (tanpa lembur)
                ans = y + xy
                call(ans)

            else:
                ans = y * gol1 # jam kerja bersih (tanpa lembur)
                call(ans)
                
        case '2':

            if y > 48 :
                yz = (y - 48) # jam lembur
                xy = yz * 10000 # upah jam lembur
                y = (y - yz) * gol2 # jam kerja bersih (tanpa lembur)
                ans = y + xy
                call(ans)

            else:
                ans = y * gol2 # jam kerja bersih (tanpa lembur)
                call(ans)

        case '3':

            if y > 48 :
                yz = (y - 48) # jam lembur
                xy = yz * 10000 # upah jam lembur
                y = (y - yz) * gol3 # jam kerja bersih (tanpa lembur)
                ans = y + xy
                call(ans)
        
            else:
                ans = y * gol3 # jam kerja bersih (tanpa lembur)
                call(ans)

        case '4':

            if y > 48 :
                yz = (y - 48) # jam lembur
                xy = yz * 10000 # upah jam lembur
                y = (y - yz) * gol4 # jam kerja bersih (tanpa lembur)
                ans = y + xy
                call(ans)

            else:
                ans = y * gol4 # jam kerja bersih (tanpa lembur)
                call(ans)

        case _:
            print("out of order")
        
if __name__ == "__main__":
    main()
