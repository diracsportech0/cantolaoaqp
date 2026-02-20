import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from mplsoccer import (VerticalPitch, Pitch, create_transparent_cmap,
                       FontManager, arrowhead_marker, Sbopen)

#from Home_page import name_club, id_club
from etl import df, df_pass #df_tipo1, df_tipo2
from functions import barras_apiladas, tipo_tiros_goles, mostrar_tablas_zonas, mapa_pases


colA, colB, colC = st.columns([5, 6, 2])
with colA:st.title('🎖️ MI CLUB')
with colB:pass
with colC:st.image('logo-piad.png', use_column_width=True)
#----------------------
#st.title(f'⚽ {name_club}')
#df = df[df['etapa'] != 'provincial'] #estamos obviando los partidos de la provincial


#ETAPA DE JUEGO
ataque = ['Ataque', 'Tran. Defensa - Ataque']
defensa= ['Defensa', 'Tran. Ataque - Defensa']

#------------ 1. MENU LATERAL
menu_miclub = ['Informe de partido','Informe acumulado']
choice2 = st.sidebar.radio("Submenú - Miclub", menu_miclub, 0)

if choice2 == 'Informe de partido':

    etapas_juego = ['Ataque', 'Defensa','Pases']

    menu_subinforme = st.sidebar.selectbox(
        "Etapa de juego",
        etapas_juego,
        0)

    if menu_subinforme == 'Ataque':
        col1, col2 = st.columns(2)
        with col1:
            #st.subheader("Gráfico Ataque")
            fig1, ax1 = plt.subplots()
            ax1.plot([1, 2, 3], [10, 20, 10])
            barras_apiladas(df, 'Event', ataque,'output', "Resumen por fase")
        with col2:
            tipo_tiros_goles(df,'Ocasión')
        
        mostrar_tablas_zonas(df, ataque)

    if menu_subinforme == 'Defensa':
        col1, col2 = st.columns(2)
        with col1:
            #st.subheader("Gráfico Ataque")
            fig1, ax1 = plt.subplots()
            ax1.plot([1, 2, 3], [10, 20, 10])
            barras_apiladas(df, 'Event', defensa,'output', "Resumen por fase")
        with col2:
            tipo_tiros_goles(df,'Ocasión rival')
        
        mostrar_tablas_zonas(df, defensa)
    
    if menu_subinforme == 'Pases':
        col1n, col2n = st.columns(2)
        with col1n:
            mapa_pases(df_pass[df_pass.zone=='1er tercio'],'CORRECTO','USMP')
        with col2n:
            mapa_pases(df_pass[df_pass.zone=='1er tercio'],'ERRONEO','USMP')
        
        col3n, col4n = st.columns(2)
        with col3n:
            mapa_pases(df_pass[df_pass.zone=='2do tercio'],'CORRECTO','USMP')
        with col4n:
            mapa_pases(df_pass[df_pass.zone=='2do tercio'],'ERRONEO','USMP')
        
        col5n, col6n = st.columns(2)
        with col5n:
            mapa_pases(df_pass[df_pass.zone=='3er tercio'],'CORRECTO','USMP')
        with col6n:
            mapa_pases(df_pass[df_pass.zone=='3er tercio'],'ERRONEO','USMP')
        

if choice2 == 'Informe acumulado':
    st.write("NO DISPONIBLE")