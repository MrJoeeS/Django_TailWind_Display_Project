import sqlite3 as lite
from django import template
from requests import request

"""
This scripts creat templates that can be used in HTML 
"""
register = template.Library()  

#Connecting to the DB
conn = lite.connect('mock_data.sqlite3')
cur = conn.cursor()

#Gets all data from the table users
cur.execute("SELECT * FROM users")
rows = cur.fetchall()

#Querying specific data from the table users
my_data = ('Male')
q ="SELECT gender FROM users WHERE gender=?"
answer = cur.execute(q,(my_data,))
male_data = answer.fetchall()

#Querying specific data from the table users
my_data = ('Female')
q ="SELECT gender FROM users WHERE gender=?"
answer = cur.execute(q,(my_data,))
female_data = answer.fetchall()


#Querying data from table dis
q ="SELECT number FROM dis"
answer = cur.execute(q)
datas = answer.fetchall()

@register.simple_tag
def dis_data():
    return datas

@register.simple_tag
def my_tag():
    return "hi"

@register.simple_tag
def total_users():
    return str(len(rows)-1)

@register.simple_tag
def total_male_users():
    return (str(len(male_data)))

@register.simple_tag
def total_female_users():
    return (str(len(female_data)))

@register.simple_tag
def total_other_users():
    return (str((len(rows)-1)-(len(male_data))-(len(female_data))))
