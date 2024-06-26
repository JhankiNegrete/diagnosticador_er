# API de Diagnóstico de Enfermedades Respiratorias

Este proyecto proporciona una API RESTful para diagnosticar enfermedades respiratorias basadas en varios síntomas utilizando un clasificador de árbol de decisión. El modelo se entrena con un conjunto de datos almacenado en formato ARFF y predice el diagnóstico basado en los síntomas ingresados por el usuario.

## Características
- Cargar y preprocesar datos desde un archivo ARFF.
- Entrenar un clasificador de árbol de decisión.
- Proveer un endpoint de API para hacer predicciones basadas en los síntomas del usuario.

## Requisitos
- Python 3.6+
- Flask
- Pandas
- Scikit-learn
- Liac-arff
- flask-cors

## Instalación
1. Clona el repositorio:
   ```sh
   git clone https://github.com/JhankiNegrete/diagnosticador_er
   cd diagnosticador_er
   ```
2. Instala los paquetes requeridos:
   ```sh
   pip install -r requirements.txt
   ```

## Uso
1. Asegúrate de tener el archivo de datos `datos.arff` en el directorio del proyecto.
2. Ejecuta la aplicación Flask:
   ```sh
   python diagnosticador.py
   ```
3. El endpoint de la API estará disponible en `http://127.0.0.1:5000/diagnostico`.
4. puedes hacer consumo abriendo el index.html que se encuentra en el directorio del proyecto (abriendo o montando en el host con live server).

## Endpoint de la API

### POST /diagnostico
Haz una solicitud POST a este endpoint con un cuerpo JSON que contenga los síntomas para obtener un diagnóstico.

#### Cuerpo de la Solicitud
```json
{
  "edad": int,
  "genero": int,  # 0 para femenino, 1 para masculino
  "fiebre_leve": int,  # 0 o 1
  "fiebre_moderada": int,  # 0 o 1 (opcional)
  "fiebre_alta": int,  # 0 o 1 (opcional)
   # un solo valor de fiebre debe tener un (1)
  "tos_leve": int,  # 0 o 1
  "tos_moderada": int,  # 0 o 1 (opcional)
  "tos_severa": int,  # 0 o 1 (opcional)
   # un solo valor de tos debe tener un (1)
  "congestion_nasal_no": int,  # 0 o 1
  "dificultad_respiratoria_no": int,  # 0 o 1
  "dolor_garganta_no": int,  # 0 o 1
  "malestar_general_no": int  # 0 o 1
}
```

#### Respuesta
```json
{
  "diagnostico": "string"
}
```

## Ejemplo de Solicitud
```json
'{
  "edad": 30,
  "genero": 1,
  "fiebre_leve": 1,
  "fiebre_moderada": 0,
  "fiebre_alta": 0,
  "tos_leve": 1,
  "tos_moderada": 0,
  "tos_severa": 0,
  "congestion_nasal_no": 0,
  "dificultad_respiratoria_no": 1,
  "dolor_garganta_no": 1,
  "malestar_general_no": 1
}'
```

## Estructura del Proyecto
```
 diagnosticador_er/
├── diagnosticador.py             # Archivo principal de la aplicación
├── datos.arff                    # Archivo de datos
├── requirements.txt              # Paquetes de Python requeridos
├── collection_detector_er.json   #Coleccion de Postman para hacer pruebas a la API
└── README.md                     # Archivo README del proyecto

```

