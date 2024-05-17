from flask import Flask, request, jsonify
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import arff

app = Flask(__name__)

# Cargar el archivo ARFF y convertirlo a DataFrame de pandas
def cargar_datos(fileName):
    with open(fileName, 'r') as f:
        data = arff.load(f)
    return pd.DataFrame(data['data'], columns=[attr[0] for attr in data['attributes']])

# Convertir variables categóricas en variables dummy
datos = cargar_datos('./datos.arff')
datos = pd.get_dummies(datos, columns=['genero', 'fiebre', 'tos', 'congestion_nasal', 'dificultad_respiratoria', 'dolor_garganta', 'malestar_general'])

# Obtener los nombres de características utilizados para entrenar el modelo
nombres_caracteristicas = datos.drop('diagnostico', axis=1).columns.tolist()

# Entrenar un modelo de clasificación
def entrenar_modelo(datos):
    X = datos.drop('diagnostico', axis=1)
    y = datos['diagnostico']
    model = DecisionTreeClassifier()
    model.fit(X, y)
    return model

# Entrenar el modelo
modelo = entrenar_modelo(datos)

# Hacer una predicción basada en los atributos ingresados por el usuario
def hacer_prediccion(modelo, atributos, nombres_caracteristicas):
    atributos_df = pd.DataFrame([atributos], columns=nombres_caracteristicas)
    return modelo.predict(atributos_df)

@app.route('/diagnostico', methods=['POST'])
def diagnostico():
    data = request.json
    edad = data['edad']
    genero = data['genero']
    fiebre_leve = data['fiebre_leve']
    fiebre_moderada = data.get('fiebre_moderada', 0)
    fiebre_alta = data.get('fiebre_alta', 0)
    tos_leve = data['tos_leve']
    tos_moderada = data.get('tos_moderada', 0)
    tos_severa = data.get('tos_severa', 0)
    congestion_nasal_no = data['congestion_nasal_no']
    congestion_nasal_si = 0 if congestion_nasal_no else 1
    dificultad_respiratoria_no = data['dificultad_respiratoria_no']
    dificultad_respiratoria_si = 0 if dificultad_respiratoria_no else 1
    dolor_garganta_no = data['dolor_garganta_no']
    dolor_garganta_si = 0 if dolor_garganta_no else 1
    malestar_general_no = data['malestar_general_no']
    malestar_general_si = 0 if malestar_general_no else 1
    genero_masculino = 0 if genero == 0 else 1
    genero_femenino = 1 if genero == 0 else 0

    atributos = [
        edad,
        genero_femenino,
        genero_masculino,
        fiebre_leve,
        fiebre_moderada,
        fiebre_alta,
        tos_leve,
        tos_moderada,
        tos_severa,
        congestion_nasal_no,
        congestion_nasal_si,
        dificultad_respiratoria_no,
        dificultad_respiratoria_si,
        dolor_garganta_no,
        dolor_garganta_si,
        malestar_general_no,
        malestar_general_si
        ]
    
    resultado = hacer_prediccion(modelo, atributos, nombres_caracteristicas)
    return jsonify({'diagnostico': resultado[0]})

if __name__ == '__main__':
    app.run(debug=True)
