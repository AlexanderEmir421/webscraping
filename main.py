from scraping import Scrapping
from cliente import Cliente
from db import DatabaseManager

class GestorScraping:
    def __init__(self, urls,db, palabra_clave="RESIDUOS"):
        self.__urls = urls
        self.__palabra_clave = palabra_clave
        self.__escrapear = Scrapping()
        self.__cliente = Cliente()
        self.__db=db

    def procesar_url(self, url):
        print(f"Accediendo a: {url}")
        self.__cliente.iniciar(url)
        self.__cliente.pasar_captcha()
        #Se puede elegir diferentes categorias "parte"- "histórico"- "expediente"
        self.procesar_categoria("parte")
        #Selecciona cualquier jurisdiccion caso "com"
        self.procesar_categoria("com")
        # Rellenar formulario con palabra clave y enviar
        self.__cliente.rellenar("formPublica:nomIntervParte", self.__palabra_clave)
        self.__cliente.verificar({"tipo": "id", "identificador": "formPublica:buscarPorParteButton"})
        # Extraer datos hasta q no se encuentren elementos
        self.extraer_datos()

    def procesar_categoria(self, categoria):#obtiene el contenido actual y clikea la categoria
        self.__escrapear.parsear(self.__cliente.contenido_actual())
        encontrado = self.__escrapear.obtener_forms(categoria)
        if encontrado:
            self.__cliente.verificar(encontrado)

    def extraer_datos(self):
        fin = True
        while fin:
            self.__escrapear.parsear(self.__cliente.contenido_actual())
            formato = self.__escrapear.buscar_detalles()#ENCUENTRA EL PRIMER EVENTO PARA MODIFICAR SU ESTRUCTURA
            evento = self.__cliente.extraer_detalles(formato)

            i = 0
            while evento is not None:
                self.__escrapear.parsear(self.__cliente.contenido_actual())
                self.__escrapear.ver_detalles(db)
                self.__cliente.pagina_anterior()
                i += 1
                evento = self.__cliente.extraer_detalles(formato.replace("dataTable:0", f"dataTable:{i}"))#SE MODIFICA LA ESTRUCTURA DEL FORMATO

            if evento is None:#si no hay mas elementos pregunta si hay una pagina siguiente
                if self.__cliente.pag_sig():
                    self.__cliente.scrollear_inicio()
                else:
                    fin = False#Si no hay pagina siguiente termina el bucle

    def ejecutar(self):
        for url in self.__urls:
            try:
                self.procesar_url(url)
            except Exception as e:
                print(f"Error procesando {url}: {e}")
    
    def cerrar(self):
        self.__cliente.cerrar()
        self.__db.cerrar()

if __name__ == "__main__":
    URLS = ["http://scw.pjn.gov.ar/scw/home.seam"]
    db=DatabaseManager()
    try:
        gestor = GestorScraping(URLS, db)
        gestor.ejecutar()
    finally:
        gestor.cerrar()