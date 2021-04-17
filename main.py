# 1.
import requests
from bs4 import BeautifulSoup

# Obtener la URL y almacenarla en una variable:
'''
- En primer lugar, importe la biblioteca de solicitudes.

- Luego, especifique la URL de la página web que desea hacer srape.

- Envíe una solicitud HTTP a la URL especificada

- y guarde la respuesta del servidor en un objeto de respuesta

- Ahora, como print .content para obtener el contenido HTML sin formato de la página web. Es de tipo "cadena".
'''

'Pagina Oficial del challange'
url = 'https://www.100daysofcode.com/'

'''
Una de las operaciones más habituales con la librería requests es hacer una petición GET,
ya sea para obtener el contenido de una web o para realizar una petición a un API.

Para ello, simplemente tienes que invocar a la función get()
indicando la URL a la que hacer la petición.
'''
page = requests.get(url)
print(page.content)

# 2.
soup = BeautifulSoup(page.text, "html.parser")
print(soup)

# 3.
'Vamos a buscar etiquetas dentro del html con .find_all()'

days100_tags = soup.find_all("Next Steps")


# 3.
'''
Luego puede copiar la etiqueta HTML y la clase, si corresponde,
y luego colocarla dentro del método soup.find_all()
En este caso, la etiqueta HTML es " span " y la clase es " tag-box-choosetags"
'''
days100_tags = soup.findAll('6 More', {'class': 'tag-box-choosetangs'})
print(days100_tags)
