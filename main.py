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

########################## Ejemplo de web scraping ##########################
import pandas as pd
import requests
from bs4 import BeautifulSoup

# Vamos a extraer información de la liga satander del Diario AS:
'Ponemos en una varible la url'

dweb = 'https://resultados.as.com/resultados/futbol/primera/clasificacion/' # <. Tipo str

page_AS = requests.get(dweb) # <- Ahora descargamos el contenido de la pagina

# Ahora transformamos a formato HTML para poder ir accediendo a los diferentes elementos de la pagina
'Así podemoes empexar a escraper'

soup_AS = BeautifulSoup(page_AS.content, 'html.parser') # <- interpreta como html

# Inspeccionar por Equipos 
'Con el .find_all busco en el archivo soup_AS (de BeautifulSoup) por "span" y despues'
'por una clase que se puede visualizar en el link del video (opciones de programador)'
'llamada "nombre-equipo"  para doder guardar los resultados en listas'

eq = soup_AS.find_all('span', {'class': 'nombre-equipo'})

lista_equipos = list()

# Un for para guardar solamente los nombre de cada equipo (Estamos depurando datos):

c = 0 # un count para que los nombres de los equipos no se repitan, inventigando solo son los priemros 20 (como se ve en la pagina) 
for i in eq:
  if c < 20: # es estrictamente  a 20 porque se toma desde el cero
    lista_equipos.append(i.get_text())
  else:
    break
  c += 1

# Ahora hacemos lo mismo para la puntiación de los equipos:

pt = soup_AS.find_all('td', {'class': 'destacado'})

puntuacion = list()

# Un for para guardar solamente los puntos por cada equipo (Estamos depurando datos):

c = 0 # un count para que los puntos de los equipos no se repitan
for i in pt:
  if c < 20: # es estrictamente  a 20 porque se toma desde el cero
    puntuacion.append(i.get_text())
  else:
    break
  c += 1

print(puntuacion)

# Importe pandas para hacer un data frame y guardar el scrape hecho:

'Guardamos un data frame los Nombres de los equipos y sus respectivvos puntos'
'Como el dataframe empieza en 0 le decimos que empiece en 1 y termine en 21 = 20(elemntos) + 1(el valor agregado)'

puntosXequipo = pd.DataFrame({'Nombre de Equipo': lista_equipos, 'Puntos': puntuacion}, index= list(range(1,21)))
print(puntosXequipo)

# Guardaremos en csv (Una buena practia de Scraping guardar los datos depurados):
'Ya que con .to_excel esta pronto quedar sin soporte entonces utlizare .to_csv'
'Además asi se podra visualizar desde el replit el csv'

puntosXequipo.to_csv('Puntos_por_Equipo_(Liga Santander).csv', index=False)