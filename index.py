import datetime as dt
import pandas as pd
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify, session
from bd import obtener_conexion
# from hashlib import md5
import hashlib
import random

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

@app.route('/alertas', methods=['GET','POST'])
def alertas():
    id_alerta = request.form['id_alerta']
    return render_template('alertas.html', id_alerta=id_alerta)

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
    # print ('MD5 antes del cifrado:' + str)
    # print ('MD5 después del cifrado es:' + password)
    # Output message if something goes wrong...
    msge = ' '
    # Check if "username" and "password" POST requests exist (user submitted form)
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        # Create variables for easy access
        username = request.form['username']
        # password = hashlib.md5(request.form['password'])
        # print(username)
        # print(password)
        # Check if account exists using MySQL
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            # cursor.execute('SELECT * FROM usuario WHERE nombre = %s AND clave = %s', (username, password,))
            cursor.execute(
                'SELECT * FROM usuario WHERE usuario = %s AND clave = %s', (username, password,))
        data = cursor.fetchall()
        res = jsonify(data)
        if len(data) == 1:
            for datos in data:
                # Create session data, we can access this data in other routes
                session['loggedin'] = True
                session['id'] = datos[0]
                session['username'] = datos[1]
                # Redirect to home page
                # msge = 'Logged in successfully!'
                print("si")
                flash('es correcto')
                return render_template('principal.html')
        else:
            # Account doesnt exist or username/password incorrect
            msge = 'Datos Incorrectos!!'
        cursor.close()
    # Show the login form with message (if any)
    return render_template('login.html', msge=msge)

# mis consultas las llamo por ajax 23-3-2020

@app.route('/ubicacion')
def ubicacion():
    return render_template('ubicacion.html')

@app.route('/buscar_ubicacion', methods=['GET', 'POST'])
def buscar_ubicacion():
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute(
            'SELECT `latitud`,`longitud`,`nombre`,`domicilio`,`departamento` FROM `ubicacion`')
        data = cursor.fetchall()
    res = jsonify(data)
    cursor.close()
    return res

# 07/09/2023 traer todas las lecturas --------------------------------------------------------------------------

@app.route('/buscar_lectura', methods=['GET', 'POST'])
def buscar_lectura():
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        # cursor.execute('SELECT `id`,`ubicacion_id`,`fecha_hora`,`sensor_1`,`sensor_8`,`sensor_5`,`sensor_4` FROM `lectura`')
        cursor.execute('SELECT lectura.`id` ,lectura.`ubicacion_id`,lectura.`fecha_hora`,lectura.`sensor_1`,lectura.`sensor_8`,lectura.`sensor_5`,lectura.`sensor_4`,ubicacion.`nombre` FROM lectura INNER JOIN ubicacion ON (lectura.`ubicacion_id` = ubicacion.`id`) order by lectura.`fecha_hora` desc')
    datos = cursor.fetchall()
    json = []
    item = []
    for data in datos:
        id = data[0]
        ubicacion_id = data[1]
        fecha_hora = data[2].strftime("%d-%m-%Y %H:%M:%S")
        sensor_1_fuego = data[3]
        sensor_8_temperatura = data[4]
        sensor_5_movimiento = data[5]
        sensor_4_humedad = data[6]
        nombre_ubicacion = data[7]
        item = {'id': id, 'ubicacion': ubicacion_id,'fecha_hora': fecha_hora, 'sensor_1_fuego': sensor_1_fuego,'sensor_8_temperatura':sensor_8_temperatura,
            'sensor_5_movimiento':sensor_5_movimiento, 'sensor_4_humedad':sensor_4_humedad , 'nombre_ubicacion':nombre_ubicacion}
        json.append(item)    
    
    cursor.close()
    return jsonify(json)

# 12/09/2023 traer una lectura --------------------------------------------------------------------------

@app.route('/buscar_lectura_alerta', methods=['GET', 'POST'])
def buscar_lectura_alerta():
    id_alerta = request.form['id_alerta']
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        # cursor.execute('SELECT `id`,`ubicacion_id`,`fecha_hora`,`sensor_1`,`sensor_8`,`sensor_5`,`sensor_4` FROM `lectura`')
        cursor.execute('SELECT lectura.`id` ,lectura.`ubicacion_id` ,lectura.`fecha_hora`,lectura.`sensor_1`,lectura.`sensor_8`,lectura.`sensor_5`,lectura.`sensor_4`,ubicacion.`nombre`,ubicacion.`latitud`,ubicacion.`longitud` FROM lectura INNER JOIN ubicacion ON (lectura.`ubicacion_id` = ubicacion.`id`)WHERE lectura.`id`=%s', (id_alerta))
    datos = cursor.fetchall()
    res = jsonify(datos)
    cursor.close()
    return res

# 30/08/2023 se agrega el sql para traer una sola lectura ------------------------------------------------------------
# SELECT * FROM lectura WHERE id= (SELECT MAX(id) FROM lectura)
@app.route('/buscar_alerta', methods=['GET', 'POST'])
def buscar_alerta():
    # SELECCION
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        # cursor.execute('SELECT `id`,`ubicacion_id`,`fecha_hora`,`sensor_1`,`sensor_8`,`sensor_5`,`sensor_4` FROM `lectura` ')
        # anterior      cursor.execute('SELECT lectura.`id`, lectura.`ubicacion_id`,lectura.`fecha_hora`, lectura.`sensor_1`, lectura.`sensor_8`, lectura.`sensor_5`, lectura.`sensor_4`, ubicacion.`nombre` FROM `lectura` INNER JOIN `ubicacion` ON (`lectura`.`ubicacion_id` = `ubicacion`.`id`)order by lectura.`fecha_hora` desc')
        # trae el maximo i
        cursor.execute('SELECT lectura.`id`, lectura.`ubicacion_id`,lectura.`fecha_hora`, lectura.`sensor_1`, lectura.`sensor_8`, lectura.`sensor_5`, lectura.`sensor_4`, ubicacion.`nombre` FROM lectura INNER JOIN ubicacion ON (`lectura`.`ubicacion_id` = `ubicacion`.`id`) WHERE `lectura`.`id`= (SELECT MAX(`id`) FROM lectura)')
        # tod los reg cursor.execute('SELECT lectura.`id`, lectura.`ubicacion_id`,lectura.`fecha_hora`, lectura.`sensor_1`, lectura.`sensor_8`, lectura.`sensor_5`, lectura.`sensor_4`, ubicacion.`nombre` FROM `lectura` INNER JOIN `ubicacion` ON (`lectura`.`ubicacion_id` = `ubicacion`.`id`) order by lectura.`fecha_hora` desc')
        datos = cursor.fetchall()
    # 19-01-2021 recorrer los datos y verlos en consola
    # http://copitosystem.com/es/python-mysql-database/
    # for row in data:
     #   idi = row[0]
      #  ubicacion_id = row[1]
       # fecha_hora = row[2]
        # sensor_1 = row[3]
        # sensor_8 = row[4]
        # sensor_5 = row[5]
        # sensor_4 = row[6]
        # imprimir los resultados
        # print ("id = {0}, ubicacion_id = {1}, fecha_hora = {2},sensor_1 = {3}, sensor_8 = {4}, sensor_5 = {5} , sensor_4 = {6}".format(idi,ubicacion_id,fecha_hora,sensor_1,sensor_8,sensor_5,sensor_4))
        # sacar las alertas
        # if (sensor_1==valortrue):
        #   print ("alerta")
        #  cur=mysql.connection.cursor()
        # cur.execute("""UPDATE lectura SET leido = %s WHERE id = %s """, ( 'SSSSS' , idi ))
        # mysql.connection.commit()
        # return jsonify(ubicacion=ubicacion_id,sensor="Fuego",fechahora=fecha_hora,alerta="danger")
        # else:
        #   print ("normal")
        #  return jsonify(ubicacion=ubicacion_id,sensor="Fuego",fechahora=fecha_hora,alerta="info")
    valortrue = "1"
    json = []
    item = []
    for data in datos:
        idi = data[0]
        ubicacion_id = data[1]
        fecha_hora = data[2].strftime("%d %m %Y %H:%M:%S")
        sensor_1_fuego = data[3]
        sensor_8_temperatura = data[4]
        sensor_5_movimiento = data[5]
        sensor_4_humedad = data[6]
        nombre_ubicacion = data[7]

        print(data)

        # EVALUACION por prioridad 1 de fuego ,2 de temperatura , 3 de movimiento , 4 de humedad
        if (sensor_1_fuego == valortrue):
            print("alerta")
            item = {'id': idi, 'ubicacion': ubicacion_id, 'sensor': 'Fuego',
                    'fechahora': fecha_hora, 'alerta': 'danger', 'nombre_ubicacion': nombre_ubicacion}
            json.append(item)
        else:
            print("normal")
            item = {'id': idi, 'ubicacion': ubicacion_id, 'sensor': 'Fuego',
                    'fechahora': fecha_hora, 'alerta': 'success', 'nombre_ubicacion': nombre_ubicacion}
            json.append(item)
        # 2 de temperatura , 3 de movimiento , 4 de humedad
        if (sensor_8_temperatura >= 30):
            print("alerta")
            item = {'id': idi, 'ubicacion': ubicacion_id, 'sensor': 'Temperatura',
                    'fechahora': fecha_hora, 'alerta': 'warning', 'nombre_ubicacion': nombre_ubicacion}
            json.append(item)
        else:
            print("normal")
            item = {'id': idi, 'ubicacion': ubicacion_id, 'sensor': 'Temperatura',
                    'fechahora': fecha_hora, 'alerta': 'success', 'nombre_ubicacion': nombre_ubicacion}
            json.append(item)

        # 3 de movimiento ,Sensor Detector Movimiento Infrarrojo Sr501 - 5
        if (sensor_5_movimiento == valortrue):
            print("alerta")
            item = {'id': idi, 'ubicacion': ubicacion_id, 'sensor': 'Movimiento',
                    'fechahora': fecha_hora, 'alerta': 'warning', 'nombre_ubicacion': nombre_ubicacion}
            json.append(item)
        else:
            print("normal")
            item = {'id': idi, 'ubicacion': ubicacion_id, 'sensor': 'Movimiento',
                    'fechahora': fecha_hora, 'alerta': 'success', 'nombre_ubicacion': nombre_ubicacion}
            json.append(item)

        
        # 4 de humedad, Sensor De Humedad Y Temperatura Dht22 - 4
        if (sensor_4_humedad >= 90):
            print("alerta")
            item = {'id': idi, 'ubicacion': ubicacion_id, 'sensor': 'Humedad',
                    'fechahora': fecha_hora, 'alerta': 'warning', 'nombre_ubicacion': nombre_ubicacion}
            json.append(item)
        else:
            print("normal")
            item = {'id': idi, 'ubicacion': ubicacion_id, 'sensor': 'Humedad',
                    'fechahora': fecha_hora, 'alerta': 'success', 'nombre_ubicacion': nombre_ubicacion}
            json.append(item)


            

        # fin de la evaluacion ----------------------------
    cursor.close()
    return jsonify(json)

# 13/09/2023 buscar todas las alertas
@app.route('/buscar_todas_alerta', methods=['GET', 'POST'])
def buscar_todas_alerta():
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        # cursor.execute('SELECT `id`,`ubicacion_id`,`fecha_hora`,`sensor_1`,`sensor_8`,`sensor_5`,`sensor_4` FROM `lectura` ')
        cursor.execute('SELECT lectura.`id`, lectura.`ubicacion_id`,lectura.`fecha_hora`, lectura.`sensor_1`, lectura.`sensor_8`, lectura.`sensor_5`, lectura.`sensor_4`, ubicacion.`nombre` FROM `lectura` INNER JOIN `ubicacion` ON (`lectura`.`ubicacion_id` = `ubicacion`.`id`)order by lectura.`fecha_hora` asc')
        # trae el maximo i
        #cursor.execute('SELECT lectura.`id`, lectura.`ubicacion_id`,lectura.`fecha_hora`, lectura.`sensor_1`, lectura.`sensor_8`, lectura.`sensor_5`, lectura.`sensor_4`, ubicacion.`nombre` FROM lectura INNER JOIN ubicacion ON (`lectura`.`ubicacion_id` = `ubicacion`.`id`) WHERE `lectura`.`id`= (SELECT MAX(`id`) FROM lectura)')
        # tod los reg cursor.execute('SELECT lectura.`id`, lectura.`ubicacion_id`,lectura.`fecha_hora`, lectura.`sensor_1`, lectura.`sensor_8`, lectura.`sensor_5`, lectura.`sensor_4`, ubicacion.`nombre` FROM `lectura` INNER JOIN `ubicacion` ON (`lectura`.`ubicacion_id` = `ubicacion`.`id`) order by lectura.`fecha_hora` desc')
        datos = cursor.fetchall()
    valortrue = "1"
    json = []
    item = []
    for data in datos:
        idi = data[0]
        ubicacion_id = data[1]
        fecha_hora = data[2].strftime("%d %m %Y %H:%M:%S")
        sensor_1_fuego = data[3]
        sensor_8_temperatura = data[4]
        sensor_5 = data[5]
        sensor_4 = data[6]
        nombre_ubicacion = data[7]

        # EVALUACION por prioridad 1 de fuego ,2 de temperatura , 3 de movimiento , 4 de humedad
        if (sensor_1_fuego == valortrue):
            print("alerta")
            item = {'id': idi, 'ubicacion': ubicacion_id, 'sensor': 'Fuego',
                    'fechahora': fecha_hora, 'alerta': 'danger', 'nombre_ubicacion': nombre_ubicacion}
            json.append(item)
        else:
            print("normal")
            item = {'id': idi, 'ubicacion': ubicacion_id, 'sensor': 'Fuego',
                    'fechahora': fecha_hora, 'alerta': 'success', 'nombre_ubicacion': nombre_ubicacion}
            json.append(item)

        if (sensor_8_temperatura >= 30):
            print("alerta")
            item = {'id': idi, 'ubicacion': ubicacion_id, 'sensor': 'Temperatura',
                    'fechahora': fecha_hora, 'alerta': 'warning', 'nombre_ubicacion': nombre_ubicacion}
            json.append(item)
        else:
            print("normal")
            item = {'id': idi, 'ubicacion': ubicacion_id, 'sensor': 'Temperatura',
                    'fechahora': fecha_hora, 'alerta': 'success', 'nombre_ubicacion': nombre_ubicacion}
            json.append(item)
        # fin de la evaluacion ----------------------------
    cursor.close()
    return jsonify(json)


@app.route("/numeros")
def numeros():
    return render_template('numeros.html')

# Generate una lectura para la base de datos cada 30 segundos

@app.route("/numeros_aleatorios", methods=['GET', 'POST'])
def numeros_aleatorios():
    # Generate 10 random numbers
    # numbers = [random.randint(1, 100) for i in range(10)]
    # Return the numbers to the template
    # return numbers
    # Get the sensor name, value, date, location, and alert from the request
    # start = datetime.datetime.strptime("01-12-2021", "%d-%m-%Y")
    # date_generated = pd.date_range(start, periods=5)

    locations = ['peras', 'manzanas', 'plátanos', 'ciruelas']
    ubicacion = (random.choice(locations))

    sensor = random.randint(1, 100)  # request.args.get("sensor_name")
    value = request.args.get("value")
    date = request.args.get("date")
    # ubicacion = request.args.get("location")
    alert = 'warning'  # request.args.get("alert")
    fechahora = random.randint(5, 15)

    # Return a dictionary with the sensor data
    data = {
        "sensor": sensor,
        "value": value,
        "fechahora": fechahora,
        "ubicacion": ubicacion,
        "alert": alert
    }

    return jsonify(data)


# 27/08/2023 Generar un diccionario con los datos aleatorios de los sensores

@app.route('/generar_datos', methods=['GET', 'POST'])
def generar_datos():
    # ubicacion entre uno y tres
    ubicacion = random.randint(1, 3)

    # fechahora actual
    fechahora = dt.datetime.now()

    # sensor1
    sensor1 = random.randint(0, 1)  # random.choice(["True", "False"])

    # sensor8
    sensor8 = random.randint(20, 60)

    # sensor5
    sensor5 = random.randint(0, 1)  # random.choice(["True", "False"])

    # sensor4
    sensor4 = random.randint(20, 100)

    datos = {
        'ubicacion': ubicacion,
        'fechahora': fechahora,
        'sensor1': sensor1,
        'sensor8': sensor8,
        'sensor5': sensor5,
        'sensor4': sensor4
    }
    # return jsonify(datos)
    _ubicacion_id = ubicacion
    _fecha_hora = fechahora
    _sensor_1 = sensor1
    _sensor_8 = sensor8
    _sensor_5 = sensor5
    _sensor_4 = sensor4
    try:
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            query = "INSERT INTO `lectura` (`ubicacion_id`, `fecha_hora`, `sensor_1`, `sensor_8`, `sensor_5`, `sensor_4`) VALUES (%s, %s, %s, %s, %s, %s)"
            cursor.execute(query, (_ubicacion_id, _fecha_hora,
                           _sensor_1, _sensor_8, _sensor_5, _sensor_4))
            conexion.commit()
            print("1 registro insertado, ID", cursor.lastrowid)
    except Exception as e:
        print("Error:", e)
        return "Error al insertar la lectura."

    conexion.close()
    return "Lectura insertada correctamente en la base de datos."

# 27/08/2023 insertar datos generados automaticamente


@app.route('/insertar_lectura', methods=['GET', 'POST'])
def insertar_lectura():
    _ubicacion_id = 1
    _fecha_hora = '2023-05-27 12:00:00'
    _sensor_1 = 1
    _sensor_8 = 1
    _sensor_5 = 1
    _sensor_4 = 1
    try:
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            query = "INSERT INTO `lectura` (`ubicacion_id`, `fecha_hora`, `sensor_1`, `sensor_8`, `sensor_5`, `sensor_4`) VALUES (%s, %s, %s, %s, %s, %s)"
            cursor.execute(query, (_ubicacion_id, _fecha_hora,
                           _sensor_1, _sensor_8, _sensor_5, _sensor_4))
            conexion.commit()
            print("1 registro insertado, ID", cursor.lastrowid)
    except Exception as e:
        print("Error:", e)
        return "Error al insertar la lectura."

    conexion.close()
    return "Lectura insertada correctamente en la base de datos."

# 05092023 hacer una prueba de alertas


@app.route("/prueba05092023")
def prueba05092023():
    return render_template('prueba05092023.html')


prueba05092023


# starting the app
if __name__ == "__main__":
    app.run(port=3000, debug=True)
