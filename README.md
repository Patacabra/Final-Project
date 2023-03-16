
# Proyecto final Ironhack

Proyecto de sistema de recomendación de cursos online a través de las plataformas de Coursera, Domestika y Udemy.

Con la idea de dar algo más de accesibilidad al conocimiento y a meter un poco cabeza en el mundillo 'Tech' para poder ir avanzando por cuenta propia.




## Extracción de datos

A través de web scraping con las herramientas BeautifulSoup para Doméstika, Selenium para Coursera y Udemy.

## Limpieza y Transformación de los datos

Con la ayuda de las librerías de Python, Pandas y NumPy he conseguido solucionar la problemática de la limpieza de los datos ya que había mucho ruido en ellos, saltos de línea, caracteres especiales, datos extra que no deberían estar ahí...

Se arreglaron los datos de tal manera que se crearon 3 archivos .csv diferentes, uno por cada una de las plataformas, con la misma distribución en las columnas para posteriormente una vez limpios agrupar todos los datos en un mismo archivo.

Se hizo alguna copia de este mismo archivo para modificarlo añadiendo en la columnas los nombres de las personas que puntuaron los cursos con su correspondiente puntuación para cada uno, todo esto con la intención de utilizar estos datos para el sistema de recomendación que viene después.

##  Visualización

He utilizado Tableau para visualizar los datos y tener una mejor idea de lo que tengo entre manos, como ver en qué franja de precios se suelen mover los cursos de Doméstika, por dónde anda el nivel de los cursos de Udemy, o qué tipo de organizaciones lideran el ranking de mayor número de cursos en Coursera.


### Precios de los cursos de Doméstika

![](/Users/fernando/Desktop/Final-Project/ProyectoFinal/image/1.png)

### Nivel de los cursos de Udemy

![](/Users/fernando/Desktop/Final-Project/ProyectoFinal/image/2.png)

### Organizaciones de los cursos de Coursera

![](/Users/fernando/Desktop/Final-Project/ProyectoFinal/image/3.png)

## Sistema de recomendación
Para el sistema de recomendación he utilizado un filtro colaborativo basado en usuarios.

Como una imagen vale más que mil palabras... Aquí dejo una explicación gráfica de lo que viene a ser el filtro basado en usuarios:

![](/Users/fernando/Desktop/Final-Project/ProyectoFinal/image/5.png)

Este determina un patrón de gustos y preferencias.
Utiliza los datos de un vecino cercano con características similares al inicial .

![](/Users/fernando/Desktop/Final-Project/ProyectoFinal/image/4.png)

El cual tiene una serie de beneficios tales como:

- Mejor satisfacción de las necesidades del cliente.
- La experiencia del usuario se convierte en una actividad más  agradable.
- Aportan una eficiencia excepcional a las conversiones de los sitios web.
- Acerca al cliente a lo que desea.

Para hacer todo este proceso he necesitado el uso de Pandas, Pylab para los gráficos, Matplotlib y SciPy.

Se ha modificado el dataframe que contenía el nombre de las personas que han calificado los cursos utilizando el título de los cursos como index del dataframe para poder trabajar con el proceso.

También se ha tenido que crear el nuevo usuario, con las calificaciones de los cursos que ha visto para ver las relaciones que tiene con el resto de la gente y acabar comparándolo con los que no ha visto y cuanto de relevante es para el nuevo usuario los cursos que se le recomienda.

## APP WEB 
Se ha creado una sencilla aplicación web a través de la librería Streamlit de python para empezar a poner en funcionamiento el proyecto 

![](/Users/fernando/Desktop/Final-Project/ProyectoFinal/image/6.png)

## Extra

El proyecto, aunque presentado aun no se encuentra finalizado ya que tengo en mente añadir unas funcionalidades que mejorarán el uso de esta aplicación web.

- Hacer scraping a tiempo real para obtener la información más reciente posible.
- Llevar esta información a una base de datos de MongoDB la cual estará actualizando la app web.
- Añadir funcionalidades de búsqueda en Streamlit tales como búsqueda por precio del curso, por el tipo de titulación que te ofrece, la cantidad de clases o el tiempo de duración del curso.
- Añadir una ruta específica para lograr tus metas, como un recorrido por los cursos más interesantes en orden creciente de dificultad para alcanzar ser un buen analista de datos, diseñador gráfico o productor de música ... 