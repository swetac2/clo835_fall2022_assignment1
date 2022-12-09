from flask import Flask, render_template, request
from pymysql import connections
import os
import random
import argparse


app = Flask(__name__)

DBHOST = os.environ.get("DBHOST") or "localhost"
DBUSER = os.environ.get("DBUSER") or "root"
DBPWD = os.environ.get("DBPWD") or "password"
DATABASE = os.environ.get("DATABASE") or "employees"
COLOR_FROM_ENV = os.environ.get('APP_COLOR') or "lime"
DBPORT = int(os.environ.get("DBPORT"))
IMAGE_URL_PATH = os.environ.get('IMAGE_URL_PATH')
IMAGE_URL_S3 = os.environ.get('IMAGE_URL_S3')

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
    
@app.route("/", methods=['GET','POST'])
def main():
    return render_template("addemp.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=81)
