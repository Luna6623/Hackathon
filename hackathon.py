import mysql.connector as sql

import subprocess

import sys

conn = sql.connect(host = "localhost", user = "sqluser",passwd = "password",database = "HACKATHON_DB")

cursor = conn.cursor()

loop = True

def participant_func():
    user_solution = input("Enter the name of your solution file: ")
    result = (subprocess.run([sys.executable, user_solution], capture_output=True, text=True, check=True)).stdout

    print(result)

    partic_finder = "SELECT * FROM HACKATHON WHERE solution = %s"
    
    partic_sql = (result.strip(), )
    

    cursor.execute(partic_finder, partic_sql)

    row = cursor.fetchone()

    if row is not None:
        print("You have solved the problem")
    else:
        print("Sorry, that is not the right answer. Please try again")


def input_problem():
    id = input("Enter the id of the problem: ")
    id = float(id)
    problem_name = input("Enter the name of the problem: ")
    category = input("Enter the category of the problem: ")
    problem_description = input("Enter the problem's description: ")
    solution = input("Enter the solution to the problem: ")

    problem_input = "INSERT INTO HACKATHON (id, problem_name, category, problem_description, solution) VALUE (%s, %s, %s, %s, %s)"
    input_sql = (id, problem_name, category, problem_description, solution)

    cursor.execute(problem_input, input_sql)

    print("Done")



def developer_func():
    id = input("Enter the id of the problem: ")
    id = float(id)
    problem_name = input("Enter the name of the problem: ")
    category = input("Enter the category of the problem: ")
    problem_description = input("Enter the problem's description: ")
    solution = input("Enter the solution to the problem: ")

    problem_input = "INSERT INTO HACKATHON (id, problem_name, category, problem_description, solution) VALUE (%s, %s, %s, %s, %s)"
    input_sql = (id, problem_name, category, problem_description, solution)

    cursor.execute(problem_input, input_sql)

    print("Done")

while loop:

    loop = False
    user_authority = input("Enter your authority (1 for participant, 2 for developer): ")

    if user_authority == "1":
        participant_func()
    elif user_authority == "2":
        password = input("Enter your password: ")
        password_finder = "SELECT * FROM PASSWORDS WHERE passwords = %s"
        password_sql = (password, )
        cursor.execute(password_finder, password_sql)

        row = cursor.fetchone()

        if row is not None:
            developer_func()
        else:
            print("No users were found with that password")
    else:
        loop = True
        print("Please choose either 1 or 2")


