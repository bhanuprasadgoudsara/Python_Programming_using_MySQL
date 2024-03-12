'''
1. Write a Python program to create a table called Student with the below columns:

SID - INT , PRIMARY KEY

SNAME - VARCHAR2(20)

COURSE - VARCHAR2(20)

MARKS - INT
'''
# importing mysql-connector module
import mysql.connector

# establishing a connection using connect method and assigning to connection object "conn"
conn = mysql.connector.connect( host = "local_host", user = "user_name", password = "password", database = "database_name")

# creating the cursor object "cur"
cur = conn.cursor()

# query execution
cur.execute(
    """
        CREATE TABLE IF NOT EXISTS Student
        (
            SID INT PRIMARY KEY,
            SNAME VARCHAR(20),
            COURSE VARCHAR(20),
            MARKS INT
        );
    """)

# cursor object has attribute "rowcount()" => no. of rows afftected during Query
print(curr.rowcount())

# closing the cursor object "cur"
cur.close()

# all DML statements are not auto-commited(lost once the connection is closed). invoked on connection object "conn"
conn.commit()

# closing the connection object "conn"
conn.close()

'''
2. Write a Python program to insert the following data into the Student table.
'''
import mysql.connector
conn = mysql.connector.connect( host = "local_host", user = "user_name", password = "password", database = "database_name")

try:
    cur = conn.cursor()
    cur.execute(
    """
        INSERT INTO Student VALUES
        (1,'Thomas','Python',82) ;
        
        INSERT INTO Student VALUES
        (2,'Kevin','Java',81) ;

        INSERT INTO Student VALUES
        (3,'Adam','Go',90) ;

        INSERT INTO Student VALUES
        (4,'John','Python',90) ;
    """)
    print(curr.rowcount())
    conn.commit()
except mysql.connector.NameError as e:
    print(e)
except mysql.connector.OperationalError as e:
    print(e)
except mysql.connector.ProgrammingError as e:
    print(e)
finally:
    cur.close()
    conn.close()
'''
3.  The marks entered for student 3 is wrong. The actual marks were 92.
    Write a python program to update the marks for student 3.
'''
import mysql.connector
conn = mysql.connector.connect( host = "local_host", user = "user_name", password = "password", database = "database_name")

try:
    cur = conn.cursor()
    cur.execute(
    """
        UPDATE Student
        SET MARKS = 92
        WHERE SID = 3;
    """)
    print(curr.rowcount())
    conn.commit()
except mysql.connector.NameError as e:
    print(e)
except mysql.connector.OperationalError as e:
    print(e)
except mysql.connector.ProgrammingError as e:
    print(e)
finally:
    cur.close()
    conn.close()

    
'''
4. Write a Python program to display all the records of Student table.
'''
import mysql.connector
conn = mysql.connector.connect( host = "local_host", user = "user_name", password = "password", database = "database_name")

try:
    cur = conn.cursor()
    cur.execute(
    """
        SELECT * FROM Student ;
    """)
    print(curr.rowcount())
    print(curr.fetchall())
    conn.commit()
except mysql.connector.NameError as e:
    print(e)
except mysql.connector.OperationalError as e:
    print(e)
except mysql.connector.ProgrammingError as e:
    print(e)
finally:
    cur.close()
    conn.close()

    
'''
5. Write a Python program to delete the student 4 record from Student table.
'''
import mysql.connector
conn = mysql.connector.connect( host = "local_host", user = "user_name", password = "password", database = "database_name")

try:
    cur = conn.cursor()
    cur.execute(
    """
        DELETE FROM Student
        WHERE SID = 4;
    """)
    print(curr.rowcount())
    conn.commit()
except mysql.connector.NameError as e:
    print(e)
except mysql.connector.OperationalError as e:
    print(e)
except mysql.connector.ProgrammingError as e:
    print(e)
finally:
    cur.close()
    conn.close()
'''
6. Write a Python program which displays the following menu and seeks the user input upon its execution.

Add a new student
Update an existing student detail
Remove a student
Display a student

Rules: 

If 1 is selected, take the student details from the standard input, and insert a new record
If 2 is selected, input the student ID, and the updated details. Update the corresponding record
If 3 is selected, input the student ID, and delete the corresponding record
If 4 is selected, input the student ID, and display the corresponding record
For any other input, display all the student records
Note: Display respective error messages wherever needed.
'''
import mysql.connector
conn = mysql.connector.connect( host = "local_host", user = "user_name", password = "password", database = "database_name")
print("MENU:\n1.Add a new student\n2.Update an existing student detail\n3.Remove a student\n4.Display a student")
inp = input("Please Enter the number to select an option:\n")
inp = int(inp)
try:
    cur = conn.cursor()
    if inp == 1:
        print("1.Adding a New Student:")
        sid = input("Enter Student ID: ")
        sname = input("Enter Student Name: ")
        course = input("Enter Course Name: ")
        marks = input("Enter Student Marks: ")
        cur.execute("INSERT INTO Student VALUES ( " + sid + ",'" + sname + "','" + course + "'," + marks + " ) ;")  
    elif inp == 2:
        print("2.Updating the Student details:")
        sid = input("Enter Student ID: ")
        sname = input("Enter Student Name: ")
        course = input("Enter Course Name: ")
        marks = input("Enter Student Marks: ")
        cur.execute("UPDATE Student SET SNAME = '" + sname + "', COURSE = '" + course + "',MARKS = " + marks + " WHERE SID = " + sid + " ;")  
    elif inp == 3:
        print("3.Deleting a Student:")
        sid = input("Enter Student ID: ")
        cur.execute("DELETE FROM Student WHERE SID = " + sid + " ;")
    elif inp == 4:
        print("4.Displaying a Student:")
        sid = input("Enter Student ID: ")
        cur.execute("SELECT * FROM Student WHERE SID = " + sid + " ;")
        print(cur.fetchone())
    else:
        print("Others:")
        cur.execute("SELECT * FROM Student ;")
        print(cur.fetchall())
    print(cur.rowcount())
    conn.commit()
except mysql.connector.NameError as e:
    print(e)
except mysql.connector.OperationalError as e:
    print(e)
except mysql.connector.ProgrammingError as e:
    print(e)
finally:
    cur.close()
    conn.close()


