import mysql.connector

def ica(x):
    sql = f"SELECT type, count(type) FROM airport where iso_country='{x}' group by type"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount > 0:
        for rivi in tulos:
            print(f"Tyyppi: {rivi[0]}: {rivi[1]}")
        return
yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='Mezraly',
         password='1234765',
         autocommit=True
         )
inp = input("anna koodi: ")
ica(inp)