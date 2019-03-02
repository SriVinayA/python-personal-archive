#!/usr/bin/env python
# -*- coding: utf-8 -*-
# the above line is to avoid 'SyntaxError: Non-UTF-8 code starting with' error


# !/usr/bin/python
import base64
import sys
import codecs
import MySQLdb

db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="test",          # your username
                     passwd="test",           # your password
                     db="test")           # name of the data base

# you must create a Cursor object. It will let
#  you execute all the queries you need
cur = db.cursor()

# Use all the SQL you like
cur.execute("SELECT * FROM employee")

# print all the first cell of all the rows
counter = 0;
for row in cur.fetchall():
    try:
        counter = counter + 1
        name = str(row[2])      
        print(str(counter) + " - " +  name);
    except ValueError as e:
        print('Error');

db.close()