from flask import Flask, render_template,request, redirect, url_for, flash, jsonify, session
from bd import obtener_conexion
#from hashlib import md5
import hashlib

# initializations
app = Flask(__name__)

app.secret_key = '2021demo'

# Mysql Connection

# routes

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/salir')
def salir(): 
   session.pop('id', None) 
   session.pop('username', None) 
   return render_template('login.html')    

@app.route('/plantilla')
def plantilla():
    return render_template('plantilla.html')

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')   

@app.route('/principal')
def principal():
    return render_template('principal.html') 

@app.route('/alertas')
def alertas():
    return render_template('alertas.html') 

@app.route('/lecturas')
def lecturas():
    return render_template('lecturas.html')     

@app.route('/sensores')
def sensores():
    return render_template('sensores.html')

@app.route('/usuarios')
def usuarios():
    return render_template('usuarios.html')

# login    
@app.route('/login', methods=['GET', 'POST'])
def login():

    # Información a encriptar
    str = request.form['password']
    # Crear objeto md5
    m = hashlib.md5()
    # Tips
    # Debe codificar aquí
    # Si la redacción es m.update (str), el error es: los objetos Unicode deben codificarse antes del hash
    # Porque el str predeterminado en python3 es unicode
    # O b = bytes (str, encoding = 'utf-8'), el efecto es el mismo, ambos codifican como bytes
    b = str.encode(encoding='utf-8')
    m.update(b)
    password = m.hexdigest()

    #print ('MD5 antes del cifrado:' + str)
    #print ('MD5 después del cifrado es:' + password)
  
    # Output message if something goes wrong...
    msge = ' '
    # Check if "username" and "password" POST requests exist (user submitted form)
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        # Create variables for easy access
        username = request.form['username']
        # password = hashlib.md5(request.form['password'])

        #print(username)
        #print(password)

        # Check if account exists using MySQL
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            #cursor.execute('SELECT * FROM usuario WHERE nombre = %s AND clave = %s', (username, password,))
            cursor.execute('SELECT * FROM usuario WHERE usuario = %s AND clave = %s', (username, password,))
        data = cursor.fetchall()
        print(data)
        print(len(data))

        res= jsonify(data)
        if len(data)==1:
            for datos in data:
                 # Create session data, we can access this data in other routes
                session['loggedin'] = True
                session['id'] = datos[0]
                session['username'] = datos[1]
                # Redirect to home page
                #msge = 'Logged in successfully!'
                print("si")
                flash('es correcto')
                return render_template('principal.html')
        else:
            # Account doesnt exist or username/password incorrect
            msge = 'Datos Incorrectos!!'
       
        cursor.close()
                  
    # Show the login form with message (if any)
    return render_template('login.html', msge = msge)

# mis consultas las llamo por ajax 23-3-2020

@app.route('/ubicacion')
def ubicacion():
    return render_template('ubicacion.html')    

@app.route('/buscar_ubicacion', methods=['GET', 'POST'])
def buscar_ubicacion():
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute('SELECT `latitud`,`longitud`,`nombre`,`domicilio`,`departamento` FROM `ubicacion`')
        data = cursor.fetchall()
    res= jsonify(data)
    cursor.close()
    return res 

@app.route('/buscar_lectura', methods=['GET', 'POST'])
def buscar_lectura():
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute('SELECT `id`,`ubicacion_id`,`fecha_hora`,`sensor_1`,`sensor_2`,`sensor_4`,`sensor_5`,`sensor_6` FROM `lectura`')
        data = cursor.fetchall()
    res= jsonify(data)
    cursor.close()
    return res     

@app.route('/alerta_lectura', methods=['GET', 'POST'])
def buscar_alerta():
    #cur = mysql.get_db().cursor()
    #cur=mysql.connect.cursor()
    # SELECCION
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        #cursor.execute('SELECT `id`,`ubicacion_id`,`fecha_hora`,`sensor_1`,`sensor_8`,`sensor_5`,`sensor_4` FROM `lectura` ')
        cursor.execute('SELECT lectura.`id`, lectura.`ubicacion_id`,lectura.`fecha_hora`, lectura.`sensor_1`, lectura.`sensor_8`, lectura.`sensor_5`, lectura.`sensor_4`, ubicacion.`nombre` FROM `lectura` INNER JOIN `ubicacion` ON (`lectura`.`ubicacion_id` = `ubicacion`.`id`)')
        datos = cursor.fetchall()

    # 19-01-2021 recorrer los datos y verlos en consola
    # http://copitosystem.com/es/python-mysql-database/
    
    #for row in data:
     #   idi = row[0]
      #  ubicacion_id = row[1]
       # fecha_hora = row[2]
        #sensor_1 = row[3]
        #sensor_8 = row[4]
        #sensor_5 = row[5]
        #sensor_4 = row[6]
        # imprimir los resultados
        #print ("id = {0}, ubicacion_id = {1}, fecha_hora = {2},sensor_1 = {3}, sensor_8 = {4}, sensor_5 = {5} , sensor_4 = {6}".format(idi,ubicacion_id,fecha_hora,sensor_1,sensor_8,sensor_5,sensor_4))
        # sacar las alertas
        #if (sensor_1==valortrue):
         #   print ("alerta")
          #  cur=mysql.connection.cursor()
           # cur.execute("""UPDATE lectura SET leido = %s WHERE id = %s """, ( 'SSSSS' , idi ))
            #mysql.connection.commit()
            #return jsonify(ubicacion=ubicacion_id,sensor="Fuego",fechahora=fecha_hora,alerta="danger")
        #else:
         #   print ("normal")
          #  return jsonify(ubicacion=ubicacion_id,sensor="Fuego",fechahora=fecha_hora,alerta="info")
    valortrue="True"
    json=[]
    item=[]
    for data in datos:
        idi = data[0]
        ubicacion_id = data[7]
        fecha_hora = data[2].strftime("%d %m %Y %H:%M:%S")
        sensor_1_fuego = data[3]
        sensor_8_temperatura = data[4]
        #sensor_5 = data[5]
        #sensor_4 = data[6]

        # EVALUACION por prioridad 1 de fuego ,2 de temperatura , 3 de movimiento , 4 de humedad
        if ( sensor_1_fuego == valortrue ) :
          print ("alerta")
          item={'id':idi, 'ubicacion':ubicacion_id,'sensor':'Fuego','fechahora':fecha_hora,'alerta':'danger'}
          json.append(item)
        else:
          print ("normal")

        if ( sensor_8_temperatura >= 30 ) :
          print ("alerta")
          item={'id':idi, 'ubicacion':ubicacion_id,'sensor':'Temperatura','fechahora':fecha_hora,'alerta':'warning'}
          json.append(item)
        else:
          print ("normal")  


        # fin de la evaluacion ----------------------------          
    cursor.close()
    return jsonify(json)     

# starting the app
if __name__ == "__main__":
    app.run(port=3000, debug=True)