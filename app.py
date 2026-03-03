import streamlit as st

st.set_page_config(page_title="Equipos Fútbol 5", layout="centered")
st.title("⚽ Generador Equipos Fútbol 5")

# -------------------------------------------------
# BASE INICIAL COMPLETA (TODOS LOS HABITUALES)
# -------------------------------------------------

if "players" not in st.session_state:
    st.session_state.players = {
        "JC": {"edad": 40, "talento": 4, "fisico": 4, "velocidad": 3},
        "Joaco Berrocal": {"edad": 37, "talento": 4, "fisico": 5, "velocidad": 4},
        "Nene Bayter": {"edad": 44, "talento": 4, "fisico": 4, "velocidad": 3},
        "Gabo Rodriguez": {"edad": 43, "talento": 4, "fisico": 5, "velocidad": 3},
        "Cheque": {"edad": 44, "talento": 5, "fisico": 3, "velocidad": 3},
        "Pipe Sandoval": {"edad": 39, "talento": 4, "fisico": 4, "velocidad": 3},
        "Alfredo": {"edad": 47, "talento": 3, "fisico": 3, "velocidad": 3},
        "Pantera": {"edad": 55, "talento": 3, "fisico": 2, "velocidad": 3},
        "Guillo": {"edad": 50, "talento": 4, "fisico": 4, "velocidad": 3},
        "Nicola": {"edad": 50, "talento": 3, "fisico": 4, "velocidad": 3},
        "Abraham": {"edad": 40, "talento": 4, "fisico": 3, "velocidad": 3},
        "Chalela": {"edad": 55, "talento": 3, "fisico": 3, "velocidad": 3},
        "Gabo Abidaud": {"edad": 38, "talento": 3, "fisico": 3, "velocidad": 3},
        "Humberto": {"edad": 50, "talento": 2, "fisico": 3, "velocidad": 3},
        "Lucho": {"edad": 50, "talento": 3, "fisico": 3, "velocidad": 3},
        "Joaco Berrio": {"edad": 40, "talento": 3, "fisico": 3, "velocidad": 2},
        "Pier": {"edad": 38, "talento": 3, "fisico": 3, "velocidad": 2},
        "Perna": {"edad": 43, "talento": 3, "fisico": 2, "velocidad": 2},
        "Juanchi Velez": {"edad": 50, "talento": 3, "fisico": 3, "velocidad": 3},
    }

players = st.session_state.players

# -------------------------------------------------
# AGREGAR NUEVO JUGADOR
# -------------------------------------------------

st.sidebar.header("➕ Agregar nuevo jugador")

new_name = st.sidebar.text_input("Nombre")
new_age = st.sidebar.number_input("Edad", 18, 70, 35)
new_talent = st.sidebar.slider("Talento", 1, 5, 3)
new_fisico = st.sidebar.slider("Estado físico", 1, 5, 3)
new_velocidad = st.sidebar.slider("Velocidad", 1, 5, 3)

if st.sidebar.button("Agregar jugador"):
    if new_name.strip() != "":
        players[new_name.strip()] = {
            "edad": new_age,
            "talento": new_talent,
            "fisico": new_fisico,
            "velocidad": new_velocidad,
        }
        st.sidebar.success(f"{new_name} agregado correctamente")

# -------------------------------------------------
# FUNCIONES
# -------------------------------------------------

def age_adjustment(age):
    if 36 <= age <= 42:
        return 0.97
    elif 43 <= age <= 50:
        return 0.94
    elif age > 50:
        return 0.90
    return 1

def calculate_ir(data):
    base = (
        0.4 * data["talento"]
        + 0.35 * data["fisico"]
        + 0.25 * data["velocidad"]
    )
    return base * age_adjustment(data["edad"])

# -------------------------------------------------
# SELECCIÓN DE JUGADORES
# -------------------------------------------------

st.subheader("Selecciona los jugadores confirmados")

confirmed_players = st.multiselect(
    "Jugadores disponibles:",
    sorted(players.keys())
)

st.write(f"Seleccionados: {len(confirmed_players)} jugadores")

# -------------------------------------------------
# GENERAR EQUIPOS
# -------------------------------------------------

if st.button("Generar Equipos"):

    total = len(confirmed_players)

    if total not in [8, 12]:
        st.error("⚠️ Solo puedes generar equipos con 8 jugadores (2 equipos) o 12 jugadores (3 equipos).")
    else:

        player_list = []
        for name in confirmed_players:
            ir = calculate_ir(players[name])
            player_list.append((name, ir))

        player_list.sort(key=lambda x: x[1], reverse=True)

        if total == 8:
            teams = {"Equipo A": [], "Equipo B": []}
            order = ["Equipo A","Equipo B",
                     "Equipo B","Equipo A",
                     "Equipo A","Equipo B",
                     "Equipo B","Equipo A"]

        else:  # 12 jugadores
            teams = {"Equipo A": [], "Equipo B": [], "Equipo C": []}
            order = ["Equipo A","Equipo B","Equipo C",
                     "Equipo C","Equipo B","Equipo A",
                     "Equipo A","Equipo B","Equipo C",
                     "Equipo C","Equipo B","Equipo A"]

        for i, player in enumerate(player_list):
            teams[order[i]].append(player)

        st.markdown("---")

        for team, members in teams.items():
            st.subheader(team)
            for p in members:
                st.write(p[0])
            st.markdown("---")
