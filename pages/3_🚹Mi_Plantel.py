import streamlit as st
import numpy as np
import pandas as pd
from etl import df, df_pass
from functions import player_passmap,graph_barras, heat_map

#----------------------

#MENU LATERAL
players = set(df_pass['player'].values)
player = st.sidebar.selectbox(
        "Jugador",
        players,
        0)


st.title("🚹 MI PLANTILLA")
#--- CONTENIDO INFO BASICA

df_player = df[df.player==player]

######## --------------- MAPA DE PASES
df_pass_player = df_pass[df_pass.player==player]
#df_pass_player = df_pass_player[df_pass_player.match_filter==rival]
player_passmap(df_pass_player,player,'USMP')

metricas = ['PASE','CONDUCCION','REGATE','TIRO','DUELO AEREO','PRESION','DUELO DEFENSIVO','PERDIDA'
            'DUELO BALON SUELTO','INTERCEPTACION','DESPEJE']
heat_map(df_player, metricas)

