#docstring- Billy Wen- valorant agent database application
#imports
import sqlite3

#contants and variables
DATABASE = "valorant.db"


#functions
def print_all_agents():
    '''print all the agents nicely'''
    db = sqlite3.connect('valorant.db')
    cursor = db.cursor()
    sql = "SELECT * from agents;"
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through the results
    print("NAME                                    ROLE                WINRATE   GENDER    BEST MAP    ULT POINTS   RELEASED YEAR")
    for agents in results:
        print(f"{agents[1]:<40}{agents[2]:<20}{agents[3]:<10}{agents[4]:<10}{agents[5]:<12}{agents[6]:<12}{agents[7]:<12}")
    #llop finished here
    db.close()



def print_all_agents_role():
    '''print all the agents nicely'''
    db = sqlite3.connect('valorant.db')
    cursor = db.cursor()
    sql = "SELECT * from agents "
    "ORDER BY role;"
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through the results
    print("name                                    ROLE")
    for agents in results:
        print(f"{agents[1]:<40} {agents[2]:<20}")
    #llop finished here
    db.close()

def print_all_agents_winrate():
    '''print all the agents nicely'''
    db = sqlite3.connect('valorant.db')
    cursor = db.cursor()
    sql = "SELECT * from agents ORDER BY winrate desc;"
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through the results
    print("name                                    WINRATE")
    for agents in results:
        print(f"{agents[1]:<40}{agents[3]:<10}")
    #llop finished here
    db.close()

def print_all_agents_gender():
    '''print all the agents nicely'''
    db = sqlite3.connect('valorant.db')
    cursor = db.cursor()
    sql = "SELECT * from agents;"
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through the results
    print("name                                    Gender")
    for agents in results:
        print(f"{agents[1]:<40}{agents[4]:<10}")
    #llop finished here
    db.close()

def print_all_agents_strongest_map():
    '''print all the agents nicely'''
    db = sqlite3.connect('valorant.db')
    cursor = db.cursor()
    sql = "SELECT * from agents;"
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through the results
    print("name                                    Strongest map")
    for agents in results:
        print(f"{agents[1]:<40}{agents[5]:<10}")
    #llop finished here
    db.close()

def print_all_agents_ult_points():
    '''print all the agents nicely'''
    db = sqlite3.connect('valorant.db')
    cursor = db.cursor()
    sql = "SELECT * from agents ORDER BY ult_points desc;"
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through the results
    print("name                                    Ult points needed")
    for agents in results:
        print(f"{agents[1]:<40}{agents[6]:<10}")
    #llop finished here
    db.close()

def print_all_agents_released_year():
    '''print all the agents nicely'''
    db = sqlite3.connect('valorant.db')
    cursor = db.cursor()
    sql = "SELECT * from agents ORDER BY released_year desc;"
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through the results
    print("name                                    Released year")
    for agents in results:
        print(f"{agents[1]:<40}{agents[7]:<10}")
    #llop finished here
    db.close()

def deleting_data():
    change = input("What is the ID of the agent you would like to remove\n")
    db = sqlite3.connect('valorant.db')
    cursor = db.cursor()
    sql = f'''DELETE FROM agents WHERE agent_id = "{change}"'''
    cursor.execute(sql)
    db.commit()

def print_new_agents():
    number = input("What is the agent's ID number? ")
    name = input("What is the agent's name? ")
    role = input("What is the agent's role? ")
    winrate = input("What is the agent's winrate? ")
    gender = input("What is the agent's gender? ")
    map = input("What is the agent's strongest map? ")
    ult = input("What is the agent's ult point needed for ult? ")
    released = input("What is the agent's released year? ")

    db = sqlite3.connect('valorant.db')
    cursor = db.cursor()
    sql = f"INSERT INTO agents VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
    cursor.execute(sql, (number, name, role, winrate, gender, map, ult, released))
    db.commit()
    db.close()
    

#main code
while True:
    user_input = input("\nWhat would you like to do."
                       "\n1. Print all agents in the agent id order from lowest to highest"
                       "\n2. Print agent name + role"
                       "\n3. Print agent name + winrate from highest to lowest"
                       "\n4. Print agent name + gender"
                       "\n5. Print agent name + strongest map"
                       "\n6. Print agent name + ult points from most to least"
                       "\n7. Print agent name + released year from newest to oldest"
                       "\n8. Input new data"
                       "\n9. Delete row"
                       "\nYou: ")
    if user_input == "1":
        print_all_agents()
    elif user_input == "2":
        print_all_agents_role()
    elif user_input == "3":
        print_all_agents_winrate()
    elif user_input == "4":
        print_all_agents_gender()
    elif user_input == "5":
        print_all_agents_strongest_map()
    elif user_input == "6":
        print_all_agents_ult_points()
    elif user_input == "7":
        print_all_agents_released_year()
    elif user_input == "8":
        print_new_agents()
    elif user_input == "9":
        deleting_data()
    elif user_input == "10":

    else:
        print("That was not an option\n")