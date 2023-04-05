from flask import Blueprint, request
users = Blueprint("users",
                    __name__,
                    url_prefix="/api/v1/users")

#Listar usuarios
@users.get("/")
def read_all():
    return "Reading all users ... soon"

#Obtener información de un usuario
@users.get("/<int:cedula>")
def read_one(cedula):
    return "Reading a user ... soon"

#Encontrar vehiculo
@users.get("/<int:cedula>/vehicle")
def find_vehicle(cedula):
    return "Find a vehicle from user ... soon"

#Crear usuario
@users.post("/")
def create():
    return "Creating a user ... soon"

#Actualizar usuario
@users.put('/<int:cedula>')
@users.patch('/<int:cedula>')
def update(cedula):
    return "Updating a user ... soon"

#Eliminar usuario
@users.delete("/<int:cedula>")
def delete(cedula):
    return "Removing a user ... soon"
