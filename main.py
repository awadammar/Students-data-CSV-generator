"""
Author: Ammar Yasser
Date: 2/12/2018
Version: 1.0
Description: python script that takes inputs ( name, email, mobile, university, major )
             from user and save it in a python dictionary then generate a csv file with this data
"""
import csv

# flag to detect if the user finished or not
flag = True

# create 'students.csv' and starting write on it
with open('students.csv', 'w', newline='') as csvfile:
    fieldnames = ['name', 'email', 'mobile', 'university', 'major']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

# write csvfile headers
    writer.writeheader()

    while flag:
        name= input("Name :")
        email= input("E-mail: ")
        mobile= str(input("Mobile :"))
        university= input("University: ")
        major = input("Major: ")

# store every student info in a dictionary
        information = {
            'name': name,
            'email':email,
            'mobile':mobile,
            'university':university,
            'major':major,
        }

# write row in our csvfile
        writer.writerow({'name': name, 'email':email, 'mobile':mobile, 'university':university, 'major':major})

# check if the user has finished
        if(input()=="STOP"):
            flag = False
