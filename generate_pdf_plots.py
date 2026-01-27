"""
Script to generate all chart figures in PDF format.

Run from project root:
    python generate_pdf_plots.py

Additional requirements:
    pip install kaleido  # To export Plotly figures
"""

import os
import plotly.graph_objects as go
import numpy as np
import pandas as pd
import plotly.express as px

# Create output folder
output_dir = "outputs/figures_pdf"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
    print(f"Folder '{output_dir}' created")

print("\n" + "="*60)
print("GENERATING PDF FIGURES")
print("="*60)

# =====================================================
# CONFIGURATION AND DATA LOADING
# =====================================================
escalaColor = 'viridis'
df = pd.read_csv('data/raw/taxonomy_complete.csv')

clasesBacteriasCarpetas = ['Abiotrophia', 'Acidovorax', 'Cyanibacteria', 'Megasphaera',
                           'Mycobacterium', 'Neisseria', 'Prevotella', 'Streptococcus', 'Veillonella']

# =====================================================
# CHART FUNCTIONS (adapted for export)
# =====================================================

def graficoBacteria(paises, frecuencia, no_especificado, titulo):
    """Generates world map of bacteria distribution."""
    fig = go.Figure()
    fig.add_trace(go.Choropleth(
        locations=paises,
        locationmode='country names',
        z=np.log(frecuencia),
        hovertemplate=['Country: <b>%s</b><br>Bacteria count: <b>%d</b> <extra></extra>' % (a, b) 
                       for a, b in zip(paises, frecuencia)],
        colorscale=escalaColor,
        reversescale=True,
        colorbar=dict(
            title='Color scale',
            tickvals=np.linspace(min(np.log(frecuencia).astype(int).tolist()), 
                                max(np.log(frecuencia).astype(int).tolist()), 10),
            ticktext=np.linspace(min(frecuencia.astype(int).tolist()), 
                                max(frecuencia).astype(int).tolist(), 10).astype(int),
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
        title=titulo,
        width=1200,
        height=700
    )
    fig.update_geos(projection_type="natural earth")
    return fig


def radarChart():
    """Generates radar chart with bacteria count."""
    df_temp1 = pd.DataFrame({
        'Col A': ['Abiotrophia', 'Cyanibacteria', 'Megasphaera',
                  'Mycobacterium', 'Neisseria', 'Prevotella', 'Veillonella', 
                  'Streptococcus', 'Acidovorax'],
        'Col B': [471, 68, 857, 9921, 4175, 9999, 4942, 9969, 4195]
    })
    
    fig = go.Figure()
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
                range=[0, max(df_temp1['Col B'])]
            ),
        ),
        showlegend=True,
        title="Count of bacteria in the DataFrame",
        width=800,
        height=700
    )
    return fig


def graphTaxonomy():
    """Generates taxonomy sunburst chart."""
    df_cleaned = df.dropna(subset=['Taxonomy:superkingdom', 'Taxonomy:phylum', 'Taxonomy:class',
                                    'Taxonomy:order', 'Taxonomy:family', 'Taxonomy:genus', 'Taxonomy:species'])
    
    fig = px.sunburst(df_cleaned,
                      path=['Taxonomy:superkingdom', 'Taxonomy:phylum', 'Taxonomy:class',
                            'Taxonomy:order', 'Taxonomy:family', 'Taxonomy:genus', 'Taxonomy:species'])
    
    fig.update_layout(
        title_text="Taxonomy distribution",
        title_font={'size': 24, 'family': 'Serif'},
        width=1000,
        height=800,
    )
    return fig


def graficoHost():
    """Generates pie chart of host distribution."""
    df_graph = pd.read_csv('data/raw/host_data.csv')
    host_counts = df_graph['Host'].value_counts()
    
    colores_personalizados = ["#a17fa9", "#35b779", '#9fa1c2', "#94bbc6", "#b5de2b"]
    
    fig = px.pie(host_counts, values=host_counts.values, names=host_counts.index, 
                 title='Hosts Distribution')
    fig.update_traces(marker=dict(colors=colores_personalizados))
    fig.update_layout(width=700, height=600)
    return fig


def treemapgraph():
    """Generates treemap chart of hosts by bacteria."""
    try:
        df_animals = pd.read_csv("data/processed/animals.csv")
        df_human = pd.read_csv('data/processed/human.csv')
        df_env = pd.read_csv('data/processed/environmental.csv')
        df_bio = pd.read_csv('data/processed/biology.csv')
        df_veg = pd.read_csv('data/processed/vegetation.csv')
        
        df_animals['host'] = 'animals'
        df_human['host'] = 'human'
        df_env['host'] = 'environmental'
        df_bio['host'] = 'biology'
        df_veg['host'] = 'vegetation'
        
        concatenated_df = pd.concat([df_animals, df_human, df_env, df_bio, df_veg], ignore_index=True)
        frecuencias2 = concatenated_df.groupby(['Class', 'host']).size().reset_index(name='frecuencia')
        
        fig = px.treemap(frecuencias2, path=['Class', 'host'],
                        values='frecuencia',
                        color_discrete_sequence=["#35b779", "#9fa1c2", "#b1de2a", "#94bbc6", 
                                                  "#b5de2b", "#fde725", "#6cc24a", "#a17fa9"])
        fig.update_layout(
            title="Host distribution by bacteria class",
            width=1000,
            height=800
        )
        return fig
    except Exception as e:
        print(f"  Error in treemap: {e}")
        return None


def graficoVarGen():
    """Generates genetic variation clustergram."""
    try:
        import dash_bio
        
        df_matrix = pd.read_csv('MAtrix_identity_abio.csv')
        df_matrix = df_matrix.fillna(100)
        
        fig = dash_bio.Clustergram(
            data=df_matrix,
            column_labels=list(df_matrix.columns[1:]),
            row_labels=list(df_matrix['Accession']),
            height=800,
            width=700,
            hidden_labels=['row', 'col']
        )
        return fig
    except Exception as e:
        print(f"  Error in clustergram (requires dash_bio): {e}")
        return None


def save_figure(fig, filename, output_dir):
    """Saves a figure in PDF format."""
    if fig is None:
        return False
    
    filepath = os.path.join(output_dir, filename)
    try:
        fig.write_image(filepath, format='pdf')
        print(f"  {filename}")
        return True
    except Exception as e:
        # Try with PNG if PDF fails
        try:
            filepath_png = filepath.replace('.pdf', '.png')
            fig.write_image(filepath_png, format='png', scale=2)
            print(f"  {filename.replace('.pdf', '.png')} (PNG fallback)")
            return True
        except Exception as e2:
            print(f"  Error saving {filename}: {e2}")
            return False


def prepararDatosSlider():
    """Prepares data for temporal slider charts."""
    from datetime import datetime
    
    # Date conversion
    formato_fecha = '%d-%b-%Y'
    tempfechas = []
    for i in df['Modification Date']:
        try:
            tempfechas.append(datetime.strptime(i, formato_fecha))
        except:
            tempfechas.append(None)
    
    dfCopia = df.copy()
    dfCopia['Modification Date'] = tempfechas
    dfCopia = dfCopia.dropna(subset=['Modification Date'])
    
    # Extract years
    tempaño = [fecha.year for fecha in dfCopia['Modification Date']]
    dfCopia['Modification Date'] = tempaño
    dfCopia.sort_values(by='Modification Date', inplace=True)
    
    return dfCopia


def graficoRS(dfData, titulo="Number of bacteria per year"):
    """Generates world map with year slider (static for PDF)."""
    # Filter unspecified data
    dfData = dfData[dfData['Country'] != 'No especificado']
    
    if len(dfData) == 0:
        return None
    
    # Group by year and country
    tempfa = []
    for year in sorted(dfData['Modification Date'].unique()):
        temp1 = dfData[dfData['Modification Date'] == year]
        countries, counts = np.unique(temp1['Country'], return_counts=True)
        years_col = np.full(len(countries), year)
        dftemp = pd.DataFrame({
            'year': years_col,
            'country': countries,
            'country frequency': counts
        })
        tempfa.append(dftemp)
    
    if not tempfa:
        return None
    
    tempfa_concat = pd.concat(tempfa)
    tempfa_concat.sort_values(['year', 'country'], ascending=[True, True], inplace=True)
    
    color_scale = px.colors.sequential.Viridis_r
    discrete_color_scale = [color_scale[i * len(color_scale) // 10] for i in range(10)]
    
    fig = px.choropleth(
        tempfa_concat,
        locations="country",
        color="country frequency",
        locationmode="country names",
        animation_frame="year",
        title=titulo,
        color_continuous_scale=discrete_color_scale,
        labels={'country frequency': 'Frequency'}
    )

    fig.update_layout(
        coloraxis_colorbar=dict(title='Color scale'),
        width=1200,
        height=800,
    )

    fig.update_geos(
        showland=True,
        landcolor='rgb(217, 217, 217)',
        showcountries=True,
        showcoastlines=True,
        projection_type='natural earth'
    )
    
    return fig


# =====================================================
# FIGURE GENERATION
# =====================================================

saved_count = 0
total_count = 0

# 1. RADAR CHART
print("\n[1/6] Generating Radar Chart...")
total_count += 1
fig = radarChart()
if save_figure(fig, "01_radar_chart_bacteria_count.pdf", output_dir):
    saved_count += 1

# 2. TAXONOMY SUNBURST
print("\n[2/6] Generating Taxonomy Sunburst...")
total_count += 1
fig = graphTaxonomy()
if save_figure(fig, "02_taxonomy_sunburst.pdf", output_dir):
    saved_count += 1

# 3. HOST DISTRIBUTION PIE CHART
print("\n[3/6] Generating Host Distribution...")
total_count += 1
try:
    fig = graficoHost()
    if save_figure(fig, "03_host_distribution_pie.pdf", output_dir):
        saved_count += 1
except Exception as e:
    print(f"  Error: {e}")

# 4. TREEMAP
print("\n[4/6] Generating Treemap...")
total_count += 1
fig = treemapgraph()
if fig and save_figure(fig, "04_treemap_host_bacteria.pdf", output_dir):
    saved_count += 1

# 5. WORLD MAPS - Global and by bacteria
print("\n[5/6] Generating World Maps...")

# Prepare global data
noEspecificado = df[df['Country'] != 'No especificado']
paisesGrafico, frecuenciaPaises = np.unique(noEspecificado['Country'], return_counts=True)
totalNoEspecificado = len(df[df['Country'] == 'No especificado'])

# Global map
total_count += 1
fig = graficoBacteria(paisesGrafico, frecuenciaPaises, totalNoEspecificado,
                      f'Total bacteria distribution<br>Without location: {totalNoEspecificado}')
if save_figure(fig, "05_map_global_bacteria.pdf", output_dir):
    saved_count += 1

# Maps by bacteria type
for i, bacteria in enumerate(clasesBacteriasCarpetas):
    total_count += 1
    try:
        tempBac = df[df['Class'] == bacteria]
        largoNE = len(tempBac[tempBac['Country'] == 'No especificado'])
        tempBac = tempBac[tempBac['Country'] != 'No especificado']
        
        if len(tempBac) > 0:
            tempPaises, tempConteo = np.unique(tempBac['Country'], return_counts=True)
            fig = graficoBacteria(tempPaises, tempConteo, largoNE,
                                  f'Bacteria: {bacteria}<br>Without location: {largoNE}')
            filename = f"05_map_{str(i+1).zfill(2)}_{bacteria.lower()}.pdf"
            if save_figure(fig, filename, output_dir):
                saved_count += 1
        else:
            print(f"  No data for {bacteria}")
    except Exception as e:
        print(f"  Error with {bacteria}: {e}")

# 6. SLIDER CHARTS (temporal evolution)
print("\n[6/6] Generating Slider Charts (temporal evolution)...")

# Prepare data with processed dates
dfSlider = prepararDatosSlider()

# Global chart with slider
total_count += 1
try:
    fig = graficoRS(dfSlider, "Global bacteria distribution by year")
    if fig and save_figure(fig, "06_slider_global.pdf", output_dir):
        saved_count += 1
except Exception as e:
    print(f"  Error with global slider: {e}")

# Slider charts by bacteria
for i, bacteria in enumerate(clasesBacteriasCarpetas):
    total_count += 1
    try:
        dfBacteria = dfSlider[dfSlider['Class'] == bacteria]
        if len(dfBacteria) > 0:
            fig = graficoRS(dfBacteria, f"Bacteria: {bacteria} - Distribution by year")
            if fig:
                filename = f"06_slider_{str(i+1).zfill(2)}_{bacteria.lower()}.pdf"
                if save_figure(fig, filename, output_dir):
                    saved_count += 1
            else:
                print(f"  Insufficient data for {bacteria}")
        else:
            print(f"  No data for {bacteria}")
    except Exception as e:
        print(f"  Error with slider {bacteria}: {e}")

# =====================================================
# SUMMARY
# =====================================================
print("\n" + "="*60)
print(f"SUMMARY: {saved_count}/{total_count} figures generated")
print(f"Location: {os.path.abspath(output_dir)}")
print("="*60)
