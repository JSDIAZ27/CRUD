from flask import Flask, render_template, request, url_for

app =Flask(__name__)

usuarios = []






@app.route("/", methods=["GET", "POST"])
def crud():
    nombre = request.form.get("nombre")
    email = request.form.get("email")
    usuarios.append({"nombre del usuario":nombre, "correo": email })




    return render_template("registro.html", usuarios=usuarios)




if __name__=="__main__":
    app.run(debug=True)

    