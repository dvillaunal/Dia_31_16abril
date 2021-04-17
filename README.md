# Web scraping:

## Tips para hacer Scraping:
 * *Comprueba siempre los términos y condiciones del sitio web antes de hacer scraping. Suelen tener condiciones que limitan la frecuencia con la que se puede hacer scraping o lo que se puede hacer.*

 * *Dado que tu script se ejecutará mucho más rápido de lo que un humano puede navegar, asegúrate de no martillear su sitio web con muchas peticiones. Esto puede incluso estar contemplado en los términos y condiciones del sitio web.*
 
 * *Puedes tener problemas legales si sobrecargas un sitio web con tus peticiones o intentas usarlo de una manera que viola los términos y condiciones que aceptaste.*
 
 * *Los sitios web cambian todo el tiempo, así que tu Scraping se romperá algún día. Sepa esto: Tendrás que mantener tu scraper si quieres que siga funcionando.*


***-> Nota:***
  * Desgraciadamente, los datos que obtienes de los sitios web pueden ser un desastre. Como con cualquier actividad de análisis de datos, tendrás que limpiarlos para que te sean útiles.
  * [Cómo hacer scraping un sitio web sin entrar en la lista negra
](https://hackernoon.com/how-to-scrape-a-website-without-getting-blacklisted-271a605a0d94?source=post_page---------------------------)
-----

## 1. Importación de las bibliotecas necesarias:

Importemos algunas bibliotecas importantes como Requests y BeautifulSoup .

~~~
import requests
from bs4 import BeautifulSoup
~~~
## 2. Usar la biblioteca Beautiful Soup para obtener los datos HTML (sin procesar) del sitio web:

Aquí usamos BeautifulSoup pasando el texto de la página como parámetro y usando el analizador HTML. Puede intentar imprimir la sopa, pero imprimir ``soup`` no le da la resultado, sino que contiene grandes cantidades de datos HTML, así que decidí no mostrarla aquí.

*Una cosa realmente buena de la biblioteca BeautifulSoup es que está construida en la parte superior de las bibliotecas de análisis HTML como html5lib, lxml, html.parser, etc. Así que el objeto BeautifulSoup y especificar la biblioteca del analizador se pueden crear al mismo tiempo.*

~~~
'line 20'
soup = BeautifulSoup(página de texto, "html.parser")
~~~



