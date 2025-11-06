from app.controllers.docente_controller import DocentreController

def main():
    #+print(DocentreController.crear("Juan David Trana","jtriana@devsenior.com"))
    print(DocentreController.obtener(1))
    print("Llamada desde main")

if __name__ == '__main__':
    main()