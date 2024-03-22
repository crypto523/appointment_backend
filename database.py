import mysql.connector
import bcrypt

def openConnection():
    try:
        # Connect to MySQL database
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="appoinment"
        )
        if connection.is_connected():
            print("Connected to MySQL database")
            return connection
    except mysql.connector.Error as error:
        print("Error connecting to MySQL database:", error)
        return connection

def closeConnection(connection):
    # Close connection
    if connection.is_connected():
        connection.close()
        print("MySQL connection closed")


# Get random appointment
def getRandAppointment(connection):
    # Create cursor object to execute SQL queries
    cursor = connection.cursor()

    # Define the SELECT query
    query = "SELECT * FROM appoinments ORDER BY RAND() LIMIT 1"

    # Execute the SELECT query
    cursor.execute(query)

    # Fetch the result
    result = cursor.fetchone()
    
    cursor.close()
    if result:
        print("Record found:")
        print(result)
        # Convert result to dictionary object
        result_dict = {
            "id": result[0],
            "firstname": result[1],
            "surname": result[2],
            "email": result[3],
            "telephone": result[4],
            "representation": result[5],
        }
        return result_dict
    else:
        print(f"No record found")
        return None

# def hash_password(password):
#     hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
#     return hashed_password.decode('utf-8')

def create(connection, email, password):
    cursor = connection.cursor()
    # check existing email
    sql1 = "SELECT * FROM credentials WHERE email = %s"
    cursor.execute(sql1, (email,))
    result = cursor.fetchone()
    if(bool(result)):
        return False
    
    # Insert data into the credentials table
    sql2 = "INSERT INTO credentials (email, password) VALUES (%s, %s)"
    values = (email, password)
    cursor.execute(sql2, values)

    # Commit the transaction
    connection.commit()
    print("Data inserted successfully!")
    cursor.close()
    return True

def getEmails(connection):
    cursor = connection.cursor()

    # Execute SQL query to select emails from the credentials table
    sql = "SELECT email FROM credentials"
    cursor.execute(sql)

    # Fetch all rows of the result
    emails = cursor.fetchall()

    # Extract emails from the result
    email_list = [email[0] for email in emails]

    return email_list

def getPassword(connection, email):
    cursor = connection.cursor()
    sql1 = "SELECT password FROM credentials WHERE email = %s"
    cursor.execute(sql1, (email,))
    result = cursor.fetchone()
    return result[0]


