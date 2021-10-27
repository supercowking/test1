# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 21:22:31 2021

@author: super_000
"""

import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

def radar_chart(val):  
    fruits=['Love','Joy','Peace','Patience','Kindness', 'Goodness', 'Faithfulness', 'Gentleness', 'Self-Control','Love']

    fig = go.Figure()

    fig.add_trace(go.Scatterpolar(
      r=[Love_val, Joy_val, Peace_val, Patience_val, Kindness_val, Goodness_val, Faithfulness_val, Gentleness_val, SelfCon_val, Love_val],
      mode = 'lines+text+markers',
      theta=fruits,
      fill='toself',
      fillcolor='rgba(0,255,127,0.4)',
      marker = dict(color = 'rgb(60,179,113)'),
      connectgaps=True
      
      ))
    

    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, val]
                )),
        showlegend=False
        )
    st.write(fig)
    #fig.show()
    
if __name__ == '__main__':
    val=10
    Love_val = st.slider('Love',0,10,1)
    Joy_val = st.slider('Joy',0,10,1)
    Peace_val = st.slider('Peace',0,10,1)
    Patience_val = st.slider('Patience',0,10,1)
    Kindness_val = st.slider('Kindness',0,10,1)
    Goodness_val = st.slider('Goodness',0,10,1)
    Faithfulness_val = st.slider('Faithfulness',0,10,1)
    Gentleness_val = st.slider('Gentleness',0,10,1)
    SelfCon_val = st.slider('Self-Control',0,10,1)
    radar_chart(val)
    