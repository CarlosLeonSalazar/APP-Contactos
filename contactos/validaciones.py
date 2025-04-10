import re


class Validar:
    """Esta clase 'Validar' agrupa 3 métodos para validar las entradas del usuario."""
    
    def validar_email(email):
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(email_regex, email):
            print("Email no válido. Inténtelo de nuevo.")
            return False
        else:
            return email
        
    def validar_telefono(telefono):
        telefono_regex = r'^\d{9}$'
        if not re.match(telefono_regex, telefono):
            print("Teléfono no válido. Inténtelo de nuevo.")
            return False
        else:
            return telefono
        
    def validar_nombre(nombre):
        nombre_apellido_regex = r'^[A-Za-zÁÉÍÓÚáéíóúÑñü\s]{1,50}$'
        if not re.match(nombre_apellido_regex, nombre):
            print("Nombre y apellido no válidos. Inténtelo de nuevo.")
            return False
        else:
            return nombre
        
if __name__ == '__main__':
    
    pass