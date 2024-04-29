import streamlit as st
import time
from streamlit_option_menu import option_menu
from firebase.data_processing import get_data
from firebase.prepare_data import select_home_away
from firebase.main import predictions_results

# Inicializar la pagina
st.set_page_config(page_title='Sistema de predicción de fútbol', page_icon='⚽', layout='wide')

# url de la imagen para la seccion predicciones
url_imagen = "https://i.postimg.cc/Wprt7pwf/futbol.png"
video_path  = "./img/video-presentacion.mp4"

# Estilos css
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("./css/style.css")

# funcion principal
def main_streamlit():

    # sidebar con las opciones disponibles
    with st.sidebar:
        selected = option_menu(
            menu_title=None, 
             options=["Inicio", "Predicciones", "Contacto"], 
            icons=["house", "robot", "envelope"],
            menu_icon="cast",  
            default_index=0,  
            styles={
                    "icon": {"color": "#fbbc04", "font-size": "20px"},
                    "nav-link": {
                        "font-size": "25px",
                        "text-align": "left",
                        "margin": "5px 0px",
                        "--hover-color": "#0073ff",
                    },
                    "nav-link-selected": {"background-color": "#2d66ff"},
            },
        )

    # seccion inicio
    if selected == "Inicio":

        column1, column2 = st.columns([2, 2])
        with st.container():

            with column1:
                st.header('Potencia tu pasión por el fútbol con predicciones confiables')
                st.write('Plataforma que utiliza algoritmos de **:blue[aprendizaje automático]** y **:blue[análisis de datos]**, combinamos la emoción del fútbol con la precisión de los datos para ofrecerte predicciones que impulsan tu experiencia futbolística. Con un enfoque en la innovación y la fiabilidad, estamos aquí para llevarte más allá de los resultados y hacerte sentir parte del juego.')
                st.markdown("*Estamos en modo de prueba no es necesario presionar el boton de suscribirse*")
                contact_form = f"""
                    <form action="https://www.paypal.com/cgi-bin/webscr" method="post" target="_blank">
                        <input type="hidden" name="cmd" value="_s-xclick" />
                        <input type="hidden" name="hosted_button_id" value="QZ386H6QCYFZQ" />
                        <input type="hidden" name="currency_code" value="USD" />
                        <input type="image" src="https://www.paypalobjects.com/en_US/i/btn/btn_subscribe_LG.gif" border="0" name="submit" title="PayPal - The safer, easier way to pay online!" alt="Subscribe" />
                    </form>
                    """
                st.markdown(contact_form, unsafe_allow_html=True)

            with column2:
                st.video(video_path, format='video/mp4', start_time=0, loop=True)
    
    # seccion predicciones
    if selected == "Predicciones":
        
        if st.session_state.show_predictions:
            
            ligas_disponibles = ["Premier League", "LaLiga", "SerieA", "Bundesliga", "Eredivisie", "Ligue 1", "Jupiler Pro League", "Premiership"]
    
            col1, col2= st.columns([2,2])
            with st.container():
                with col1:
                    left_column, right_column= st.columns([1,3])
                    with st.container():
                        with left_column:
                            st.image(url_imagen, use_column_width=True)

                        with right_column:
                            st.title("Predicciones Deportivas") 

                    liga_seleccionada = st.selectbox("🌎 Selecciona una liga:", ligas_disponibles)

                    equipos = get_teams_for_league(liga_seleccionada)
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
                    <button type="submit">Enviar</button>
                </form>
                """
            
            st.markdown(form, unsafe_allow_html=True)

        with d_columna:
            st.write('Si quieres conocer más sobre el proyecto :blue[¡Contáctanos!]')

def get_teams_for_league(league):
    if league == "Premier League":
        return ['Burnley', 'Arsenal', 'Bournemouth', 'Brighton', 'Everton', 'Sheffield United', 'Newcastle', 'Brentford', 'Chelsea', 'Man United', "Nott'm Forest", 'Fulham', 'Liverpool', 'Wolves', 'Tottenham', 'Man City', 'Aston Villa', 'West Ham', 'Crystal Palace', 'Luton']
    elif league == "LaLiga":
        return ['Almeria', 'Sevilla', 'Sociedad', 'Las Palmas', 'Ath Bilbao', 'Celta',
            'Villarreal', 'Getafe', 'Cadiz', 'Ath Madrid', 'Mallorca', 'Valencia',
            'Osasuna', 'Girona', 'Barcelona', 'Betis', 'Alaves', 'Granada', 'Vallecano', 'Real Madrid']
    elif league == "SerieA":
        return ['Empoli', 'Frosinone', 'Genoa', 'Inter', 'Roma', 'Sassuolo', 'Lecce', 'Udinese',
            'Torino', 'Bologna', 'Monza', 'Milan', 'Verona', 'Fiorentina', 'Juventus',
            'Lazio', 'Napoli', 'Salernitana', 'Cagliari', 'Atalanta']
    elif league == "Bundesliga":
        return ['Werder Bremen', 'Augsburg', 'Hoffenheim', 'Leverkusen', 'Stuttgart',
            'Wolfsburg', 'Dortmund', 'Union Berlin', 'Ein Frankfurt', 'RB Leipzig',
            'Bochum', 'Darmstadt', 'FC Koln', 'Freiburg', 'Heidenheim', "M'gladbach",
            'Mainz', 'Bayern Munich', 'Hertha']
    elif league == "Eredivisie":
        return ['Volendam', 'PSV Eindhoven', 'Heerenveen', 'Ajax', 'Zwolle', 'Nijmegen',
            'AZ Alkmaar', 'Feyenoord', 'Almere City', 'Heracles', 'Excelsior', 'Vitesse',
            'For Sittard', 'Go Ahead Eagles', 'Utrecht', 'Sparta Rotterdam', 'Twente', 'Waalwijk']
    elif league == "Ligue 1":
        return ['Nice', 'Marseille', 'Paris SG', 'Brest', 'Clermont', 'Montpellier', 'Nantes',
            'Rennes', 'Strasbourg', 'Metz', 'Lyon', 'Toulouse', 'Lille', 'Le Havre',
            'Lorient', 'Reims', 'Monaco', 'Lens']
    elif league == "Jupiler Pro League":
        return ['St. Gilloise', 'Eupen', 'Charleroi', 'RWD Molenbeek', 'Antwerp', 'Gent',
            'Club Brugge', 'St Truiden', 'Standard', 'Genk', 'Cercle Brugge',
            'Oud-Heverlee Leuven', 'Anderlecht', 'Mechelen', 'Westerlo', 'Kortrijk']
    elif league == "Premiership":
        return ['Celtic', 'Dundee', 'Livingston', 'St Johnstone', 'Kilmarnock', 'Hibernian',
            'Rangers', 'Ross County', 'St Mirren', 'Aberdeen', 'Hearts', 'Motherwell']
    else:
        return st.warning('Seleccione un equipo disponible', icon="⚠️")

def get_file_league(league):
    if league == "Premier League":
        file = './data/premier_league_data.csv'
        df_data = get_data(file)
        return df_data
    elif league == "LaLiga":
        file = './data/laliga_data.csv'
        df_data = get_data(file)
        return df_data
    elif league == "SerieA":
        file = './data/seriea_data.csv'
        df_data = get_data(file)
        return df_data
    elif league == "Bundesliga":
        file = './data/bundesliga_data.csv'
        df_data = get_data(file)
        return df_data
    elif league == "Eredivisie":
        file = './data/eredivisie_data.csv'
        df_premier_legaue = get_data(file)
        return df_premier_legaue
    elif league == "Ligue 1":
        file = './data/ligue1_data.csv'
        df_data = get_data(file)
        return df_data
    elif league == "Jupiler Pro League":
        file = './data/liga_belgica_data.csv'
        df_data = get_data(file)
        return df_data
    elif league == "Premiership":
        file = './data/liga_escocia_data.csv'
        df_data = get_data(file)
        return df_data
    else:
        return st.warning('Seleccione una liga disponible', icon="⚠️")
    
if __name__ == "__main__":
    if 'show_predictions' not in st.session_state:
        st.session_state.show_predictions = True 
    main_streamlit()
