from flask import Flask, render_template, request, url_for, redirect

app =Flask(__name__)

usuarios = []
id_contador=1 





@app.route("/", methods=["GET", "POST"])
def crud():
    global id_contador 

    if request.method=='POST':
     nombre = request.form.get("nombre")#guarda en una variable de python lo que el usurio entrega al form
     email = request.form.get("email")
     usuarios.append({"id":id_contador,"nombre_del_usuario":nombre, "correo": email }) #insertando un usuario 
     id_contador+=1
     return redirect(url_for("crud"))


    id_eliminar=request.args.get("borrar")#siempre quda como texto
    if id_eliminar: #si me entregan un id a eliminar 
        #TODO: eliminar el usuario con el id del parametro de las lista
        for item in usuarios:
            if str(item['id'])==id_eliminar:
                usuarios.remove(item)
                break
        return redirect(url_for("crud"))#llamar al nombre de la funcion  


    return render_template("registro.html", usuarios=usuarios)#lista que entregamos al html
    
 #Ruta de actualizacion de datos del usuario
@app.route("/update/<int:id>", methods=['GET', 'POST']) #Ruta con parametros
def update(id):

    estudiante_a_editar=''
    #TODO: identificar el diccionario del usuario con el id a entregar
    for diccionario in usuarios:
        if diccionario['id']==id:
            estudiante_a_editar=diccionario
            print("el estudiante a editar es: ", estudiante_a_editar)
            break

    if request.method=='POST':
        #TODO: actualiar el diccionario del estudiante con los datos del fomulario   
        estudiante_a_editar['nombre_del_usuario']=request.form.get('nombre')
        estudiante_a_editar['correo']=request.form.get('email')
        return redirect(url_for("crud"))
    
    #si despues de recorrrer toda la lista, no encontramos el id integrado 
    if estudiante_a_editar=='':
        return f"no existe el usuario con id: {id}"#salgo de la funcion

    return render_template("editar.html",estudiante_a_editar=estudiante_a_editar)







if __name__=="__main__":
    app.run(debug=True)

    