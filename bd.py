import pymysql

def obtener_conexion():
   return pymysql.connect(host='rmolina.mysql.pythonanywhere-services.com',user='rmolina',password='rawson2021',db='rmolina$tesis2020')
