import mysql.connector as mysql
from datetime import datetime, timedelta

# Mengambil isi loker
def simpanLoker():
    conn = mysql.connect(
        host="localhost", #memakai host lokal
        user="lokermanage",
        password="1234",
        database="lokerdb"
    )
    c = conn.cursor()
    

    
    # tampilin loker yang filled
    sql = """select * from loker where filled=False"""
    c.execute(sql)
    lokers = c.fetchall()
    print("Menjalankan simpan loker ================>")
    print("Berikut daftar loker yang kosong")
    print("index|lokerid|tipe")
    for i in range(len(lokers)):
        print(i, "|",  lokers[i][0], "|", lokers[i][1])
    
    ulang = True;
    while ulang:
        print("\nmasukkan -99 untuk berhenti pengulangan")
        print("> index: ", end='')
        userinput = int(input())
        if(userinput in range(len(lokers))):
            id_loker = lokers[userinput][0]
            setFull(conn, id_loker)
        elif(userinput == -99):
            ulang = False
        else:
            print("Input berada diluar indeks")

def setFull(conn, id_loker):
    c = conn.cursor()
    print("Masukkan password: ", end='')
    password = input()
    print("Masukkan userNIK: ", end='')
    userNIK = input()
    print("Masukkan userName: ", end='')
    userName = input()
    print("Masukkan userPhone: ", end='')
    userPhone = input()
    print("Masukkan userMail: ", end='')
    userMail = input()
    dateSimpan = datetime.now().date()

    sql = """UPDATE loker SET filled=1, password=%s, userNIK=%s, userName=%s, userPhone=%s, userMail=%s, dateSimpan=%s WHERE lokerid=%s;"""
    value = (password, userNIK, userName, userPhone, userMail, dateSimpan, id_loker)
    c.execute(sql, value)
    conn.commit()
    print("loker behasil diisi")
