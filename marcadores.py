import os
import csv
import json
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
UPLOAD_FOLDER = 'descargas'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def csv_to_json(csv_file_path):
    data = []
    with open(csv_file_path, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            data.append(row)
    return data

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        if file and file.filename.endswith('.csv'):
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(file_path)
            json_data = csv_to_json(file_path)
            json_filename = file.filename.replace('.csv', '.json')
            json_file_path = os.path.join(app.config['UPLOAD_FOLDER'], json_filename)
            with open(json_file_path, 'w') as json_file:
                json.dump(json_data, json_file, indent=4)
            return jsonify({"message": "File converted and saved as JSON."})

    return render_template('archivo.html')

@app.route("/generarjson")
def generarjson():
    with open("data1.csv", "r") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=";")
        data = []
        for row in csvreader:
            data.append({
                "DEPARTAMENTO": row[0],
                "LOCALIDAD": row[1],
                "BARRIO": row[2],
                "VIVIENDAS": row[3],
                "MOTRIZ": row[4],
                "LATITUD": row[5],
                "LONGITUD": row[6],
                "Fecha de Entrega": row[7]
            })

    return json.dumps(data)


# starting the app
if __name__ == "__main__":
    app.run(port=3000, debug=True)

