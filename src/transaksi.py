import mysql.connector as mysql
from datetime import datetime, date

def unduhtransaksi():
    conn = mysql.connect(
        host="localhost", #memakai host lokal
        user="lokermanage",
        password="1234",
        database="lokerdb"
    )
    c = conn.cursor()

    print("Tanggal Awal: ")
    dariTanggal = inputDate()

    print("\n\nTanggal Akhir: ")
    sampaiTanggal = inputDate()
    sql = """select * from transaksi where dateTransaksi >= %s and dateTransaksi < %s"""
    value = (dariTanggal, sampaiTanggal)
    c.execute(sql, value)
    res = c.fetchall()
    
    
    print("\nMasukkan nama file: ")
    filename = input() + ".csv"
    f = open(filename, 'w')

    header = "idTransaksi;lokerid;dateTransaksi;value\n"
    datas = []
    for r in res:
        datas.append(r)
    f.write(header)
    for data in datas:
        datastring = str(data[0])+";"+str(data[1])+";"+str(data[2])+";"+str(data[3])+"\n"
        f.write(datastring)
    f.close()

def inputDate():
    print("> tahun: ", end='')
    tahun = int(input())
    print("> bulan: ", end='')
    bulan = int(input())
    print("> tanggal: ", end='')
    tanggal = int(input())

    while bulan > 12 or tanggal > 31:
        print("Input salah, mohon masukkan tanggal dan bulan yang benar")
        print("> tahun: ", end='')
        tahun = int(input())
        print("> bulan: ", end='')
        bulan = int(input())
        print("> tanggal: ", end='')
        tanggal = int(input())

    return date(tahun, bulan, tanggal)