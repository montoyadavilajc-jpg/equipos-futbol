import streamlit as st
import random

st.set_page_config(page_title="Equipos Fútbol 5", layout="centered")

st.title("⚽ Generador Equipos Fútbol 5")

# -------------------------
# BASE DE JUGADORES
# -------------------------

players = {
    "JC": {"edad": 40, "talento": 4, "fisico": 4, "velocidad": 3},
    "Pantera": {"edad": 55, "talento": 3, "fisico": 2, "velocidad": 3},
    "Guillo": {"edad": 50, "talento": 4, "fisico": 4, "velocidad": 3},
    "Joaco Berrio": {"edad": 40, "talento": 3, "fisico": 3, "velocidad": 2},
    "Joaco Berrocal": {"edad": 37, "talento": 4, "fisico": 5, "velocidad": 4},
    "Nene Bayter": {"edad": 44, "talento": 4, "fisico": 4, "velocidad": 3},
    "Gabo Rodriguez": {"edad": 43, "talento": 4, "fisico": 5, "velocidad": 3},
    "Alfredo": {"edad": 47, "talento": 2, "fisico": 3, "velocidad": 3},
    "Nicola": {"edad": 50, "talento": 3, "fisico": 4, "velocidad": 3},
    "Pipe Sandoval": {"edad": 39, "talento": 4, "fisico": 4, "velocidad": 3},
    "Lucho": {"edad": 50, "talento": 3, "fisico": 3, "velocidad": 3},
    "Chalela": {"edad": 55, "talento": 3, "fisico": 3, "velocidad": 3},
}

# -------------------------
# FUNCIONES
# -------------------------

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

# -------------------------
# DROPDOWN MULTISELECT
# -------------------------

confirmed_players = st.multiselect(
    "Selecciona los 12 jugadores confirmados:",
    list(players.keys())
)

st.write(f"Jugadores seleccionados: {len(confirmed_players)} / 12")

# -------------------------
# GENERAR EQUIPOS
# -------------------------

if st.button("Generar Equipos"):

    if len(confirmed_players) != 12:
        st.error("⚠️ Debes seleccionar exactamente 12 jugadores.")
    else:

        # Calcular IR
        player_list = []
        for name in confirmed_players:
            ir = calculate_ir(players[name])
            player_list.append((name, ir))

        # Ordenar por IR
        player_list.sort(key=lambda x: x[1], reverse=True)

        # Distribución serpiente
        teams = {"Equipo A": [], "Equipo B": [], "Equipo C": []}
        order = ["Equipo A","Equipo B","Equipo C",
                 "Equipo C","Equipo B","Equipo A",
                 "Equipo A","Equipo B","Equipo C",
                 "Equipo C","Equipo B","Equipo A"]

        for i, player in enumerate(player_list):
            teams[order[i]].append(player)

        # Mostrar resultados
        for team, members in teams.items():
            avg = sum(p[1] for p in members) / 4
            st.subheader(team)
            for p in members:
                st.write(f"{p[0]} (IR {round(p[1],2)})")
            st.write(f"Promedio IR: {round(avg,2)}")
            st.markdown("---")
