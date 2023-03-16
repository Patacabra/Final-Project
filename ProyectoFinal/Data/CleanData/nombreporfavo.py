import streamlit as st
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from PIL import Image

Cursosfer = ['Dibujo de personajes con gouache y lápices de colores',
       'Storytelling and influencing: Communicate with impact',
       'Introducción a la arquitectura de interiores: reforma una vivienda',
       'Fundamentals of Accounting',
       'Introducción al moulage: modelado sobre maniquí',
       'Inteligencia Artificial aplicada Proyectos Arquitectónicos\nAprende a generar imágenes digitales para tus diseños de Interiorismo y Arquitectura con Inteligencia Artificial (AI)'
       'Ilustración para packaging: crea diseños de productos únicos',
       'Tejido de punto para prendas infantiles',
       'Curso: Playwright con Javascript en Español\nAprende Automatización de Pruebas con Playwright con Javascritp nivel Basico- Intermedio',
       'Fotografía de retrato en superficies traslúcidas',
       'WhatsApp Api con PHP Envío y Recepción de Mensajes\nWhatsApp Api con PHP Envío y Recepción de Mensajes, Creación de un Chat BOT, Integración con CHATGPT',
       'Cómo hacer Campañas de Ingeniería Social\nPhishing 101',
       'Google Sheets. La hoja de Cálculo - Formulas y Funciones\nAprende a usar La hoja de Cálculo de Google con ejercicios de fórmulas y funciones, además desde tu dispositivo móvil.',
       'Curso de Autodesk Inventor 2021\n¿Te gustaría ser más productivo y desarrollar proyectos de la industria Mecánica, Industrial y de Manufactura?',
       'Diseño de personajes con cerámica: explora el color y la textura',
       'Curso de ChatGPT para principiantes - Aprenda a utilizar el\nUtilización de la inteligencia artificial en los negocios y en la vida cotidiana con el software OpenAI Curso básico',
       'Aprende JavaScript de CERO a EXPERTO\nAprende JavaScript sin ningún conocimiento previo',
       'Bordado con textura: combina puntadas y mostacillas',
       'Retrato experimental con tinta, alcohol y té',
       'Email marketing para impulsar tu negocio',
       'Ilustración con acrílico: crea universos mágicos',
       'Branding innovador: crea una identidad visual completa',
       'Finanzas personales',
       'Creación de paisajes contemporáneos en acuarela']


links = ['https://www.domestika.org/es/courses/3718-dibujo-de-personajes-con-gouache-y-lapices-de-colores',
         'https://www.coursera.org/learn/communicate-with-impact',
         'https://www.domestika.org/es/courses/2872-introduccion-a-la-arquitectura-de-interiores-reforma-una-vivienda?nbt=nb%3Aadwords%3Ag%3A17619083267%3A141287925962%3A614115063759&nb_adtype=&nb_kwd=&nb_ti=aud-365262770871:dsa-1713741220453&nb_mi=&nb_pc=&nb_pi=&nb_ppi=&nb_placement=&nb_li_ms=&nb_lp_ms=&nb_fii=35668970497&nb_ap=&nb_mt=&gclid=CjwKCAjw_MqgBhAGEiwAnYOAenn_ZwiVJjbloqD-CxLill4R_5JiHOAKuP4a_2nfaadcpRqIFoZVFxoCLhQQAvD_BwE','https://www.coursera.org/specializations/accounting-fundamentals',
         'https://www.domestika.org/es/courses/2858-introduccion-al-moulage-modelado-sobre-maniqui?nbt=nb%3Aadwords%3Ag%3A17619083267%3A141287926202%3A614247569414&nb_adtype=&nb_kwd=&nb_ti=aud-365262770871:dsa-1613432933488&nb_mi=&nb_pc=&nb_pi=&nb_ppi=&nb_placement=&nb_li_ms=&nb_lp_ms=&nb_fii=23630962393&nb_ap=&nb_mt=&gclid=CjwKCAjw_MqgBhAGEiwAnYOAeiisV7F1UvNJjA6TdLPALpPY_Xy-MITD9noCXxK7EfdY8k4cN1dRkhoCJWoQAvD_BwE',
         'https://www.udemy.com/course/arquitectura-ia/',
         'https://www.domestika.org/es/courses/2388-tejido-de-punto-para-prendas-infantiles?nbt=nb%3Aadwords%3Ag%3A17619083267%3A133422094690%3A607064987683&nb_adtype=&nb_kwd=&nb_ti=aud-1210842837973:dsa-1515013238540&nb_mi=&nb_pc=&nb_pi=&nb_ppi=&nb_placement=&nb_li_ms=&nb_lp_ms=&nb_fii=23630961214&nb_ap=&nb_mt=&gclid=CjwKCAjw_MqgBhAGEiwAnYOAehmCtOeGoi1rl1z5FuSGY7VV13AMm8cgLGvO1IaUaLoy-BqV2WwNZBoCAa0QAvD_BwE',
         'https://www.udemy.com/course/curso-playwright-con-javascript-en-espanol/',
         'https://www.domestika.org/es/courses/3582-fotografia-de-retrato-en-superficies-traslucidas',
         'https://www.udemy.com/course/whatsapp-api-con-php-envio-y-recepcion-de-mensajes/',
         'https://www.udemy.com/course/phishing101/',
         'https://www.udemy.com/course/hojas-calculos-google-funciones-formulas-smartphone/',
         'https://www.udemy.com/course/curso-de-inventor-2021/',
         'https://www.domestika.org/es/courses/3577-diseno-de-personajes-con-ceramica-explora-el-color-y-la-textura',
         'https://www.udemy.com/course/curso-de-chatgpt-para-principiantes-aprenda-a-utilizar-el/',
         'https://www.udemy.com/course/aprende-javascript-de-cero-a-experto/',
         'https://www.domestika.org/es/courses/2774-bordado-con-textura-combina-puntadas-y-mostacillas',
         'https://www.domestika.org/es/courses/2688-retrato-experimental-con-tinta-alcohol-y-te?nbt=nb%3Aadwords%3Ag%3A17619083267%3A133422094770%3A607064987755&nb_adtype=&nb_kwd=&nb_ti=aud-1365785360523:dsa-1659327555241&nb_mi=&nb_pc=&nb_pi=&nb_ppi=&nb_placement=&nb_li_ms=&nb_lp_ms=&nb_fii=23630963263&nb_ap=&nb_mt=&gclid=CjwKCAjw_MqgBhAGEiwAnYOAeoWoyOKCwi3q34W51W40H1NAbqVuGmYwLavfltZ6by8R7f7QDsGXdRoC_nkQAvD_BwE',
         'https://www.domestika.org/es/courses/2270-email-marketing-para-impulsar-tu-negocio',
         'https://www.domestika.org/es/courses/2369-ilustracion-con-acrilico-crea-universos-magicos',
         'https://www.domestika.org/es/courses/3244-branding-innovador-crea-una-identidad-visual-completa',
         'https://www.coursera.org/learn/finanzas-personales',
         'https://www.domestika.org/es/courses/2289-creacion-de-paisajes-contemporaneos-en-acuarela?nbt=nb%3Aadwords%3Ag%3A17619083267%3A133422094770%3A607064987755&nb_adtype=&nb_kwd=&nb_ti=aud-1365785360523:dsa-1659327555241&nb_mi=&nb_pc=&nb_pi=&nb_ppi=&nb_placement=&nb_li_ms=&nb_lp_ms=&nb_fii=23630961145&nb_ap=&nb_mt=&gclid=CjwKCAjw_MqgBhAGEiwAnYOAeo8KKTwh-_DP3ZdSV-YlQD_EUQ0Dh2jz7wI8JBXMFNmtlE9rDPwE7hoCTvgQAvD_BwE']

recomendacion = ['Masters en Excel 1',
                 'Reconocimiento de Huella Dactilar en Excel',
                 'DaVinci Resolve para corrección de color profesional en cine',
                 'Nivel 3. Integrarse en el ecosistema',
                 'Uso Profesional de tus archivos en la Nube con Google Drive']


linksreco = ['https://www.udemy.com/course/universidad-excel-microsoft-tablas-dinamicas-dashboard-macros-vba/',
             'https://www.udemy.com/course/reconocimiento-de-huella-dactilar-en-excel/',
             'https://www.domestika.org/es/courses/3028-davinci-resolve-para-correccion-de-color-profesional-en-cine?nbt=nb%3Aadwords%3Ag%3A17619083267%3A133422094530%3A607064987647&nb_adtype=&nb_kwd=&nb_ti=aud-1210842837973:dsa-1659327555081&nb_mi=&nb_pc=&nb_pi=&nb_ppi=&nb_placement=&nb_li_ms=&nb_lp_ms=&nb_fii=23630962291&nb_ap=&nb_mt=&gclid=CjwKCAjw_MqgBhAGEiwAnYOAevUYvgQjpW_ZcSOVRH_zqBlRLsV6AePAtxBTKBZvACIo5lmXT4ITshoCpRoQAvD_BwE',
             'https://www.udemy.com/course/nivel-3-integrarse-en-el-ecosistema/',
             'https://www.udemy.com/course/uso-profesional-de-tus-archivos-en-la-nube-con-google-drive/']


st.title("Sistema de recomendación de cursos online")

# Cargar imágenes
coursera_logo = Image.open("coursera-logo.png")
domestika_logo = Image.open("2.png")
udemy_logo = Image.open("fotor.png")





# Mostrar imágenes
col1, col2, col3 = st.columns(3)
with col1:
    st.image(coursera_logo, use_column_width=True)
    st.write("[Coursera](https://www.coursera.org/)")
with col2:
    st.image(domestika_logo, use_column_width=True)
    st.write("[Domestika](https://www.domestika.org/)")
with col3:
    st.image(udemy_logo, use_column_width=True)
    st.write("[Udemy](https://www.udemy.com/)")


# Sidebar
st.sidebar.subheader("Mi perfil:")


# Aquí podrías agregar más información sobre tu perfil, como tu nombre, correo electrónico, etc.
profile_image = Image.open("cute-afro-boy-mascot-cartoon-icon-kawaii-mascot-character-illustration-for-sticker-poster-animation-children-book-or-other-digital-and-print-product-vector-modified.png")
st.sidebar.image(profile_image, width=200, clamp=True)

st.sidebar.markdown("# Fer")

st.sidebar.subheader("Mis cursos")
st.sidebar.write("Aquí puedes ver una lista de los cursos que has hecho y has valorado")
# Aquí podrías cargar una lista de cursos que ya has hecho y valorado en otro archivo CSV

# Creamos el acordeón para Mis cursos
accordion = st.sidebar.expander("Mis cursos")

# Agregamos los cursos y links como elementos del acordeón
with accordion:
    for i in range(len(Cursosfer)):
        st.write("- " + f"[{Cursosfer[i]}]({links[i]})")


st.sidebar.subheader("Recomendaciones")
st.sidebar.write("Aquí puedes ver recomendaciones de cursos en línea")
# Aquí podrías agregar un modelo de recomendación que sugiera cursos basados en tus intereses y cursos anteriores

# Creamos el acordeón para Mis cursos
accordion = st.sidebar.expander("Mis recomendaciones")

# Agregamos los cursos y links como elementos del acordeón
with accordion:
    for i in range(len(recomendacion)):
        st.write("- " + f"[{recomendacion[i]}]({linksreco[i]})")


# Cargar archivo CSV
df1 = pd.read_csv("cursosp.csv")

columnas = ["Title", "Organization", "Web", "Course_actual_price", "Course_rating", "Course_certificate"]

# Filtrar datos según las columnas seleccionadas
df = df1.loc[:, columnas]





# Crear acordeón para seleccionar plataformas
with st.expander("Seleccionar plataformas"):
    domestika = st.checkbox("Domestika")
    coursera = st.checkbox("Coursera")
    udemy = st.checkbox("Udemy")

# Filtrar datos según las plataformas seleccionadas
if domestika:
    df = df[df["Web"] == "Domestika"]
if coursera:
    df = df[df["Web"] == "Coursera"]
if udemy:
    df = df[df["Web"] == "Udemy"]   

# Mostrar tabla filtrada
st.write(df)




