# Esta Clase representa a los usuarios de mi app
class Usuario:
    def __init__(self, nombre, correo, password):

        print("se creó un nuevo usuario")

        self.nombre = nombre
        self.correo = correo
        self.password = password

        #si el usuario tiene una sesión activa
        self.sesion =  False

    def iniciar_sesion(self):
        print("Estamos iniciando sesión")

    def cerrar_sesion(self):
        print("Estamos cerrando sesión")


