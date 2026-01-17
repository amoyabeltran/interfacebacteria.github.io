"""
Para que funcione el código debe estar junto con el dataset en la misma carpeta

Se ejecuta con el siguiente comando en consola "streamlit run app.py"

"""


import plotly.graph_objects as go
import numpy as np
import pandas as pd
import geopandas as gpd
import plotly.express as px
import streamlit as st
from funcionesYDatos import *




# Crear un selectbox con dos opciones
seleccion_principal = st.sidebar.selectbox("Menu", ["Home",'Geo-localization', 'Taxonomy', 'Host', 'Genetic Variation', 'Authors'])
if seleccion_principal=="Home":
    st.markdown("""
                    <style>body {text-align: justify}</style>
            

        # Exploration and Visualization Interface for Public Database Information Regarding Pathogenic Bacteria in the Pulmonary Environment

        Using this exploration and visualization interface, we utilize Data Science to uncover key insights within the healthcare landscape, particularly related to the sequences and metadata of pathogenic bacteria.
        Data science provides valuable insights into the large amount of internet data about individuals, institutions, and regulatory bodies, providing valuable understanding for decision-makers and healthcare professionals. The COVID-19 pandemic demonstrated its potential, establish essential evidence during emergencies. It emphasized the significance of data-driven approaches in dealing with complex and evolving public health crises, particularly those related to pathogens [1](https://datascience.codata.org/articles/10.5334/dsj-2023-041), [2](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7393550/).
        By integrating sequence data and associating information, our platform provides a comprehensive understanding of pathogens present in the pulmonary environment. Through sophisticated visualization techniques, users can navigate and interpret complex metadata, gaining valuable perspectives on the intricate interplay between pathogens and health. This approach not only contributes to advancing scientific knowledge but also holds immense potential for shaping targeted strategies in the fight against infectious diseases.
        We selected nine bacterial genera that are reported in the literature as associated with the pathogenesis of the pulmonary environment. These include:
     """, unsafe_allow_html=True)
    st.markdown('''
        - ***Abiotrophia***: This genus contains four species. In humans, Abiotrophia defectiva has been found in the oral cavity, urogenital tract, and intestinal tract. More recently, representative organisms of this group have been found in samples associated with lung cancer [3](https://www.hindawi.com/journals/ecam/2021/6522191/)
            ''')
    st.markdown('''
        - ***Granulicatella***: Members of this genus are gram-positive bacteria, which are part of the normal microbiota of the oral cavity and intestinal and genitourinary tract and have been found to be responsible for severe infections, especially in patients with predisposing factors. Evidence of extravascular infections by G. adiacens is limited, with the most frequent anatomical locations being joints, ocular orbit, and lungs, among others, or after joint prosthetic procedures. This case is novel because G. adiacens in an immunocompetent patient is unusual in the medical context [4](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9785600/).
            ''')
    left_co, cent_co3, last_co=st.columns(3)
    with cent_co3:
        st.image('https://www.researchgate.net/profile/Hye-Jeong-2/publication/268411835/figure/fig1/AS:648213749039104@1531557609483/Gram-stain-of-Granulicatella-adiacens-isolated-from-the-case-Smears-were-prepared.png')
        st.caption('Figure 1. Gram stain of Granulicatella adiacens isolated from a septicemia case [5](https://www.researchgate.net/profile/Hye-Jeong-2/publication/268411835/figure/fig1/AS:648213749039104@1531557609483/Gram-stain-of-Granulicatella-adiacens-isolated-from-the-case-Smears-were-prepared.png)')
    st.markdown('''
        - Acidovorax: This genus has been classified as gram-negative beta-proteobacteria, and establishes symbiotic relationships with many plants. Acidovorax is classified as a biotropic pathogen. Recently, a study discovered the presence of bacteria from the Acidovorax genus in both tumor and non-neoplastic lung tissues. This was observed in a group of 50 Japanese patients.The findings indicate that Acidovorax could serve as a valuable biomarker in the detection of lung cancer [6](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9250845/),[7](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10482636/).        
            ''')
    st.markdown('''
        - ***Mycobacterium***: This genus includes highly virulent pathogens such as Mycobacterium tuberculosis and leprae. However, the majority of species within this genus are microorganisms found in the environment. The clinical importance of biofilms formed by mycobacterial microorganisms has been described for many chronic diseases, especially lung [8](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9925856/). 
            ''')
    left_co, cent_co2, last_co=st.columns(3)
    with cent_co2:
        st.image('https://d2jx2rerrg6sh3.cloudfront.net/image-handler/ts/20190916120106/ri/650/picture/2019/9/%40shutterstock_393854935.jpg')
        st.caption('Figure 2. Tuberculosis bacillus in the lungs. Tuberculosis is caused by the bacterium Mycobacterium tuberculosis. Image Credit: Juan Gaertner / Shutterstock. [link](https://www.news-medical.net/health/History-of-Tuberculosis.aspx)')
    st.markdown('''
        - ***Megasphaera***: Is a genus that includes a group of anaerobic bacteria with distinct spherical cell shapes. These microorganisms have important roles in different ecological niches, such as the human gastrointestinal tract and other low-oxygen environments. In healthcare and microbiology, Megasphaera species have been associated with a range of physiological processes and pathogenic conditions. Recently, they have also been linked to lung cancer [9](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10324390/).
            ''')
    st.markdown('''
        - ***Streptococcus***: A group of Gram-positive bacteria, is crucial in medicine and industry. They are part of the normal microbial flora of animals and humans and can cause diseases ranging from subacute to chronic. Streptococci are essential in industrial and dairy processes and as pollution indicators. In recent years, increasing attention has been given to streptococcal species diversity, partly because of advances in understanding the pathogenetic and epidemiologic significante. Some importants members include S. mutans and S sanguis (involved in dental caries), “S. milleri” (associated with suppurative infections in children and adults), and S. pneumoniae (worldwide contributor to illness and death across all age demographics, with youngsters and the elderly being particularly vulnerable). [10](https://www.ncbi.nlm.nih.gov/books/NBK7611/) 
        ''')
    left_co, cent_co,last_co = st.columns(3)
    with cent_co:
        st.image('https://maidenlab.zoo.ox.ac.uk/sites/default/files/styles/standard_desktop/public/2021-03/screenshot_2021-03-10_at_17.01.45.png?itok=yx3eUFRf')
        st.caption('Figure 3. Streptococcus pneumoniae seen by electron micrograph.[link](https://maidenlab.zoo.ox.ac.uk/history-and-biology-istreptococcus-pneumoniaei)')
    st.markdown('''
        - ***Neisseria***: Is a Gram-negative genus that currently includes over 30 species. These species demonstrate remarkable adaptation to their mammalian host and possess distinct phenotypes. Only two species are considered strict human pathogens. *N gonorrhoeae* causes the sexually transmitted disease gonorrhea, while *N. meningitidis* is responsible for meningitis and sepsis. Unusual infections in the respiratory tract and lungs have been reported in literature, specifically associated with species such as N. Bacilliformis, N. flavescens, N. lactamica, among others [11](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7168603/).
            ''')
    st.markdown('''
        - ***Veillonella***: Are anaerobic bacteria considered part of the normal flora of the oral cavity, upper respiratory tract, small intestines, and vagina. In humans, some Veillonella species have been reported as potential respiratory pathogens. For example, Veillonella parvula has been associated with children with cystic fibrosis [12](https://www.sciencedirect.com/science/article/pii/S1201971208000957).
        ''')
    left_co, cent_co1,last_co = st.columns(3)
    with cent_co1:
        st.image('https://cdn.dsmz.de/images/strain/17174/EM_DSM_2008_1.jpg')
        st.caption('Figure 4. Electron microscopic image of Veillonella parvula.[link](https://bacdive.dsmz.de/strain/17174)')
    st.markdown('''
        - ***Prevotella***: Is a genus of anaerobic gram-negative bacteria that consists of over 50 species. Many of these are found in the human microbiota as commensals in the upper respiratory tract and genitourinary system. From a clinical point of view, the species of interest is P. oris, which causes serious pleuropulmonary infections [13](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10336306/) and  P. melanogenica may also cause systemic diseases such as aspiration pneumonia, according to recent studies [14](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10272425/). 
            ''')
    


    st.markdown('''### Data collection:
                
To conduct an integrated analysis, we utilize information associated with 16S rRNA sequences retrieved from genetic sequence databases in NCBI repositories. Using Entrez direct tools, we download Genbank files [https://www.ncbi.nlm.nih.gov/genbank/samplerecord/] reported for selected bacteria. Metadata pertaining to each sequence, such as ID, host, taxonomy, date, organism, country, isolation source, and others, were collected using in-house developed scripts based on Biopython libraries.
                

### Results overview:
                 
A total of 44,639  files were downloaded and processed classified in the different groups of selected bacteria.
 ''')
    st.plotly_chart(radarChart())

elif seleccion_principal == "Geo-localization":
    st.markdown('''
                <style>body {text-align: justify}</style>
                
                # Geo-localization
                Global cooperative networks and the exchange of data are essential for worldwide identification of pathogens, significantly enhancing our comprehension of contagious illnesses and our capacity to identify, track, and react to newly emerging infections. The period after the COVID-19 pandemic has led to rapid progress in the field of pathogen discovery. The availability of a wide range of samples from different geographical regions has become essential for investigating the genetic diversity of pathogens. This access allows for real-time tracking and surveillance of the spread of pathogens, comprehension of the dynamics of disease transmission, identification of possible reservoirs or vectors, and the creation of focused interventions to manage and avoid epidemics [15]().
                To understand the distribution of the sequences reported associated with bacteria of interest, we explore the geolocalization of the data. Here, we used latitude and longitude from each country reported to map sequences in a geographic context using geopandas and plotly libraries for an interactive view. 
    ''', unsafe_allow_html=True)
    opciones_secundarias = ["Global data", "Bacteria: Abiotrophia", "Bacteria: Acidovorax", "Bacteria: Cyanibacteria", "Bacteria: Megasphaera",
                            "Bacteria: Mycobacterium", "Bacteria: Neisseria", "Bacteria: Prevotella", "Bacteria: Streptococcus", "Bacteria: Veillonella"]
    seleccion_secundaria = st.sidebar.selectbox("Selecciona una opción secundaria", opciones_secundarias)

   # Mostrar el gráfico según la selección
    if seleccion_secundaria == "Global data":
        st.markdown('### World map')
        st.plotly_chart(graficoBacteria(datosBacteriasGlobales[0]), use_container_width=True)
        st.markdown('### Graph with slider')
        #st.markdown('### World map with slider')
        st.plotly_chart(graficoRS(datosRangeSlider[0]), use_container_width=True)
        
        left_coll, right_coll=st.columns(2, gap='medium')
        with left_coll:
            st.markdown('### This is the data used to create the world maps')
            st.dataframe(dfConcat[0], use_container_width=True)
        with right_coll:
            st.markdown('### Bacteria frequency per country')
            tempdfff=pd.read_csv('GeographyData.csv')
            st.dataframe(tempdfff, use_container_width=True)
    elif seleccion_secundaria == "Bacteria: Abiotrophia":
        st.markdown('### World map')
        st.plotly_chart(graficoBacteria(datosBacteriasGlobales[1]), use_container_width=True)
        st.markdown('### Graph with slider')
        st.plotly_chart(graficoRS(datosRangeSlider[1]), use_container_width=True)
        st.markdown('### This is the data used to create the world maps')
        st.dataframe(dfConcat[1], use_container_width=True)
    elif seleccion_secundaria == "Bacteria: Acidovorax":
        st.markdown('### World map')
        st.plotly_chart(graficoBacteria(datosBacteriasGlobales[2]), use_container_width=True)
        st.markdown('### Graph with slider')
        st.plotly_chart(graficoRS(datosRangeSlider[2]), use_container_width=True)
        st.markdown('### This is the data used to create the world maps')
        st.dataframe(dfConcat[2], use_container_width=True)
    elif seleccion_secundaria == "Bacteria: Cyanibacteria":
        st.markdown('### Gráfico mapa mundi')
        st.plotly_chart(graficoBacteria(datosBacteriasGlobales[3]), use_container_width=True)
        st.markdown('### Graph with slider')
        st.plotly_chart(graficoRS(datosRangeSlider[3]), use_container_width=True)
        st.markdown('### This is the data used to create the world maps')
        st.dataframe(dfConcat[3], use_container_width=True)
    elif seleccion_secundaria == "Bacteria: Megasphaera":
        st.markdown('### Gráfico mapa mundi')
        st.plotly_chart(graficoBacteria(datosBacteriasGlobales[4]), use_container_width=True)
        st.markdown('### Graph with slider')
        st.plotly_chart(graficoRS(datosRangeSlider[4]), use_container_width=True)
        st.markdown('### This is the data used to create the world maps')
        st.dataframe(dfConcat[4], use_container_width=True)
    elif seleccion_secundaria == "Bacteria: Mycobacterium":
        st.markdown('### Gráfico mapa mundi')
        st.plotly_chart(graficoBacteria(datosBacteriasGlobales[5]), use_container_width=True)
        st.markdown('### Graph with slider')
        st.plotly_chart(graficoRS(datosRangeSlider[5]), use_container_width=True)
        st.markdown('### This is the data used to create the world maps')
        st.dataframe(dfConcat[5], use_container_width=True)
    elif seleccion_secundaria == "Bacteria: Neisseria":
        st.markdown('### Gráfico mapa mundi')
        st.plotly_chart(graficoBacteria(datosBacteriasGlobales[6]), use_container_width=True)
        st.markdown('### Graph with slider')
        st.plotly_chart(graficoRS(datosRangeSlider[6]), use_container_width=True)
        st.markdown('### This is the data used to create the world maps')
        st.dataframe(dfConcat[6], use_container_width=True)
    elif seleccion_secundaria == "Bacteria: Prevotella":
        st.markdown('### Gráfico mapa mundi')
        st.plotly_chart(graficoBacteria(datosBacteriasGlobales[7]), use_container_width=True)
        st.markdown('### Graph with slider')
        st.plotly_chart(graficoRS(datosRangeSlider[7]), use_container_width=True)
        st.markdown('### This is the data used to create the world maps')
        st.dataframe(dfConcat[7], use_container_width=True)
    elif seleccion_secundaria == "Bacteria: Streptococcus":
        st.markdown('### Gráfico mapa mundi')
        st.plotly_chart(graficoBacteria(datosBacteriasGlobales[8]), use_container_width=True)
        st.markdown('### Graph with slider')
        st.plotly_chart(graficoRS(datosRangeSlider[8]), use_container_width=True)
        st.markdown('### This is the data used to create the world maps')
        st.dataframe(dfConcat[8], use_container_width=True)
    elif seleccion_secundaria == "Bacteria: Veillonella":
        st.markdown('### Gráfico mapa mundi')
        st.plotly_chart(graficoBacteria(datosBacteriasGlobales[9]), use_container_width=True)
        st.markdown('### Graph with slider')
        st.plotly_chart(graficoRS(datosRangeSlider[9]), use_container_width=True)
        st.markdown('### This is the data used to create the world maps')
        st.dataframe(dfConcat[9], use_container_width=True)
elif seleccion_principal == "Taxonomy": 
    st.markdown('''
                <style>body {text-align: justify}</style>

                # Taxonomy

                Taxonomic classification is crucial for pathogen discovery, aiding in the development of diagnostic tools, treatments, and preventive measures against emerging infections [16](https://www.ncbi.nlm.nih.gov/books/NBK52875/). By utilizing taxonomy classification from genbank files, we can chart various levels of assignments using state-of-the-art visualization tools. Furthermore, our results show more diversity than previously reported, considering the bacteria of interest.'''
                , unsafe_allow_html=True)
        
    st.plotly_chart(graphTaxonomy(), use_container_width=True)
elif seleccion_principal == "Host":
    st.markdown('''
                <style>body {text-align: justify}</style>

                # Host
                Precisely identifying the animal, human host(s) that play a critical role in maintaining the transmission of pathogens is essential for efficiently managing, preventing, and eliminating these diseases. It also helps to reveal important information about the ecology of zoonotic infectious diseases and conservation strategies. Current evidence suggests that the majority of newly emerging diseases in humans originate from animals and are mostly caused by the transmission of pathogens from wildlife, either directly or indirectly [17](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8954416/#:~:text=Appropriate%20identification%20of%20the%20animal,infectious%20diseases%20and%20conservation%20strategies.). We selected groups of bacteria that can infect many different types of host and can be transmitted between multiple species. Understanding how these bacteria adapt and thrive in various host species and environments is crucial for predicting and controlling future outbreaks. 

                To gain insight in this matter, we have created an intuitive interface that allows users to explore the interactions between the bacteria and their surroundings in a dynamic and engaging way.
                '''
                , unsafe_allow_html=True)
    st.image('img/circosPoster.png')

    st.plotly_chart(graficoHost(), use_container_width=True)
    st.plotly_chart(treemapgraph(), use_container_width=True)
elif seleccion_principal == "Genetic Variation":
    st.markdown('''
                <style>body {text-align: justify}</style>

                # Variation Sequence
                Genetic sequencing has revolutionized the epidemiology of infectious diseases. The 16S rRNA sequence is the most widely used method to analyze the diversity of bacteria. This gene contains highly conserved regions, present in the majority of bacterial genomes, and hypervariable regions that allow taxa to be discriminated against [18](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7767281/#B40-microorganisms-08-02018).  

                Keeping this in mind we evaluated the genetic similarity between different organisms/strains belong to the same bacteria target in order to understand their potential pathogenesis. By comparing the 16S rRNA sequences of various isolates, we can determine if there are distinct clusters or subtypes within the population, indicating potential host, sources or routes of transmission. This information can then be used to inform public health interventions and control measures.



                ''', unsafe_allow_html=True)
    #st.plotly_chart(treemapgraph(), use_container_width=True)
    st.plotly_chart(graficoVarGen(), use_container_width=True)

elif seleccion_principal == 'Authors':

    st.markdown('''
                
                <style>body {text-align: justify}</style>

                # Authors:

                Fernanda Bravo Cornejo, bravoc@utem.cl; Diego Santibanez Oyarce, dsantibanezo@utem.cl; Camilo Cerda Sarabia, ccerdas@utem.cl; Hugo Osses Prado, hosses@utem.cl; Esteban Gomez Teran, egomez@utem.cl

                Raul Caulier-Cisterna, rcaulier@utem.cl; Jorge Vergara-Quezada, jorgever@utem.cl; Ana Moya-Beltran, amoya@utem.cl (corresponding author).

                This work was presented in the '1eras Jornadas de Ciencia de Datos y Salud pública' organized by Escuela de Salud pública, Universidad de Chile. https://saludpublica.uchile.cl/extension/programas/1ras-jornadas-de-ciencia-de-datos-y-salud-publica/presentacion

                Acknowledgement: Departamento de Informatica y Computacion, UTEM; Escuela de Informatica, UTEM; Laboratorio de Investigacion Aplicada, Departamento de Informatica y Computacion, UTEM.

                This is the first version of the project and was fully developed by students and professors of Universidad Tecnologica Metropolitana. https://www.utem.cl/universidad/
                ''', unsafe_allow_html=True)
