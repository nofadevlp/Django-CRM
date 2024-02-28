#install mysql on computer
#http://dev.mysql.com/download/installer
# pip install mysql
# pip install mysql-connector
# pip install mysql-connector-python
# To Intialize the git,there are few commands to enter in command prompt or Git bash.
# Git Bash is best for github and preinitiazed with .ssh.
# For every new project if you want to intialize git,these commands are must used in the path where you are saved your files.

# There are 5 Commands.They are:

# $ git config --global user.name "Your Name" //here change to your name.
# $ git config --global user.email "you@youraddress.com" //here change to your email
# $ git config --global push.default matching
# $ git config --global alias.co checkout 
# $ git init

# When commands are done,there will be file '.git' have in your Folder.
import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'password123'
)

# prepare a cursor object
cursorObject = dataBase.cursor()

# create a database

cursorObject.execute("CREATE DATABASE student")
print("All Done !")