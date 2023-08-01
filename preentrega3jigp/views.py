from django.http import HttpResponse
from django.template import Template, Context 

def saludo(request):
    return HttpResponse("Hola mundo!!!")

def bienvenidos(request):
    return HttpResponse("<html><h1>Bienvenidos a su pagina de inicio</h1></html>")

def pruebatemplate(request):
    with open("C:/Users/User/OneDrive/Escritorio/Python CoderHouse/PreEntrega3/preentrega3jigp/preentrega3jigp/plantillas/index.html") as file:
        plantilla = Template(file.read())
    contexto = Context()
    documento = plantilla.render(contexto)
    return HttpResponse(documento)

    