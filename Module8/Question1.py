import mysql.connector

# Establish database connection
connection = mysql.connector.connect(
         host='127.0.0.1',
         port=3306,
         database='gamedb',   # use your actual DB name
         user='root',
         password='907360270@aks',
         autocommit=True
)

icao = input("Enter the ICAO code of an airport: ")

cursor = connection.cursor()
sql = "SELECT name, municipality FROM airport WHERE ident=%s"
cursor.execute(sql, (icao,))
result = cursor.fetchone()

if result:
    print(f"Airport name: {result[0]}")
    print(f"Location: {result[1]}")
else:
    print("No airport found with that ICAO code.")