#COMANDO A EJECUTAR ANTES DE TRABAJAR EN EL PROYECTO SCREAMLIT
#pip show streamlit saber si está instalada
#streamlit run Prácticas.py

#git init Inicializar el repositorio:
#git branch -M main Asegurar la rama principal main:
#git remote add origingit remote add origin <URL del repositorio> Agregar el repositorio remoto: Vincular con tu GitHub:
#git add . Agregar todos los archivos al área de preparación:
#git commit -m "Sincronizando proyecto con GitHub"
#git push -u origin main --force
#SUBIR EL CÓDIGO A GITHUB DESDE LA TERMINAL DE VISUAL STUDIO CODE
#git init
#git branch -M main
#git remote add origin <URL del repositorio> Agregar el repositorio remoto: Vincular con tu GitHub:
#git add .
#git commit -m "Sincronizando app.py"
#git push -u origin main --force


import streamlit as st
st.title("CONSULTA LOCADORES SBC")
Equipo_locadores = {
    "Centro de contacto": ["Fiorella Silva", "Katherine Romero", "Sanndy Urbina"],
    "Gestión": ["Jhon Hilario", "Claudia Vicente"],
    "Presencial": ["Christian Gago"],
    "Gestión": ["Eliana Carrasco", "María Chapoñan", "Lourdes Collazos","Carmen Bautista"]
}
Equipo = st.selectbox("Seleccione su equipo", options=list(Equipo_locadores.keys()))
locadores_disponibles = Equipo_locadores[Equipo]
locador_seleccionado = st.selectbox("Seleccione el locador", options=locadores_disponibles)



