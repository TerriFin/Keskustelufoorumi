from flask import Flask, render_template
app = Flask(__name__)

class Item:
    def __init__(self, name = "Noppa"):
        self.name = name

nimi = "Sami Saukkonen"

lista = [1, 1, 2, 3, 4, 2, 1, 4, 3, 2, 3, 7, 8, 12312321, 4, 2]

esineet = []
esineet.append(Item())
esineet.append(Item("Sänky"))
esineet.append(Item("Kissa"))
esineet.append(Item("Tietokone"))
esineet.append(Item())

@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/demo')
def content():
    return render_template("demo.html", nimi=nimi, lista = lista, esineet = esineet)

if __name__ == "__main__":
    app.run(debug=True)