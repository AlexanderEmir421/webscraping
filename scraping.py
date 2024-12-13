from bs4 import BeautifulSoup
from db import DatabaseManager

class Scrapping:
    def __init__(self):
        self.__texto = None

    def get_texto(self):
        return self.__texto

    def parsear(self, text):
        self.__texto = BeautifulSoup(text, "html.parser")

    def buscar(self, form, texto):
        encontrado = {
            "identificador": None,
            "tipo": None,
            "nombre": None,
            "categoria": None,
        }
        elementos = form.find_all(True)  # Encuentra todas las etiquetas dentro del formulario
        for elemento in elementos:
            palabras = elemento.get_text(strip=True).lower().split()
            if texto.lower() in palabras:
                encontrado["categoria"] = elemento.name
                encontrado["nombre"] = elemento.get_text(strip=True)
                if elemento.has_attr("id"):
                    encontrado["tipo"] = "id"
                    encontrado["identificador"] = elemento["id"]
                elif elemento.has_attr("class"):
                    encontrado["tipo"] = "class"
                    encontrado["identificador"] = elemento["class"]
                return encontrado  
        return encontrado

    def obtener_forms(self, palabra):
        if self.__texto is None:
            return None
        forms = self.__texto.find_all('form')
        for form in forms:
            encontrado = self.buscar(form, palabra)
            if encontrado["nombre"] is not None:
                self.__texto = form#Si se encuentra el formulario buscado se limpia el html para una busqueda mas rapida
                return encontrado
        return None

    def buscar_contenido_label_span(self, palabra):#Se identifico q cada dato que necesitaba tenia un label y dentro su contenido
        encontrado = {
            "titulo": palabra,
            "contenido": None
        }
        labels = self.__texto.find_all("label")
        for label in labels:
            if palabra in label.get_text():
                span = label.find_next("span")
                if span:
                    encontrado["contenido"] = span.get_text(strip=True)
                    return encontrado
        return encontrado

    def buscar_elemento(self, palabra):
        return self.buscar(self.__texto, palabra)

    def buscar_detalles(self):#Busca el evento en comun 
        for element in self.__texto.find_all(attrs={"onclick": True}):
            if "mojarra.jsfcljs" in element["onclick"]:
                return element["onclick"]

    def ver_detalles(self,db):#Añadir buscar demandate y demandado
        palabras_clave = [
            "Expediente:", "Jurisdicción:", "Dependencia:", "Sit. Actual:", "Carátula:"
        ]
        guardar=[]
        for palabra in palabras_clave:
            resultado = self.buscar_contenido_label_span(palabra)
            if resultado["contenido"]:
                guardar.append(resultado["contenido"])
            else:
                guardar.append(None)
        db.guardar_dato(guardar)