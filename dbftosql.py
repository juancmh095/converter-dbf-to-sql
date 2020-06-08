# -*- coding: utf-8 -*-

from dbfread import DBF
import mysql.connector
from mysql.connector import Error
from mysql.connector.connection import MySQLConnection
from mysql.connector import pooling
import json
from collections import OrderedDict
import dataset
import os
import re

""" db = dataset.connect('mysql://user:root@localhost/sys_data')
table2 = db['people'] """
connection = mysql.connector.connect(host="",port="",user="",passwd="",database="", autocommit = True)
cur = connection.cursor()
idx = 0

""" cambiar año siempre """
año = '2018'

""" ruta del directorio """
dirVar = './'
files = os.listdir(dirVar)
cont = 0

""" regex para separar numeros del nombre """

regex = r"[1,2,3,4,5,6]"

subst = ""

print('NUMERO DE ARCHIVOS',len(files))

try:
	for file in files:

		print('#########################################################################')

		cont = cont + 1
		data = file.split('.')		

		""" regex """
		test_str = data[0]

		estado = re.sub(regex, subst, test_str, 0, re.MULTILINE)
		print('ESTADO: '+estado)

		if(data[1] == 'DBF'):
			print(cont,' ARCHIVOS DE ',len(files),file)
			table = DBF(file, char_decode_errors='ignore')
			for record in table:
				idx = idx + 1
				try:
					cur.execute("INSERT INTO table (`) VALUES ();",())
				except Exception as e:
					pass
		print(idx)
		print('#########################################################################')
except Exception as err:
	print(err)
finally:
	print(idx)
