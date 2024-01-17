# Importação
from flask import Flask

app = Flask(__name__)

# Definir uma rota raiz (página inicial) e a função que será executada ao requisitar
@app.route('/teste')
def hello_world():
    return 'Hello World'

if __name__ == "__main__":
    app.run(debug=True)