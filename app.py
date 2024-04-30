import streamlit as st
import time
from streamlit_option_menu import option_menu
from firebase.data_processing import get_teams_for_league, get_file_league, get_leagues, get_data_excel
from firebase.prepare_data import select_home_away
from firebase.main import predictions_results

# Inicializar la pagina
st.set_page_config(
    page_title='Sistema de predicción de fútbol', 
    page_icon='⚽', 
    layout='wide',
)

# url de la imagen para la seccion predicciones
url_imagen = "https://i.postimg.cc/8cWxW26H/jugador-de-futbol.png"
video_path  = "./img/video-presentacion.mp4"

# Estilos css
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("./css/style.css")

# funcion principal
def main_streamlit():

    # sidebar con las opciones disponibles
    selected = option_menu(
        menu_title=None, 
        options=["Inicio", "Predicciones", "Contacto"], 
        icons=["house", "robot", "envelope"],
        menu_icon="cast",  
        default_index=0,  
        orientation="horizontal",
        styles={
            "icon": {"color": "green", "font-size": "22px"},
            "nav-link": {
                "font-size": "20px",
                "--hover-color": "#A7C957",
                "text-align": "center",
            },
            "nav-item": {"margin": "0px 7px"},
            "nav-link-selected": {"background-color": "#A7C957"},
        },
    )

    # seccion inicio
    if selected == "Inicio":

        column1, column2 = st.columns([2, 2])
        with st.container():

            with column1:
                st.header('Descubre tu pasión por el fútbol con predicciones confiables')
                st.write('Es una plataforma que utiliza algoritmos de **aprendizaje automático** y **análisis de datos**, combinamos la emoción del fútbol con la precisión de los datos para ofrecerte predicciones que impulsan tu experiencia futbolística. Con un enfoque en la innovación y la fiabilidad. ¡Hazte con el control del juego y sé el protagonista de cada partido!')
                st.markdown("*Estamos en modo de prueba no es necesario presionar el boton de suscribirse*")
                contact_form = f"""
                    <form action="https://www.paypal.com/cgi-bin/webscr" method="post" target="_blank">
                        <input type="hidden" name="cmd" value="_s-xclick" />
                        <input type="hidden" name="hosted_button_id" value="QZ386H6QCYFZQ" />
                        <input type="hidden" name="currency_code" value="USD" />
                        <input type="image" src="https://www.paypalobjects.com/en_US/i/btn/btn_subscribe_LG.gif" border="0" name="submit" title="PayPal - The safer, easier way to pay online!" alt="Subscribe" />
                    </form> """
                st.markdown(contact_form, unsafe_allow_html=True)

            with column2:
                st.video(video_path, format='video/mp4', start_time=0)
    
    # seccion predicciones
    if selected == "Predicciones":
        
        if st.session_state.show_predictions:
            
            df_data_excel = get_data_excel()
            ligas_disponibles = get_leagues(df_data_excel)
            # ligas_disponibles = ["Premier League", "LaLiga", "SerieA", "Bundesliga", "Eredivisie", "Ligue 1", "Jupiler Pro League", "Premiership"]
    
            col1, col2= st.columns([2,2])
            with st.container():
                with col1:
                    left_column, right_column= st.columns([1,3])
                    with st.container():
                        with left_column:
                            st.image(url_imagen, width=100)

                        with right_column:
                            st.title("Predicciones Deportivas") 

                    liga_seleccionada = st.selectbox("🌎 Selecciona una liga:", ligas_disponibles)

                    equipos = get_teams_for_league(liga_seleccionada, df_data_excel)
                    equipo_home = st.selectbox("🏠 Equipo local:", equipos)
                    equipo_away = st.selectbox("✈ Equipo visitante:", equipos)
                    
                    df = get_file_league(liga_seleccionada)

                    st.write("Trabajo desarrollado por: [@nicoleepalomino](https://www.instagram.com/nicolee.palomino/)")

            with col2:
                if st.button("🤖 Generar predicciones"):
                    if equipo_home != equipo_away:
                        progress_text = "Operación en progreso. Por favor, espere."
                        my_bar = st.progress(0, text=progress_text)

                        for percent_complete in range(100):
                            time.sleep(0.02)
                            my_bar.progress(percent_complete + 1, text=progress_text)
                        time.sleep(2)
                        my_bar.empty()

                        partidos_equipo_local, partidos_equipo_visitante = select_home_away(df, equipo_home, equipo_away)
                        
                        predictions = predictions_results(partidos_equipo_local, partidos_equipo_visitante, equipo_home, equipo_away)
                        victory_prediction, corner_prediction, corner_home_prediction, corner_away_prediction, yc_prediction, over_under_prediction, goals_home_prediction, goals_away_prediction, btts_prediction, prob_corners = predictions[0], predictions[1], predictions[2], predictions[3], predictions[4], predictions[5], predictions[6], predictions[7], predictions[8], predictions[9]
                        
                        st.subheader("**PREDICCIONES**")
                        st.write("Resultado:", victory_prediction)
                        st.write("Saques de Esquinas:", corner_prediction)
                        st.write(f"Saques de Esquinas ({equipo_home}):", corner_home_prediction)
                        st.write(f"Saques de Esquinas ({equipo_away}):", corner_away_prediction)
                        st.write("Tarjetas amarillas:", yc_prediction)
                        st.write("Over/Under:", over_under_prediction)
                        st.write(f"Goles ({equipo_home}):", goals_home_prediction)
                        st.write(f"Goles ({equipo_away}):", goals_away_prediction)
                        st.write("Ambos equipos marcan:", btts_prediction)
                        st.write(prob_corners)
                    else :
                        st.warning('Seleccione bien los equipos', icon='⚠️')
        else :
            st.write("Por favor, suscríbete para acceder a las sección de predicciones")
    
    if selected == "Contacto":
        st.subheader('Contacto')

        i_columna, d_columna = st.columns([2,2])
        with i_columna:
            form = """
                <form action="https://formspree.io/f/xeqynqwa" method="POST">
                    <input type="email" name="email" placeholder="Correo electrónico" required>
                    <textarea name="message" placeholder="Escribe tu mensaje aquí"></textarea>
                    <button type="submit">✉ Enviar</button>
                </form> """
            st.markdown(form, unsafe_allow_html=True)

        with d_columna:
            st.write('Si quieres conocer más sobre el proyecto :orange[¡Contáctanos!]')

if __name__ == "__main__":
    if 'show_predictions' not in st.session_state:
        st.session_state.show_predictions = True 
    main_streamlit()