from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html', title="Flask", mensaje="Bienvenido a mi sitio web")

@app.route('/servicios')
def servicios():
    return render_template('servicios.html', title="Servicios", mensaje="Estos son los servicios que ofrecemos")

@app.route('/contacto')
def contacto():
    return render_template('contacto.html', title="Contacto", mensaje="Contáctanos para más información.")

@app.route('/productos')
def productos():
    return render_template('productos.html', title="Productos", mensaje="Estos son los productos que ofrecemos.")

if __name__ == '__main__':
    app.run(debug=True, port=5050)