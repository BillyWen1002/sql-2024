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


#this prints out my agent roles
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

#this function prints out the agent names along with the winrate
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

#this function prints out the agent names along with the gender
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

#this function prints out the agent names along with the strongest maps
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

#this function prints out the agent names along with the ult points needed to get their ult
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

#this function prints out the agent names along with the released year
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

#this function deletes the agent from the data base 
def deleting_data():
    change = input("What is the ID of the agent you would like to remove\n")
    db = sqlite3.connect('valorant.db')
    cursor = db.cursor()
    sql = f'''DELETE FROM agents WHERE agent_id = "{change}"'''
    cursor.execute(sql)
    db.commit()

#this function asks for the info for the new agent the user wishs to input an inserts the data into the database
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


#this function edits the agent data how ever the user wishs and it get saved to the database
def edit_agent_data():
    agent_id = input("Enter the ID of the agent you want to edit: ")
    db = sqlite3.connect('valorant.db')
    cursor = db.cursor()
    sql = "SELECT * FROM agents WHERE agent_id = ?"
    cursor.execute(sql, (agent_id,))
    agent = cursor.fetchone()
    if agent:
        agent_name = agent[1]
        role = agent[2]
        winrate = agent[3]
        gender = agent[4]
        strongest_map = agent[5]
        ult_points = agent[6]
        released_year = agent[7]
        print("Current Agent Details:")
        print("1. Name:", agent[1])
        print("2. Role:", agent[2])
        print("3. Winrate:", agent[3])
        print("4. Gender:", agent[4])
        print("5. Strongest Map:", agent[5])
        print("6. Ult Points:", agent[6])
        print("7. Released Year:", agent[7])
        attribute = input("Enter the number of the attribute you want to edit (or 0 to cancel): ")
        if attribute == "0":
            return
        new_value = input("Enter the new value: ")
        if attribute == "1":
            agent_name = new_value
        elif attribute == "2":
            role = new_value
        elif attribute == "3":
            winrate = new_value
        elif attribute == "4":
            gender = new_value
        elif attribute == "5":
            strongest_map = new_value
        elif attribute == "6":
            ult_points = new_value
        elif attribute == "7":
            released_year = new_value
        else:
            print("Invalid attribute number.")
            return
        sql = f"UPDATE agents SET agent_name=?, role=?, winrate=?, gender=?, strongest_map=?, ult_points=?, released_year=? WHERE agent_id=?"
        cursor.execute(sql, (agent_name, role, winrate, gender, strongest_map, ult_points, released_year, agent_id))
        db.commit()
        print("Agent data updated successfully.")
    else:
        print("Agent not found.")

    

#main code
#this code prints out all the functions the user can select from
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
                       "\n10. Edit data"
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
        edit_agent_data()
    else:
        print("That was not an option\n")