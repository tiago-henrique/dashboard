import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout='wide')

col1, col2 = st.columns(2)
col3, col4 = st.columns(2)
col5, col6, col7 = st.columns(3)

df = pd.read_csv('gerenciamento.csv')

df_new = df[['equipamento', 'laboratorio', 'data']]

equipamentos = {
    1: 'AGITADOR DE PLACAS',
    2: 'AGITADOR MAGNÉTICO',
    3: 'VORTEX',
    4: 'ANALISADOR DE BIOQUÍMICA COBAS',
    5: 'ANALISADOR DE ELETRÓLITOS - INOLAB',
    6: 'ANALISADOR HEMATOLÓGICO - VETERINÁRIO',
    7: 'ANALISADOR DE ELETRÓLITOS - PRODIMOL',
    8: 'CITÔMETRO DE FLUXO',
    9: 'BALANÇA ANALÍTICA',
    10: 'BANHO HISTOLÓGICO',
    11: 'BANHO ULTRASSÔNICO',
    12: 'CENTRÍFUGA AXYGEN PLATE SPINNER',
    13: 'CENTRÍFUGA TIPO MICRO EPPENDORF',
    14: 'PICODROP',
    15: 'LAVADORA DE MICROPLACAS',
    16: 'LEITORA DE MICROPLACAS',
    17: 'MÁQUINA DE GELO',
    18: 'MICROSCÓPIO VERTICAL',
    19: 'MICRÓTOMO ROTATIVO',
    20: 'PHMETRO',
    21: 'QUBIT',
    22: 'REAL TIME',
    23: 'MAGPIX',
    24: 'TAPESTATION',
    25: 'FOTODOCUMENTADOR',
    26: 'MILLI-Q',
    27: 'MISEQ',
    28: 'PROFLEX'
}

laboratorios = {
    1: 'LAB. DE FISIOLOGIA',
    2: 'LAB. FISIOLOGIA EXPERIMENTAL',
    3: 'LAB. HABILIDADES CIRÚRGICAS',
    4: 'LAB. DE HABILIDADES E SIMULAÇÃO',
    5: 'LAB. DE IMUNOGENÉTICA',
    6: 'LITEX',
    7: 'LIMC',
    8: 'LIN',
    9: 'LMMBM',
    10: 'LAB. DE MICROBIOLOGIA',
    11: 'LAB. DE MICROCIRÚRGIA',
    12: 'LACIS',
    13: 'LAB. DE SEPSE',
    14: 'VIROLOGIA',
    15: 'NPBIN',
    16: 'UPGEM',
    17: 'LAB. DE FARMACOLOGIA DA INFLAMAÇÃO',
    18: 'CIN'
}

geladeiras = {
    1: 'Freezer -20',
    2: 'Freezer -80',
    3: 'Geladeira'
}

df_new['laboratorio'] = df_new['laboratorio'].map(laboratorios)
df_new['equipamento'] = df_new['equipamento'].map(equipamentos)

contar_utilizacao = df_new['equipamento'].value_counts().reset_index()
contar_utilizacao.columns = ['Equipamento', 'Frequência']


fig_freq = px.bar(contar_utilizacao, x='Frequência', y='Equipamento', orientation='h', color='Frequência', title='Uso de Equipamento por Laboratórios')
col1.plotly_chart(fig_freq, use_container_width=True)

contar_laboratorios = df_new['laboratorio'].value_counts().reset_index()
contar_laboratorios.columns = ['Laboratório', 'Frequência']

fig_lab = px.bar(contar_laboratorios, x='Laboratório', y='Frequência', color='Frequência', title='Laboratórios')
col2.plotly_chart(fig_lab, use_container_width=True)


#controle de temperatura

df_t = pd.read_csv('temperatura.csv')
df_ta = df_t[df_t['selecao'] == 1] 

df_ta_new = df_ta[['selecao', 'ambiente', 'temperatura_atual', 'temperatura_maxima', 'temperatura_minima', 'umidade', 'data']]
df_ta_new = df_ta_new.dropna(axis=0)

fig_temp = px.line(df_ta_new, x='data', y=['temperatura_atual', 'temperatura_maxima', 'temperatura_minima'], markers=True, title='Gráfico de Temperatura Ambiente')
#st.plotly_chart(fig_temp)
col3.plotly_chart(fig_temp, user_container_width=True)


df_te = df_t[df_t['selecao'] == 2]
df_te_new = df_t[['tipo_equipamento', 'temperatura_atual_equipamento', 'temperatura_maxima_equipamento', 'temperatura_m_nima_equipamento']]
#df_te_new = df_te_new.dropna(axis=0)
df_te_new.columns = ['Equipamento', 'Temperatura Atual', 'Temperatura Máxima', 'Temperatura Mínima']
#col4.write(df_te_new)


freezer_80 = df_te_new[df_te_new['Equipamento'] == 2]
col5.write("Freezer -80")
col5.write(freezer_80)

geladeira = df_te_new[df_te_new['Equipamento'] == 3]
col6.write('Geladeira')
col6.write(geladeira)

freezer_20 = df_te_new[df_te_new['Equipamento'] == 1]
col7.write('Freezer -20')
col7.write(freezer_20)
#fig_tem_eq = px.bar(df_te_new, x='tipo_equipamento', y=['temperatura_atual_equipamento','temperatura_maxima_equipamento','temperatura_m_nima_equipamento'], title='Gráfico de Temperatura Equipamentos')
#st.plotly_chart(fig_tem_eq)

#st.write(df_te)
