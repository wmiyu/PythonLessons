#!/bin/python3
# ************************************************************************** */
#
#                                                        :::      ::::::::  
#   less30_SQL.py                                         :+:      :+:    :+:   
#                                                    +:+ +:+         +:+    
#   By: wmiyu <wmiyu@student.21-school.ru>         +#+  +:+       +#+   
#                                                +#+#+#+#+#+   +#+        
#   Created: 17.02.2023 A.D.                          #+#    #+#       
#                                                    #+#   #+#+#+#+#  
#   Description:
# ************************************************************************** */

import pypyodbc
import sys

mySQLServer = "localhost"
myDatabase = "postgres"
myUser = "postgres"
myPass = "pgpwd4habr"
connectionStr = (
    'DRIVER={psqlOBDC};' +
    'Server=127.0.0.1;' +
    'Port=5432;' +
    'Database=postgres;' +
    'Uid=postgres;' +
    'Pwd=pgpwd4habr;')

print(connectionStr)

try:
    connection = pypyodbc.win_create_mdb("birds_wiki.mdb")
    #connection = pyodbc.connect(connectString=connectionStr)
except Exception:
    print(sys.exc_info()[1])
    sys.exit(1)

cursor = connection.cursor()

myCreateQuery = ("""
CREATE TABLE birds (id SERIAL PRIMARY KEY, bird VARCHAR(256), description VARCHAR(1024));
""")

mySQLQuery = ("""
                SELECT id, bird
                FROM birds
                """)

cursor.execute(myCreateQuery)

results = cursor.fetchall()
print(results)
connection.close()
