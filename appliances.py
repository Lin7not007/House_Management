#import libraries 
import mysql.connector
import pandas as pd

#connect to MySQL
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="appliances"
)

#create cursor to perform operations
mycursor = mydb.cursor()

#create table
mycursor.execute("CREATE TABLE IF NOT EXISTS appliances (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), brand VARCHAR(255), model VARCHAR(255), serial_no VARCHAR(255), warranty_exp DATE, warranty_contact INT, last_service DATE, price INT, status VARCHAR(255))")

#function to add new appliance
def add_appliance(name, brand, model, serial_no, warranty_exp, warranty_contact, last_service, price, status):
    sql = "INSERT INTO appliances (name, serial_no, price, status) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    mycursor.execute(sql, (name, brand, model, serial_no, warranty_exp, warranty_contact, last_service, price, status))
    mydb.commit()

#function to update appliance info
def update_status(name, warranty_exp, warranty_contact, last_service, status):
    sql = "UPDATE appliances SET status = %s WHERE serial_no = %s"
    mycursor.execute(sql, (name, warranty_exp, warranty_contact, last_service, status))
    mydb.commit()

#function to delete appliance
def delete_appliance(name):
    sql = "DELETE FROM appliances WHERE serial_no = %s"
    mycursor.execute(sql, (name))
    mydb.commit()

#function to view all appliances
def view_appliances():
    mycursor.execute("SELECT * FROM appliances")
    result = mycursor.fetchall()
    df = pd.DataFrame(result, columns=['id','name','serial_no','price','status'])
    print(df)