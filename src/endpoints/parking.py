from flask import Blueprint, request
parking = Blueprint("parking",
                    __name__,
                    url_prefix="/api/v1/parking")

#Listar parqueaderos
@parking.get("/")
def read_all():
    return "Reading all parking ... soon"

#Obtener información de un parqueadero
@parking.get("/<int:id>")
def read_one(id):
    return "Reading a parking ... soon"

#Crear parqueaderos
@parking.post("/")
def create():
    return "Creating a parking ... soon"

#Actualizar parqueaderos
@parking.put('/<int:id>')
@parking.patch('/<int:id>')
def update(id):
    return "Updating a parking ... soon"

#Eliminar un parqueaderos
@parking.delete("/<int:id>")
def delete(id):
    return "Removing a parking ... soon"
