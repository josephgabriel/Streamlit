import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def main():
    st.set_page_config(layout="wide")
    st.columns
    st.title("Monitoramento de Evasão")
    st.write("Instituto Federal do Ceará — Campus Tianguá  ·  Semestre 2026.1")

    st.divider()

    col1, col2, col3, col4 = st.columns([1, 1, 1, 1])   

    with col1:
        st.markdown("""
        <div style="
            border: 5px solid #4682B4; 
            background-color: #000b00; 
            padding: 20px; 
            border-radius: 10px;
            text-align: left;">
            <h3 style='margin: 0; font-size: 24px;'>Baixo Risco</h3>
            <h2>0</h2>
            <p>Alunos</p>
        </div>
    """, unsafe_allow_html=True)
    
    with col2:
       st.markdown("""
        <div style="
            border: 5px solid #FFFF00; 
            background-color: #000b00; 
            padding: 20px; 
            border-radius: 10px;
            text-align: left;">
            <h3 style='margin: 0; font-size: 24px;'>Risco Moderado</h3>
            <h2>0</h2>
            <p>Alunos</p>
        </div>
    """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div style="
            border: 5px solid #FF0000; 
            background-color: #000b00; 
            padding: 20px; 
            border-radius: 10px;
            text-align: left;">
            <h3 style='margin: 0; font-size: 24px;'>Risco Alto</h3>
            <h2>0</h2>
            <p>Alunos</p>
        </div>
    """, unsafe_allow_html=True)

    with col4:
        st.markdown("""
        <div style="
            border: 5px solid #4CAF50; 
            background-color: #000b00; 
            padding: 20px; 
            border-radius: 10px;
            text-align: left;">
            <h3 style='margin: 0; font-size: 24px;'>Taxa de Evasão</h3>
            <h2>0%</h2>
            <p>Acumulado do semestre.</p>
        </div>
    """, unsafe_allow_html=True)
        
    st.divider()
    
    col_pie1, col_pie2 = st.columns(2)

    with col_pie1:
# gráfico de linha
      df = pd.DataFrame(
          np.random.randn(10, 2),
          columns=('x', 'y')
      )
      st.line_chart(df)

    with col_pie2:
# grfico de pizza
      df1 = pd.DataFrame({
      "Categoria": ["Baixo", "Moderado", "Alto"],
      "Valor": [10, 20, 30]
})  
  
      fig, ax = plt.subplots()
      fig.patch.set_facecolor('#2E8B57')
      ax.set_facecolor('white')
      cores = ['#4682B4', '#FFFF00', '#FF0000']
      ax.pie(df1["Valor"], labels=df1["Categoria"], autopct='%1.1f%%', colors= cores)
      
      with st.container():
          st.pyplot(fig)
          plt.close(fig)