# capa de vista/presentación

from django.shortcuts import redirect, render
from .layers.services.services import getAllImages  # Asegúrate de importar correctamente
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

def index_page(request):
    return render(request, 'index.html')

# Esta función obtiene los listados de imágenes de la API y los usa para dibujar el template.
def home(request):
    input_name = request.GET.get('name', '')  # Obtener el nombre desde el query string
    images = getAllImages(input_name)  # Llama a la función para obtener las imágenes
    favourite_list = []  # Aquí puedes agregar la lógica para obtener favoritos si lo deseas

    return render(request, 'home.html', {'images': images, 'favourite_list': favourite_list})

def search(request):
    search_msg = request.POST.get('query', '')

    if search_msg != '':
        # Aquí puedes implementar la lógica para buscar imágenes si lo deseas.
        # Por ahora, redirigimos a la vista home con el query como parámetro.
        return redirect('home')  # Cambia esto para que incluya el nombre en la URL
    else:
        return redirect('home')

# Funciones que se usan cuando el usuario está logueado en la aplicación.
@login_required
def getAllFavouritesByUser(request):
    favourite_list = []
    return render(request, 'favourites.html', {'favourite_list': favourite_list})

@login_required
def saveFavourite(request):
    pass

@login_required
def deleteFavourite(request):
    pass

@login_required
def exit(request):
    pass
