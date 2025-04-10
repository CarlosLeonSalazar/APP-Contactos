import json

class Contactos:
    """Clase Contactos:
        Esta clase representa un contacto con nombre, teléfono e email.
        La clase también tiene un método para convertir a un diccionario que posteriormente se guardará en una archivo json.
        
        __init__ Inicializar la clase con los atributos básicos de la clase
        
        __str__ Método para mostrar estado de los datos del contacto
        
        to_dict Método para convertir el contacto en un diccionario para guardarlo en un archivo json."""
        
    id_contacto = 0
    
    def __init__(self, nombre, telefono, email, ID=None):
        """Se inicialiaza con los datos básicos de la clase"""
        self.nombre = nombre
        self.telefono = telefono
        self.email = email
        if ID is not None:
            self.id = ID
        else:
            Contactos.id_contacto += 1
            self.id = Contactos.id_contacto

        
    def __str__(self):
        """Muestra la instacia de la clase"""
        return f"ID: {self.id} - Nombre: {self.nombre}, Teléfono: {self.telefono}, Email: {self.email}."
    
    def to_dict(self):
        """Convierte el contacto en un diccionario para guardarlo en un archivo json."""
        return {
            "ID" : self.id,
            "nombre": self.nombre,
            "telefono": self.telefono,
            "email": self.email
        }

    
class Gestor_contactos(Contactos):
    """Clase Gestor de contactos:
        Esta clase hereda de la clase Contactos y añade métodos para gestionar los contactos
        en un archivo definido como atributo de clase (archivo). 
        
        El acceso a ese archivo no depende de una instancia de Gestor_contactos, sino que es común a todas las instancias,
        permite que todos los contactos sean almacenados en un solo archivo sin necesidad de crear una instancia cada vez
        de la clase Gestor_contactos.
        
        Variable de clase: "archivo" que almacena al fichero contactos.json.
        
        Métodos de clase: cargar_contactos, guardar_contactos, crear_contactos, mostrar_contactos, buscar_contactos, eliminar conactos
        """
    # Variables de clase.
    archivos = "fichero_contactos.json"
    
    
    @classmethod
    def cargar_contactos(cls):
        """Cargar el archivo contactos.json
        
        return : lista de contactos
        """
        try:
            with open(cls.archivos, "r", encoding="utf-8") as file: 
                data = json.load(file)
                if data:
                    Contactos.id_contacto = max(contacto.get("ID", 0) for contacto in data)            
                return [Contactos(**contacto) for contacto in data]
        except FileNotFoundError:
            return []
            
    @classmethod
    def guardar_contactos(cls, contactos):
        """Guarda los contactos en un archivo .json
        
        Args: contactos
        
        Convierte la lista en un diccionario para ser almacenado en archivo .json y actualiza la información al sobrescribirla"
        """
        with open(cls.archivos, "w", encoding="utf-8") as file:
            json.dump([contacto.to_dict() for contacto in contactos], file, indent=4, ensure_ascii=False)

        
    @classmethod
    def crear_contacto(cls, nombre, telefono, email):
        """Función para crear nuevos contactos.
        
        Args. nombre, telefono, email
        
        Carga infomación del archivo con la función cls.cargar_contactos() y luego se guardan con la función cls.guardar_conactos
        """      
        contactos = cls.cargar_contactos()
        contacto_existente = next((contacto for contacto in contactos if contacto.email == email), None)
        if contacto_existente:
            print("Ya existe un contacto con ese email.")
        else:
            nuevo_contacto = Contactos(nombre, telefono, email)
            contactos.append(nuevo_contacto)
            cls.guardar_contactos(contactos)
            print(f"Se ha creado el nuevo contacto: {nuevo_contacto.nombre}")
        
    @classmethod
    def mostrar_contactos(cls):
        """Muestra un listado con todos los contactos"""
        contactos = cls.cargar_contactos()
        if contactos:
            print("Contactos registrados:")
            for contacto in contactos:
                print(contacto)
        else:
            print("No hay contactos registrados.")
            
    @classmethod
    def eliminar_contacto(cls, nombre):
        """Método para eliminar contactos
        
        Args: nombre
        """
        contactos = cls.cargar_contactos()
        if contactos:
            #nombre = input("Introduzca el nombre del contacto a eliminar: ")
            contacto_eliminar = next((contacto for contacto in contactos if contacto.nombre == nombre), None)
            if contacto_eliminar:
                contactos.remove(contacto_eliminar)
                cls.guardar_contactos(contactos)
                print(f"Se ha eliminado el contacto: {contacto_eliminar.nombre}")
            else:
                print("No se ha encontrado el contacto.")
        else:
            print("No hay contactos registrados.")
    
    @classmethod
    def buscar_contacto(cls, nombre):
        """Método para buscar contacto por el nombre
        
        Args: nombre
        """
        contactos = cls.cargar_contactos()
        if contactos:
            buscar_lista = []
            for contacto in contactos:
                if contacto.nombre == nombre:            
                    buscar_lista.append(contacto)
            if buscar_lista:
                print("Contactos encontrados:")
                for contacto in buscar_lista:
                    print(contacto)
            else:
                print("No se ha encontrado el contacto.")         
        else:
            print("No hay contactos registrados.")
    
if __name__ == "__main__":
    
    #Gestor_contactos.crear_contacto()
    #Gestor_contactos.mostrar_contactos()
    #Gestor_contactos.eliminar_contacto()
    #Gestor_contactos.mostrar_contactos()
    Gestor_contactos.buscar_contacto()

    
   