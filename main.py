from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        nombre = str(request.form['nombre'])
        edad = int(request.form['edad'])
        cantidad_tarros = int(request.form['cantidad_tarros'])

        precio_por_tarro = 9000
        total_sin_descuento = cantidad_tarros * precio_por_tarro


        if 18 <= edad <= 30:
            descuento = 0.15
        elif edad > 30 :
            descuento = 0.25
        else:
            descuento = 0

        monto_descuento = total_sin_descuento * descuento
        total_con_descuento = total_sin_descuento - monto_descuento

        return render_template('ejercicio1.html',
                               nombre=nombre,
                               total_sin_descuento=total_sin_descuento,
                               monto_descuento=monto_descuento,
                               total_con_descuento=total_con_descuento
        )

    return render_template('ejercicio1.html')

USUARIOS = {
    "juan": "admin",
    "pepe": "user"
}

@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    mensaje = ""
    if request.method == 'POST':

        nombre = request.form['nombre']
        contrasena = request.form['contrasena']

        # Verificar credenciales
        if nombre in USUARIOS and USUARIOS[nombre] == contrasena:
            if nombre == "juan":
                mensaje = f"Bienvenido Administrador {nombre}"
            elif nombre == "pepe":
                mensaje = f"Bienvenido Usuario {nombre}"
        else:
            mensaje = "Usuario o contraseña incorrectos"

    return render_template('ejercicio2.html', mensaje=mensaje)

if __name__ == '__main__':
    app.run(debug=True)