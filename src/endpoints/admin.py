from flask import Blueprint, request
admin = Blueprint("admin",
                    __name__,
                    url_prefix="/api/v1/admin")

#Listar administradores
@admin.get("/")
def read_all():
    return "Reading all admin ... soon"

#Obtener información de un administrador
@admin.get("/<int:cedula>")
def read_one(cedula):
    return "Reading a admin ... soon"

#Obtener el historial de un parqueadero específico
@admin.get("/history/<int:id_parking>")
def specific_parking_history(id_parking):
    return "View a specific parking history ... soon"

#Obtener el historial de los parqueaderos
@admin.get("/history")
def parking_history(id_parking):
    return "View parking history ... soon"

#Crear administrador
@admin.post("/")
def create():
    return "Creating a admin ... soon"

#Actualizar administrador
@admin.put('/<int:cedula>')
@admin.patch('/<int:cedula>')
def update(cedula):
    return "Updating a admin ... soon"

#Eliminar un administrador
@admin.delete("/<int:cedula>")
def delete(cedula):
    return "Removing a admin ... soon"
