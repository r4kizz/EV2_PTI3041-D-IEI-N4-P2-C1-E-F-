from django.shortcuts import render


GENEROS = [
    {'id': 'comedia', 'nombre': 'Comedia', 'descripcion': 'Películas con mucha risa y situaciones locas'},
    {'id': 'drama', 'nombre': 'Drama', 'descripcion': 'Películas con intensas emociones y conflictos'},
]


def vista(request):
    contexto = {'generos': GENEROS}
    return render(request, 'home/home.html', contexto)


def ver_genero(request, categoria):
    peliculas_db = {
        'comedia': [
            {'nombre': 'Supercool', 'anio': 2007, 'imagen': 'images/comedia/supercool.png'},
            {'nombre': '¿Qué pasó ayer?', 'anio': 2009, 'imagen': 'images/comedia/quepasoayer.png'},
            {'nombre': 'No Te Metas Con Zohan', 'anio': 2008, 'imagen': 'images/comedia/zohan.png'},
            {'nombre': 'La Máscara', 'anio': 1994, 'imagen': 'images/comedia/lamascara.png'},
            {'nombre': 'Ted', 'anio': 2012, 'imagen': 'images/comedia/ted.png'},
            {'nombre': 'Shrek', 'anio': 2001, 'imagen': 'images/comedia/shrek.png'},
            {'nombre': 'Tren Bala', 'anio': 2022, 'imagen': 'images/comedia/trenbala.png'},
            {'nombre': 'Donde Estan Las Rubias', 'anio': 2004, 'imagen': 'images/comedia/rubias.png'},
            {'nombre': 'Scary Movie', 'anio': 2026, 'imagen': 'images/comedia/scary.png'},
            {'nombre': 'Zoolander', 'anio': 2001, 'imagen': 'images/comedia/zoolander.png'},
        ],
        'drama': [
            {'nombre': 'El Padrino', 'anio': 1972, 'imagen': 'images/drama/elpadrino.png'},
            {'nombre': 'Eterno Resplando: de una mente sin recuerdos', 'anio': 2004, 'imagen': 'images/drama/eterno.png'},
            {'nombre': 'Forrest Gump', 'anio': 1994, 'imagen': 'images/drama/forrestgump.png'},
            {'nombre': 'Lo Imposible', 'anio': 2012, 'imagen': 'images/drama/imposible.png'},
            {'nombre': 'El club de la pelea', 'anio': 1999, 'imagen': 'images/drama/clubpelea.png'},
            {'nombre': 'El Shwon de Truman', 'anio': 1998, 'imagen': 'images/drama/truman.png'},
            {'nombre': 'En busca de la felicidad', 'anio': 2006, 'imagen': 'images/drama/felicidad.png'},
            {'nombre': 'El Niño Con El Pijama De Rayas', 'anio': 2008, 'imagen': 'images/drama/rayas.png'},
            {'nombre': 'Titanic', 'anio': 1997, 'imagen': 'images/drama/titanic.png'},
            {'nombre': 'Whiplash', 'anio': 2014, 'imagen': 'images/drama/whiplash.png'},
            {'nombre': 'Requiem Por Un Sueño', 'anio': 2000, 'imagen': 'images/drama/requiem.png'},
]
    }

    peliculas_filtradas = peliculas_db.get(categoria, [])
    contexto = {
        'categoria': categoria,
        'peliculas': peliculas_filtradas,
        'generos': GENEROS,
    }
    return render(request, 'home/peliculas.html', contexto)