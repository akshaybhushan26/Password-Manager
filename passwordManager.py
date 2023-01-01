# Creating a password Manager in python with MySQL database as backend for storing user's credentials.

# Importing Modules
import mysql.connector

# Creating a connection with the database
db_connection = mysql.connector.connect(
  host = "localhost",
  user = input("\nEnter the username for the database (root): "), # "root" is the username for this system
  passwd = input("Enter the password for the database: "), # "lakshay24" is the password for this system
  database = "passwordManager"
  )
FLAG = True # Creating a flag variable to run the program in a loop

if db_connection.is_connected():
      print("\n >>> Database is successfully connected <<< ")

mycursor = db_connection.cursor() # Creating a cursor object to execute the queries

# Creating a table in the database
mycursor.execute("CREATE TABLE IF NOT EXISTS passManager (WEBSITE VARCHAR(200), USERNAME VARCHAR(200), PASSWORD VARCHAR(200))")

# Creating a function to add the credentials to the database
def add():
    website = input("Enter the Website's name to add: ")
    username = input("Now, Enter the Username for the website: ")
    password = input("and the Password: ")
    mycursor.execute("INSERT INTO passManager (WEBSITE, USERNAME, PASSWORD) VALUES (%s, %s, %s)", (website, username, password))
    db_connection.commit()
    print("\nYour credentials have been added successfully")

# Creating a function to view the credentials from the database
def view():
    data = []
    mycursor.execute("SELECT * FROM passManager")
    for x in mycursor:
        data.append(x)
    if len(data) == 0:
        print(" Sorry!!, no credentials found")
    else:
        for x in data:
            print("---------------------------------------------")
            print("Credentials for Website", x[0],"are: ")
            print("---------------------------------------------")
            print("Website :-> ", x[0])
            print("Username:-> ", x[1])
            print("Password:-> ", x[2])
            print("---------------------------------------------")

# Creating a function to delete the credentials from the database
def delete():
    website = input("Enter the Website's name you want to delete the data from: ")
    mycursor.execute("DELETE FROM passManager WHERE WEBSITE = %s", (website,))
    if mycursor.rowcount == 0:
        print("\nNo such website found!!")
    else:
        db_connection.commit()
        print("Your credentials have been deleted successfully")

# Creating a function to update the credentials from the database
def update():
    website = input("Enter the Website's name to update credentials for: ")
    username = input("Enter the Username for the website to change: ")
    password = input("and Enter the Password too: ")
    mycursor.execute("UPDATE passManager SET USERNAME = %s, PASSWORD = %s WHERE WEBSITE = %s", (username, password, website))
    if mycursor.rowcount == 0:
        print("\n Sorry!!, no such website found!!")
    else:
        db_connection.commit()
        print("\nYour credentials have been updated successfully!!")

# Creating a function to search the credentials from the database
def search():
    searchData = []
    website = input("Enter the Website's name you to want to search credentials for: ")
    mycursor.execute("SELECT * FROM passManager WHERE WEBSITE = %s", (website,))
    for x in mycursor:
        searchData.append(x)
    if len(searchData) == 0:
        print("\nSorry!! no credentials found for the website", website, ":(")
    else:
        for x in searchData:
            print("---------------------------------------------")
            print("Credentials for Website", x[0],"are: ")
            print("---------------------------------------------")
            print("Website :-> ", x[0])
            print("Username:-> ", x[1])
            print("Password:-> ", x[2])
            print("---------------------------------------------")

# Creating a function to display the menu
def menu():
    print()
    print("===========> Python-MySQL || Password-Manager <===========")
    print()
    print("---------------- by Akshay Bhushan ----------------")
    print()
    print("Select the option from the menu:")
    print("1. Add credentials")
    print("2. View credentials")
    print("3. Delete credentials")
    print("4. Update credentials")
    print("5. Search credentials")
    print("6. Exit")
    print()

# Creating a function to call the menu function and ask the user to enter the choice
def main():
    menu()
    choice = int(input("Enter your choice: "))
    print()
    if choice == 1:
        add()
    elif choice == 2:
        view()
    elif choice == 3:
        delete()
    elif choice == 4:
        update()
    elif choice == 5:
        search()
    elif choice == 6:
        global FLAG
        print("========= Thank you for using the program!! =========")
        FLAG = False
    else:
        print("Invalid choice")
        main()

# Calling the main function
while FLAG:
    main()