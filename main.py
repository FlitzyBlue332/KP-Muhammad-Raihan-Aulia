import src.ambilLoker as al
import src.simpanLoker as sl
import src.transaksi as tr

ulang = True
while ulang:
    print("\n\nSelamat datang di LOKERMANAGE!!!")
    print("Silahkan pilih salah satu dari menu berikut untuk memilih fitur")
    print("\n\n")
    print("1. AmbilLoker")
    print("2. SimpanLoker")
    print("3. UnduhTransaksi")
    print("\n> Pilihan: ", end='')
    inputUser = input()
    if(inputUser == "AmbilLoker" ):
        al.ambilLoker()
    elif(inputUser == "SimpanLoker"):
        sl.simpanLoker()
    elif(inputUser == "UnduhTransaksi"):
        tr.unduhtransaksi()
    else:
        print("Input salah, masukan hanya boleh AmbilLoker, SimpanLoker, atau UnduhTransaksi")