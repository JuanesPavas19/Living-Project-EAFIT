def Pysort(datos):
    return sorted(datos)

def menuDieta():
    men = int(input("1. Id    2. nombre    3. info    4. duracion \n"))

    cursor = db.cursor()

    if men == 1:
        print('FORM Dieta SELECT * ORDER BY Id')
    elif men == 2:
        print('FROM Dieta SELECT * ORDER BY nombre')
    elif men == 3:
        print('FROM Dieta SELECT * ORDER BY info')
    elif men == 4:
        print('FROM Dieta SELECT * ORDER BY duración')

def menuRutina():
    menr = int(input("1. Id    2. nombre    3. info    4. dificultad \n"))

    cursor = db.cursor()

    if menr == 1:
        print('FORM Rutina SELECT * ORDER BY Id')
    elif menr == 2:
        print('FROM Rutina SELECT * ORDER BY nombre')
    elif menr == 3:
        print('FROM Rutina SELECT * ORDER BY info')
    elif menr == 4:
        print('FROM Rutina SELECT * ORDER BY dificultad')


def main():
    mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)
    print(menuDieta(mydb))

main()