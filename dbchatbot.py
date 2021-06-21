import chatbot
import pymysql
import bcrypt

db = pymysql.connect(host="localhost", user="Luit", password="supersafepassword123", database="chatbot")

cursor = db.cursor()

def createuser():
    global username
    username = input("create username: ")
    password = input("create password: ")

    salt = bcrypt.gensalt(rounds=16)
    hashed = bcrypt.hashpw(password.encode('utf8'), salt)

    cursor = db.cursor()
    cursor.execute("""SELECT * FROM user WHERE user_name=%s""",(username))
    if cursor.fetchone() == None:
        cursor = db.cursor()
        cursor.execute("""INSERT INTO user (user_name, hashed_pass) VALUES (%s,%s)""",(username,hashed))

        db.commit()
    else:
        print("This username already exists, please enter a new one.")
        createuser()

def login():
    global username
    username=input("username: ")
    passwd=input("password: ")

    cursor = db.cursor()
    cursor.execute("SELECT hashed_pass FROM user WHERE user_name=%s",(username))
    data = cursor.fetchone()[0]

    if bcrypt.checkpw(passwd.encode('utf8'),data.encode('utf8')):
        print("You are now logged in!")
        chatbot.main(username)
    else:
        print("password incorrect, please try again.")
        login()
    
new = input("Is this the first time using this app? ")
if new == "yes":
    createuser()
    login()

elif new == "no":
    login()