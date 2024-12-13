from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Cliente:
    def __init__(self):
        self.__chrome_options = Options()
        self.__chrome_options.add_experimental_option("detach", True)
        self.__driver = None

    def iniciar(self, url):
        try:
            self.__driver = webdriver.Chrome(
                service=webdriver.chrome.service.Service(ChromeDriverManager().install()),
                options=self.__chrome_options
            )
            self.__driver.get(url)
        except WebDriverException:
            print("Error al iniciar el navegador")

    def scrollear_inicio(self):
        self.__driver.execute_script("window.scrollTo(0, 0);")

    def scrollear(self):
        posicion_actual = self.__driver.execute_script("return window.pageYOffset;")
        self.__driver.execute_script("window.scrollBy(0, window.innerHeight);")
        nueva_posicion = self.__driver.execute_script("return window.pageYOffset;")
        return nueva_posicion > posicion_actual

    def pasar_captcha(self):
        try:#No funciona con imagenes
            self.__driver.switch_to.frame(0)
            captcha_element = self.__driver.find_element(By.XPATH, '//*[@id="recaptcha-anchor"]')
            captcha_element.click()
            print("Captcha resuelto.")
            self.__driver.switch_to.default_content()
        except NoSuchElementException:
            self.recargar()
            self.pasar_captcha()
        except Exception:
            self.recargar()
            self.pasar_captcha()
        #SI OCURRE UN ERROR INTENTA RECARGAR LA PAGINA PARA VER SI PUEDE ENTRAR DNV ES UNA MALA PRACTICA YA QUE PUEDE BLOQUEAR LA IP AL HACER MUCHAS CONSULTAS

    def verificar(self, elemento):#Busca para clickear si se encuentra id ,class o el peor de los casos solamente la etiqueta
        if elemento is None:
            return
        try:
            if elemento["tipo"] == "id":
                self.__driver.find_element(By.ID, elemento["identificador"]).click()
            elif elemento["tipo"] == "class":
                self.__driver.find_element(By.CLASS_NAME, elemento["identificador"]).click()
            elif elemento["tipo"] is None:
                options = self.__driver.find_elements(By.TAG_NAME, elemento["categoria"])
                for el in options:
                    if elemento["nombre"] in el.text:
                        el.click()
                        return
            else:
                raise ValueError("Tipo de identificador no válido")
        except NoSuchElementException:
            print("Elemento no encontrado.")
        except Exception:
            print("Error al intentar clickear el elemento")

    def contenido_actual(self):
        if self.__driver:
            WebDriverWait(self.__driver, 10).until(
                EC.presence_of_element_located((By.TAG_NAME, "body"))
            )#antes de devolver la pagina cargada espera a que cargue el cuerpo del html
            return self.__driver.page_source

    def rellenar(self, elemento, escribir):
        try:
            campo = self.__driver.find_element(By.ID, elemento)
            campo.clear()
            campo.send_keys(escribir)
        except NoSuchElementException:
            print(f"No se encontró el elemento con ID '{elemento}'.")
        except Exception:
            print("Error al intentar rellenar el campo")

    def recargar(self):
        self.__driver.refresh()

    def extraer_detalles(self, formato):
        try:#busca el elemento del formato modificado y lo clikea para ver los detalles
            elemento = self.__driver.find_element(By.XPATH, f'//*[@onclick="{formato}"]')
            ActionChains(self.__driver).move_to_element(elemento).click().perform()
            return True
        except Exception:
            if self.scrollear():#si ocurre un error intenta scrollear 
                return self.extraer_detalles(formato)
            return None #no se puede scrollear mas

    def pagina_anterior(self):
        self.__driver.back()

    def pag_sig(self):
        try:
            contenedor = self.__driver.find_element(By.XPATH, "//span[text()='Siguiente ']/..")
            ActionChains(self.__driver).move_to_element(contenedor).click().perform()
            return True
        except NoSuchElementException:
            return False

    def cerrar(self):
        try:
            if self.__driver:
                self.__driver.quit()
                self.__driver = None
        except Exception as e:
            print(f"Ocurrió un error al intentar cerrar el navegador: {e}")