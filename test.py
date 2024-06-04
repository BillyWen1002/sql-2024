import sqlite3

DATABASE = 'cars.db'

def print_all_cars():
    speed = input("what speed: ")
    with sqlite3.connect(DATABASE) as db:
        cursor = db.cursor()
        sql = "SELECT car_name FROM,top_speed car WHERE top_speed > ?;"
        cursor.execute(sql,(speed,))
        results = cursor.fetchall()
        #print them nicely

        for car in results:
            print(f"Car: {car[0]} Top Speed : {car[1]}")


if __name__== "__main__":
   print_all_cars()