from aplicacion.config.mysqlconnection import connectToMySQL #siempre importar la conección con la base de datos
from flask import flash

class Encuestado:
    def __init__(self,data):
        # acá van todas las columnas de la tabla de workbench
        self.id = data['id']
        self.nombre = data['nombre']
        self.apellido = data['apellido']
        self.ubicacion= data['ubicacion']
        self.lenguaje = data['lenguaje']
        self.comentario = data['comentario']
        self.genero = data['genero']
        self.terminos = data['terminos']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

        #METODO CREAR
    @classmethod
    def creardojo(cls,data):
        consulta = "INSERT INTO dojos (nombre, apellido, ubicacion, lenguaje, comentario, genero, terminos) VALUES (%(nombre)s,%(apellido)s,%(ubicacion)s,%(lenguaje)s,%(comentario)s, %(genero)s, %(terminos)s);"
        resultado = connectToMySQL("esquema_encuesta_dojo").query_db(consulta,data)
        return resultado
    
    #METODO DE LECTURA
    @classmethod
    def un_encuestado(cls,data):
        consulta = "SELECT * FROM dojos WHERE id = %(id)s"
        resultado = connectToMySQL ("esquema_encuesta_dojo").query_db(consulta, data)
        #esto es para copnvertir ese diccionario en objeto. como es una lista que contiene VARIOS diccionarios.
        return cls(resultado[0])
    
    @staticmethod
    def validate_encuestado(encuestado):
        is_valid = True # asumimos que esto es true
        if len(encuestado['nombre']) < 3:
            flash("Tu nombre debe contener al menos 3 carácteres.")
            is_valid = False
        if len(encuestado['apellido']) < 3:
            flash("Tu apellido debe contener al menos 3 carácteres.")
            is_valid = False
        #en estos dos que son de selección, deje que la opcion por defecto tenga como value 1 caracter, asi se asegura que elija uno diferente al por defecto
        if len(encuestado['ubicacion']) < 3:
            flash("Debes elegir una ubicación")
            is_valid = False
        if len(encuestado['lenguaje']) < 3:
            flash("Debes elegir un lenguaje")
            is_valid = False
        
        if len(encuestado['comentario']) < 3:
            flash("Tu comentario debe tener al menos 3 carácteres")
            is_valid = False 
        
        # if len(encuestado['genero']) < 3:
        #     flash("Debes elegir un genero")
        #     is_valid = False
        # if  len(encuestado['terminos']) <1:
        #     flash("Debes aceptar nuestros términos y condiciones")
        #     is_valid = False
        
        return is_valid
