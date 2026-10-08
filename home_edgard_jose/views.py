from django.shortcuts import render


GENEROS = [
    {'id': 'accion', 'nombre': 'Acción', 'descripcion': 'Películas con mucha adrenalina y persecuciones'},
    {'id': 'drama', 'nombre': 'Drama', 'descripcion': 'Películas con intensas emociones y conflictos'},
]


def vista(request):
    contexto = {'generos': GENEROS}
    return render(request, 'home/home.html', contexto)


def ver_genero(request, categoria):
    peliculas_db = {
        'accion': [
            
        ],
        'drama': [
           
]
    }

    peliculas_filtradas = peliculas_db.get(categoria, [])
    contexto = {
        'categoria': categoria,
        'peliculas': peliculas_filtradas,
        'generos': GENEROS,
    }
    return render(request, 'home/peliculas.html', contexto)