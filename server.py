from flask import Flask, app, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/home')
def home():
    return render_template('index.html', title="Flask", mensaje="Bienvenido a mi sitio web")

@app.route('/servicios')
def servicios():
    return render_template('servicios.html')

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

@app.route('/productos')
def productos():
    return render_template('productos.html')




if __name__ == '__main__':
    app.run(debug=True,port=5050)