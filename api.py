import mysql.connector
import requests
import urllib.parse
import json

#from flask import Flask, jsonify, request



host = "sergio-1.chvt2nz4puya.us-east-1.rds.amazonaws.com"
usuario = "admin"
senha = 'xande1972'
porta = 3306
banco = 'chinook'

conn =  mysql.connector.connect(host = host, user =usuario, passwd = senha, port = porta, database = banco)
cursor = conn.cursor()
cursor.execute("DELETE FROM artists WHERE ArtistId = 555;")

records = cursor.fetchall()


conn.commit ()
conn.close      # print(f"Registro {cursor.lastrowid} inserido.")
   # return "OK"
#dados_format = json.dumps(records, indent=4)

#print(cursor.description)
#print(dados_format)

#print (records)
'''
for r in records:
    print(f"ARTISTAS {cursor.description[0][0]} : {r[0]}, {cursor.description[1][0]} : {r[1]}, {cursor.description[2][0]} : {r[2]}, {cursor.description[3][0]} : {r[3]}")
row_headers = [x[0] for x in cursor.description]
print (f"ROW {row_headers}")
print (f"RECORDS {records[0]}")
print(f"TUPLA ÚNICA {tuple(row_headers)}")
print(f"TUPLA RECORDS {dict(zip(tuple(row_headers), records[0]))}")

result = [dict(zip(tuple(row_headers),i)) for  i in records]
print(f"RESULADO {result}")

#jret = jsonnify(result)'''

    