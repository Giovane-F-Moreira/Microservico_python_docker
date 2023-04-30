from flask import Flask
from flask import jsonify

service = Flask(__name__)

# "constants"
IS_ALIVE = "yes"
VERSION = "0.0.2"
AUTHOR = "Giovane Fernandes Moreira"
EMAIL = "giovane.fern.m@gmail.com"

# bd estatic (while test)
CIRCUIT_INF = [
    {
      "_id": 1,
      "countryImg": "https://images.uncyc.org/pt/thumb/d/d9/Bandeira_de_Portugal.png/300px-Bandeira_de_Portugal.png",
      "local": "GP de Portugal",
      "circuit": "Circuito de Portimão",
      "date": "26",
      "month": "MAR",
      "details": {
          "circuitImg": "https://www.grandepremio.com.br/wp-content/uploads/2020/06/portimao.png",
          "route": "4.6km",
          "curves": "15(7 Direita, 8 Esquerda)"
      },
    },
    {
      "_id": 2,
      "countryImg": "https://imagepng.org/wp-content/uploads/2017/10/bandeira-argentina.png",
      "local": "GP da Argentina",
      "circuit": "Circuito Termas de Río Hondo",
      "date": "02",
      "month": "ABR",
      "details": {
          "circuitImg": "hhttps://bxrepsol.s3.eu-west-1.amazonaws.com/static/2022/08/29050951/Termas2-1024x590-1.png",
          "route": "4.8km",
          "curves": "14(8 Direita, 6 Esquerda)"
      },
    }
]

CLIMATE_INFO = [
    {
        "_id_climate": 1,
        "temperature": "27° C",
        "airHumidity": "34%",
        "wind": "12.2 m/s"
    },
    {
        "_id_climate": 2,
        "temperature": "27° C",
        "airHumidity": "15%",
        "wind": "7.6 m/s"
    }
]

TIME_INFO = [
    {
        "_id_time": 1,
        "event": {
            "tl1": {
                "day": "Sexta-Feira",
                "date": "31/03/2023",
                "time": "10:45"
            },
            "tc": {
                "day": "Sábado",
                "date": "01/04/2023",
                "time": "10:50"
            },
            "tl2": {
                "day": "Sexta-Feira",
                "date": "31/03/2023",
                "time": "15:00"
            },
            "sprint": {
                "day": "Sábado",
                "date": "01/04/2023",
                "time": "15:00"
            },
            "gp": {
                "day": "Domingo",
                "date": "02/04/2023",
                "time": "14:00"
            }   
        } 
    },
    {
        "_id_time": 2,
        "event": {
            "tl1": {
                "day": "Sexta-Feira",
                "date": "31/03/2023",
                "time": "10:45"
            },
            "tc": {
                "day": "Sábado",
                "date": "01/04/2023",
                "time": "10:50"
            },
            "tl2": {
                "day": "Sexta-Feira",
                "date": "31/03/2023",
                "time": "15:00"
            },
            "sprint": {
                "day": "Sábado",
                "date": "01/04/2023",
                "time": "15:00"
            },
            "gp": {
                "day": "Domingo",
                "date": "02/04/2023",
                "time": "14:00"
            }   
        } 
    }
] 


#This route return infomation about the service 
@service.route("/isalive/")
def is_alive():
    return IS_ALIVE

# This route return infomation about the development
@service.route("/info/")
def get_info():
    info = jsonify(
        version = VERSION,
        author = AUTHOR,
        email = EMAIL
    )

    return info

# This route return infomation about circuit in moto GP 2023 event
@service.route("/circuit_info/")
def get_circuit_info():
    circuit = jsonify(
        CIRCUIT_INF
    )

    return circuit


# This route return infomation about climete in moto GP 2023 event
@service.route("/climate_info/")
def get_climate_info():
    climate = jsonify(
        CLIMATE_INFO
    ) 

    return climate

# This route return infomation about time and moto GP 2023 event
@service.route("/time_info/")
def get_time_info():
    time = jsonify(
        TIME_INFO
    ) 

    return time

if __name__ == "__main__":
    service.run(
        host = "127.0.0.1",
        debug=True
    )