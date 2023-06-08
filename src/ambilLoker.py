import mysql.connector as mysql
from datetime import datetime, timedelta

# Mengambil isi loker
def ambilLoker():
    conn = mysql.connect(
        host="localhost", #memakai host lokal
        user="lokermanage",
        password="1234",
        database="lokerdb"
    )

    # tampilin loker yang filled
    lokers = showOnlyFilled(conn)    
    
    ulang = True
    while ulang:
        print("\nmasukkan -99 untuk berhenti pengulangan")
        print("> index: ", end='')
        userinput = int(input())
        if(userinput in range(len(lokers))):
            loker = lokers[userinput]
            print("> Masukkan Password: ", end='')
            password = input()
            if(password == loker[3]):
                dateSimpan = loker[8]
                dateAmbil = datetime.now().date()
                harga = calculateHarga(dateAmbil=dateAmbil, dateSimpan=dateSimpan, lokerType=loker[1])
                print("Harga: Rp.", harga)
                id_loker = loker[0]
                setEmpty(conn, id_loker)
                addTransaction(conn, id_loker, harga)
            else:
                print("password salah!!!")

            # tunjukan ulang
            lokers = showOnlyFilled(conn)
        
        elif(userinput == -99):
            ulang = False
        else:
            print("Input berada diluar indeks")


def showOnlyFilled(conn):
    c = conn.cursor()
    sql = """select * from loker where filled=TRUE"""
    c.execute(sql)
    lokers = c.fetchall()
    print("\n\n\nBerikut daftar loker yang terisi")
    print("index|tipe|userNIK|userName|userPhone|userMail|dateSimpan")
    for i in range(len(lokers)):
        print(i, "|",  lokers[i][1], "|", lokers[i][4], "|", lokers[i][5], "|", lokers[i][6], "|", lokers[i][7], "|", lokers[i][8])
    return lokers


def addTransaction(conn, id_loker, harga):
    c = conn.cursor()
    sql = """INSERT INTO transaksi (lokerid, dateTransaksi, value) VALUES (%s, %s, %s);"""
    value = (id_loker, datetime.now().date(), harga)
    c.execute(sql, value)
    conn.commit()


def setEmpty(conn, id_loker):
    c = conn.cursor()
    sql = """UPDATE loker SET filled = 0, password=NULL, userNIK=NULL, userName=NULL, userPhone=NULL, userMail=NULL, dateSimpan=NULL  WHERE lokerid=%s"""
    value = (id_loker,)
    c.execute(sql, value)
    conn.commit()
    print("loker behasil dikosongkan")

def calculateHarga(dateAmbil, dateSimpan, lokerType):
    # calculate harga
    if((dateAmbil-dateSimpan).days > 2 and lokerType == 'big'):
        price = (dateAmbil-dateSimpan).days * 25000 * 1.2
    elif((dateAmbil-dateSimpan).days <= 2 and lokerType == 'big'):
        price = (dateAmbil-dateSimpan).days * 25000

    elif((dateAmbil-dateSimpan).days > 2 and lokerType == 'small'):
        price = (dateAmbil-dateSimpan).days * 15000 * 1.2
    elif((dateAmbil-dateSimpan).days <= 2 and lokerType == 'small'):
        price = (dateAmbil-dateSimpan).days * 15000    

    return price

