# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 16:57:55 2016

@author: Administrator
"""

import pymysql

#from pymongo import MongoClient

#conn2 = MongoClient()
#db = conn2.test
#
#
#collection = db.Gnomes
#CollectionU = db["users"]

conn = pymysql.connect("localhost", "root", "password", "chrishardmandb")

cursor= conn.cursor()
cursor2= conn.cursor()

stringin = str(input("choose either give a product or order a rating or review ratings. "))
while True:
    if stringin == "review":
        stringin = input("choose either order, prod. ")
        if stringin == "order":
            sql = "SELECT * FROM chrishardmandb.orders"
            cursor.execute(sql)
            results = cursor.fetchall()
            
            for row in results:
                Orderid = row[0]
                sql2 = "SELECT Customer_FirstName, Customer_Surname FROM chrishardmandb.customer WHERE ID_Customer =" + str(row[5])           
                cursor2.execute(sql2)
                results2 = cursor2.fetchone()
                Custname = results2
                Orderrating= row [7]
                print ("orders, name, rating.")
                
                print (Orderid ," ",Custname, " ", Orderrating)
            break
        elif stringin =="prod":
            sql = "SELECT * FROM chrishardmandb.rating"
            cursor.execute(sql)
            results = cursor.fetchall()
            
            for row in results:
                sql2 = "SELECT Product_Name FROM chrishardmandb.product WHERE ID_Product =" + str(row[3])           
                cursor2.execute(sql2)
                results2 = cursor2.fetchone()
                Productname = results2
                Productrating= row [1]
                print (" Product, name, rating.")
                
                print (Productname, " ", Productrating)
            break
        else:
            stringin = input("choose either 'Order' or 'Products' to review. ")
    else:
        stringin = input("choose either 'prod' or 'order' ")
    
        if stringin == "prod":
            print ("list of all product to review below.")
            sql = "SELECT ID_Product, Product_name FROM chrishardmandb.product"
            cursor.execute(sql)
            results = cursor.fetchall()
            for row in results:
                ProductID = row[0]
                ProductName = row[3]
                print (ProductID, " ", ProductName)        
            
            ProductReview = input("select Product to review by name or ID number")
            ProductRate = input ("give a rating for the product out of 100.")                   
            sql = "INSERT INTO chrishardmandb.rating VALUES(" + ProductID + "," +ProductName+");"
            cursor.execute(sql)
            break
        else:
            break
        
        

#
#sql = "SELECT * FROM chrishardmandb.Customer"
#cursor.execute(sql)
#results = cursor.fetchall()
#
#for row in results:
#    Customerid = row[0]
#    Customername = row[1]
#    print ("Customer")
#    print (Customerid," ",Customername)
#    
#sql = "SELECT * FROM chrishardmandb.Orders"
#cursor.execute(sql)
#results = cursor.fetchall()
#
#for row in results:
#    Orderid = row[0]
#    Ordername = row[1]
#    print ("orders")
#    print (Orderid," ",Ordername)
#    
#
#sql = "SELECT * FROM chrishardmandb.Product"
#cursor.execute(sql)
#results = cursor.fetchall()
#
#for row in results:
#   Productid = row[0]
#   Productname = row[1]
#   print ("results")
#   print (Productid," ",Productname)

cursor.close()
cursor2.close()
conn.close()