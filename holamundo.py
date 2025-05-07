#importamos la clas Flask desde el modulo flask
from  flask import Flask
#creamos una instancia de la aplicacion flask:
app = Flask(__name__)
# DEfinimos  una ruta ('/')que responde con  el mensaje "!hola mundo¡"
@app.route('/')
def hello_world():
    return 'hola mundo clase programacion leng 3 '
#verificamos si  el script se esta ejecutando directamente
if __name__ == '__main__':
    #ejecutamos la aplicasion en modo depuracion para facilitar el  desarrollo 
    app.run(debug=True)