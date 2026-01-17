
import plotly.graph_objects as go
import numpy as np
import pandas as pd
import geopandas as gpd
import plotly.express as px
import streamlit as st
import dash_bio

escalaColor='viridis'


df=pd.read_csv('datos_taxonomiaCompleta2.csv')


noEspecificado=df[df['Country']!='No especificado']
paisesGrafico, indice, frecuenciaPaises=np.unique(noEspecificado['Country'], return_counts=True,return_index=True)
totalNoEspecificado=len(df[df['Country']=='No especificado'])

datosGraficoGlobal=[paisesGrafico, frecuenciaPaises, totalNoEspecificado, f'Total bacterias <br>Bacteria without location: {totalNoEspecificado}']

# # Crear un array de 9x9 con todos los elementos a False
# array = np.full((10, 10), False)

# # Establecer True en la diagonal
# np.fill_diagonal(array, True)

clasesBacteriasCarpetas = ['Abiotrophia','Acidovorax', 'Cyanibacteria', 'Megasphaera','Mycobacterium','Neisseria','Prevotella', 'Streptococcus','Veillonella']
datosBacteriasGlobales=[datosGraficoGlobal]

for i in range(len(clasesBacteriasCarpetas)):
    tempBac=df[df['Class']==clasesBacteriasCarpetas[i]]
    largoNE=len(tempBac[tempBac['Country']=='No especificado'])
    tempBac=tempBac[tempBac['Country']!='No especificado']
    tempPaisesBacteria, tempConteo=np.unique(tempBac['Country'], return_counts=True)
    datosBacteriasGlobales.append([tempPaisesBacteria, tempConteo,largoNE, f'Bacteria: {clasesBacteriasCarpetas[i]} <br>Bacteria without location: {largoNE}'])

# visualizacion de los graficos 0,1,2,3,4,5,6,7,8,9
# globales,'Abiotrophia','Acidovorax', 'Cyanibacteria', 'Megasphaera','Mycobacterium','Neisseria','Prevotella', 'Streptococcus','Veillonella'
def graficoBacteria(i):
    fig =go.Figure()
    fig.add_trace(go.Choropleth(
        locations=i[0],
        locationmode='country names',
        z=np.log(i[1]),
        hovertemplate =['Country: <b>%s</b><br>Bacteria count : <b>%d</b> <extra></extra>' % (a, b) for a, b in zip(i[0], i[1])],
        colorscale=escalaColor,
        reversescale=True,
        colorbar=dict(
            title='Color scale',
            tickvals= np.linspace(min(np.log(i[1]).astype(int).tolist()), max(np.log(i[1]).astype(int).tolist()),10), 
            ticktext=np.linspace(min(i[1].astype(int).tolist()), max(i[1]).astype(int).tolist(),10).astype(int),
            ticks='outside',
        ),
        
    ))
    fig.update_layout(
            geo=dict(
                showland=True,
                landcolor='rgb(217, 217, 217)',
                showcountries=True,
                showcoastlines=True,
                projection_type='natural earth'
            ),
            title=i[3]
    )
    
    fig.update_geos(projection_type="natural earth")
    #3840 × 2160
    #fig.update_layout(width=3840, height=2160)
    # Mostrar el gráfico
    #ancho, alto=fig.layout.width, fig.layout.height
    #fig.update_layout(width=(3840/fig.layout.width), heigth= (2160/fig.layout.height))
    #fig.write_image("my_image.png", width=3840, height=2160, scale=1)
    return fig


#conversion de string fecha de modificacion 
from datetime import datetime
formato_fecha = '%d-%b-%Y'
tempfechas=[]
for i in df['Modification Date']:
    tempfechas.append(datetime.strptime(i, formato_fecha))


dfCopia=df.copy()
dfCopia['Modification Date'] = tempfechas


tempaño=[]
for i in range(len(dfCopia)):
    tempaño.append(dfCopia['Modification Date'][i].year)


dfCopia['Modification Date']=tempaño

dfCopia.sort_values(by='Modification Date', inplace=True)


def procesamientoDatosBacterias():
    dfs=[]
    for i in range(len(clasesBacteriasCarpetas)+1):
        if i ==0:
            tempdf=dfCopia[['Country', 'Modification Date', 'Class']]
            dfs.append(tempdf)
        else: 
            tempdf=dfCopia[dfCopia['Class']==clasesBacteriasCarpetas[i-1]]
            tempdf=tempdf[['Country', 'Modification Date', 'Class']]
            dfs.append(tempdf)
        
    return dfs
        
dataFramesGrafico=procesamientoDatosBacterias()

#No Especificado DfCopy
nedc=dataFramesGrafico[0][dataFramesGrafico[0]['Country']!='No especificado']
#nedc[nedc['Class']==clasesBacteriasCarpetas[1]]
cantidadNoEspecificadoRS=len(dataFramesGrafico[0][dataFramesGrafico[0]['Country']=='No especificado'])

tempfa=[]
for i in nedc['Modification Date'].unique():
    temp1=nedc[nedc['Modification Date']==i]
    temp2, temp3= np.unique(temp1['Country'], return_counts=True)
    temp4=np.full(len(temp2), i) # crea una lista de NxM y la rellena con un parametro
    dftemp=pd.DataFrame({'year': temp4,
                         'country': temp2,
                         'country frequency':temp3})
    tempfa.append(dftemp)
#clasesBacteriasCarpetas
def rsGraficoAños():
    datosrs=[]
    datosrsne=[]
    for j in clasesBacteriasCarpetas:
        tempfa=[]
        dfrs=dataFramesGrafico[0][dataFramesGrafico[0]['Class']==j]
        tempne=len(dfrs[dfrs['Country']=='No especificado'])
        dfrs=dfrs[dfrs['Country']!='No especificado']
        
        datosrsne.append(tempne)
        for i in dfrs['Modification Date'].unique():
            temp1=dfrs[dfrs['Modification Date']==i]
            temp2, temp3= np.unique(temp1['Country'], return_counts=True)
            temp4=np.full(len(temp2), i) # crea una lista de NxM y la rellena con un parametro
            dftemp=pd.DataFrame({'year': temp4,
                                'country': temp2,
                                'country frequency':temp3})
            tempfa.append(dftemp)
        datosrs.append(tempfa)
    return datosrs, datosrsne

datosRangeSlider, datosRangeSliderNE=rsGraficoAños()

datosRangeSlider.insert(0, tempfa)
datosRangeSliderNE.insert(0, cantidadNoEspecificadoRS)

def graficoRS(tempfa):
    tempfa=pd.concat(tempfa)
    tempfa.sort_values(['year', 'country'], ascending=[True, True], inplace=True)
    color_scale = px.colors.sequential.Viridis_r
    discrete_color_scale = [color_scale[i * len(color_scale) // 10] for i in range(10)]
    fig = px.choropleth(
        tempfa,
        locations="country",
        color="country frequency",
        locationmode="country names",
        animation_frame="year",
        title='Number of bacteria per year',
        color_continuous_scale=discrete_color_scale,
        labels={'frecuenciaPais': 'Frecuencia'}
    )

    fig.update_layout(coloraxis_colorbar=dict(title='Color scale'))
    fig.update_layout(width=800,
                    height=600,              
                    )

    fig.update_geos(showland=True,
            landcolor='rgb(217, 217, 217)',
            showcountries=True,
            showcoastlines=True,
            projection_type='natural earth')
    return fig

#graficoRS(datosRangeSlider[0])

df['Modification Date']= tempfechas

#graficoBacteria(datosBacteriasGlobales[0])

dfConcat=[]
for i in range(len(datosRangeSlider)):
    dfConcat.append(pd.concat(datosRangeSlider[i], axis=0))

        
def radarChart():
    df_temp1 = pd.DataFrame({'Col A': ['Abiotrophia', 'Cyanibacteria', 'Megasphaera',
                                  'Mycobacterium', 'Neisseria', 'Prevotella','Veillonella', 'Streptococcus',
                                  'Acidovorax'],
                        'Col B': [471, 68, 857, 9921, 4175, 9999,4942, 9969,4195]})

    fig = go.Figure()

    # Duplicate the first data point at the end for closed line
    r_values = df_temp1['Col B'].tolist() + [df_temp1['Col B'][0]]
    theta_values = df_temp1['Col A'].tolist() + [df_temp1['Col A'][0]]

    fig.add_trace(go.Scatterpolar(
        r=r_values,
        theta=theta_values,
        fill='toself',
        marker=dict(color='green'),
        name='Count'
    ))

    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, max(df_temp1['Col B'])]  # Ajusta el rango según tus datos
            ),
        ),
        showlegend=True,
        title="Count of bacterias in the DataFrame"
    )

    return fig

def graphTaxonomy():
    df_cleaned = df.dropna(subset=['Taxonomy:superkingdom', 'Taxonomy:phylum', 'Taxonomy:class',
                                    'Taxonomy:order', 'Taxonomy:family', 'Taxonomy:genus', 'Taxonomy:species'])

    fig = px.sunburst(df_cleaned,
                    path=['Taxonomy:superkingdom', 'Taxonomy:phylum', 'Taxonomy:class',
                            'Taxonomy:order', 'Taxonomy:family', 'Taxonomy:genus', 'Taxonomy:species'])

    fig.update_layout(title_text="Taxonomy distribution", 
                    title_font={'size': 24, 'family': 'Serif'},
                    width=1000, 
                    height=800,
                    )
    return fig

def graficoHost():
    df_graph=pd.read_csv('df_graph_host.csv')
    # Obtener la cuenta de cada host
    host_counts = df_graph['Host'].value_counts()

    # Crear una paleta de colores personalizada
    colores_personalizados = ["#a17fa9","#35b779", '#9fa1c2',  "#94bbc6",    "#b5de2b"]

    # Crear el gráfico de pastel con la paleta personalizada
    fig = px.pie(host_counts, values=host_counts.values, names=host_counts.index, title='Hosts Distribution')

    # Asignar la paleta de colores personalizada
    fig.update_traces(marker=dict(colors=colores_personalizados))

    # Actualizar el diseño del gráfico
    fig.update_layout(width=500, height=500)

    # Mostrar el gráfico
    return fig

def treemapgraph():
    df = pd.read_csv('Animals.csv')
    df1 = pd.read_csv('Human.csv')
    df2 = pd.read_csv('Environmental.csv')
    df3 = pd.read_csv('Biology.csv')
    df4 = pd.read_csv('Vegetation.csv')
    df['host'] = 'animals'
    df1['host'] = 'human'
    df2['host'] = 'ambiental'
    df3['host'] = 'biologico'
    df3['host'] = 'vegatacion'
    concatenated_df = pd.concat([df, df1, df2, df3, df4], ignore_index=True)

    frecuencias = concatenated_df.groupby(['Class', 'host','Isolation Source']).size().reset_index(name='frecuencia')
    frecuencias2 = concatenated_df.groupby(['Class', 'host']).size().reset_index(name='frecuencia')

    columnas_seleccionadas = ['Class', 'host','frecuencia']
    df_seleccionado = frecuencias2[columnas_seleccionadas]

    levels = ['Class', 'host']
    color_columns = ['Class', 'host']
    value_column = 'frecuencia'

    fig = px.treemap(df_seleccionado, path=['Class', 'host'],
                    values='frecuencia',
                    color_discrete_sequence=["#35b779", "#9fa1c2","#b1de2a", "#94bbc6", "#b5de2b","#fde725", "#6cc24a", "#a17fa9"])
    return fig


def graficoVarGen():

    df = pd.read_csv('MAtrix_identity_abio.csv')
    df2 = pd.read_csv('Animals.csv')
    df3 = pd.read_csv('Human.csv')
    #new_df.to_csv('nuevo_dataframe.csv', index=False)

    df3['Host'] = 'human'
    df2['Host'] = 'animals'
    concatenated_df = pd.concat([df2, df3], ignore_index=True)

    df = pd.read_csv('MAtrix_identity_abio.csv')
    df = df.fillna(100)
    def convertir_y_dividir(valor):
        try:
            return float(valor) / 100.0
        except ValueError:
            return np.nan  # Si no se puede convertir a float, devuelve NaN

    matriz_decimal = df.iloc[:, 1:].apply(lambda x: x.map(convertir_y_dividir))

    # Concatenar las columnas de títulos con la matriz convertida
    matriz_resultante = pd.concat([df.iloc[:, 0], matriz_decimal], axis=1)

    df_resultado = pd.merge(matriz_resultante, concatenated_df[['Accession', 'Host']], on='Accession', how='left')
    # df = pd.read_csv('MAtrix_identity_abio.csv')
    # df2 = pd.read_csv('Animals.csv')
    # df3 = pd.read_csv('Human.csv')

    #df = df.fillna(100)

    fig =dash_bio.Clustergram(
        data=df,
        column_labels=list(df_resultado.Host),
        row_labels=list(df_resultado.Host),
        height=800,
        width=700,
        hidden_labels=['row', 'col']
    )
    
    return fig