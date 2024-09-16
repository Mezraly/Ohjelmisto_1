import mysql.connector
from geopy import distance

def ica1(x):
    sql = f"SELECT latitude_deg, longitude_deg FROM airport where ident='{x}'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount > 0:
        for rivi in tulos:
            ic1 = (rivi[0], rivi[1])
        return ic1

def ica2(y):
    sql = f"SELECT latitude_deg, longitude_deg FROM airport where ident='{y}'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount > 0:
        for rivi in tulos:
            ic2 = (rivi[0], rivi[1])
        return ic2
yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='Mezraly',
         password='1234765',
         autocommit=True
         )
x = input("anna ICAO koodi: ")
y = input("anna ICAO koodi: ")
print(distance.distance(ica1(x), ica2(y)).km)