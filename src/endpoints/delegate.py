from flask import Blueprint, request
delegate = Blueprint("delegate",
                    __name__,
                    url_prefix="/api/v1/delegate")

#Listar delegados
@delegate.get("/")
def read_all():
    return "Reading all delegate ... soon"

#Obtener información de un delegado
@delegate.get("/<int:cedula>")
def read_one(cedula):
    return "Reading a delegate ... soon"

#Crear delegados
@delegate.post("/")
def create():
    return "Creating a delegate ... soon"

#Actualizar delegados
@delegate.put('/<int:cedula>')
@delegate.patch('/<int:cedula>')
def update(cedula):
    return "Updating a delegate ... soon"

#Eliminar un delegados
@delegate.delete("/<int:cedula>")
def delete(cedula):
    return "Removing a delegate ... soon"
