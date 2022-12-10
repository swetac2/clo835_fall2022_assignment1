from flask import Flask, render_template, request
from pymysql import connections
import os
import random
import argparse
import socket


app = Flask(__name__)
image_url = " "
DBHOST = os.environ.get("DBHOST") or "localhost"
DBUSER = os.environ.get("DBUSER") or "root"
DBPWD = os.environ.get("DBPWD") or "password"
DATABASE = os.environ.get("DATABASE") or "employees"
COLOR_FROM_ENV = os.environ.get('APP_COLOR') or "lime"
DBPORT = int(os.environ.get("DBPORT"))
My_name = os.environ.get('MYNAME')
if os.path.exists('/clo835/config/image_url'):
 My_file = open("/clo835/config/image_url", "r")
 image_url = My_file.read()
 print("Background image url is ",image_url)

# Create a connection to the MySQL database
db_conn = connections.Connection(
    host= DBHOST,
    port=DBPORT,
    user= DBUSER,
    password= DBPWD, 
    db= DATABASE
    
)
output = {}
table = 'employee';

# Define the supported color codes
color_codes = {
    "red": "#e74c3c",
    "green": "#16a085",
    "blue": "#89CFF0",
    "blue2": "#30336b",
    "pink": "#f4c2c2",
    "darkblue": "#130f40",
    "lime": "#C1FF9C",
}

# Generate a random color
COLOR = random.choice(["red", "green", "blue", "blue2", "darkblue", "pink", "lime"])

    
@app.route("/", methods=['GET','POST'])
def main():
   return render_template('addemp.html', debug="Environment Variables: DB_Host=" + (os.environ.get('DB_Host') or "Not Set") + "; DB_Database=" + (os.environ.get('DB_Database')  or "Not Set") + "; DB_User=" + (os.environ.get('DB_User')  or "Not Set") + "; DB_Password=" + (os.environ.get('DB_Password')  or "Not Set") )
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=81)
