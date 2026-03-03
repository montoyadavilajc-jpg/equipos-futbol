import streamlit as st
import random
import pandas as pd

st.title("Generador Equipos Fútbol 5")

# Base de jugadores
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

confirmed_input = st.text_input(
    "Escribe los confirmados separados por coma:"
)

if st.button("Generar Equipos"):
    confirmed = [name.strip() for name in confirmed_input.split(",")]

    valid_players = []
    for name in confirmed:
        if name in players:
            ir = calculate_ir(players[name])
            valid_players.append((name, ir))

    if len(valid_players) != 12:
        st.warning("Debe haber exactamente 12 jugadores confirmados.")
    else:
        # Ordenar por IR
        valid_players.sort(key=lambda x: x[1], reverse=True)

        teams = {"Equipo A": [], "Equipo B": [], "Equipo C": []}
        order = ["Equipo A","Equipo B","Equipo C",
                 "Equipo C","Equipo B","Equipo A",
                 "Equipo A","Equipo B","Equipo C",
                 "Equipo C","Equipo B","Equipo A"]

        for i, player in enumerate(valid_players):
            teams[order[i]].append(player)

        for team, members in teams.items():
            avg = sum(p[1] for p in members) / 4
            st.subheader(team)
            for p in members:
                st.write(f"{p[0]} (IR {round(p[1],2)})")
            st.write(f"Promedio IR: {round(avg,2)}")
