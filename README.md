# Interface Bacteria Dashboard

Exploration and Visualization Interface for Public Database Information Regarding Pathogenic Bacteria in the Pulmonary Environment.

**Live Dashboard**: [Visit Website](https://informatica.utem.cl/investigacion/interfacebacteria/)

---

## About

Using this exploration and visualization interface, we utilize Data Science to uncover key insights within the healthcare landscape, particularly related to the sequences and metadata of pathogenic bacteria. Data science provides valuable insights into the large amount of internet data about individuals, institutions, and regulatory bodies, providing valuable understanding for decision-makers and healthcare professionals.

The COVID-19 pandemic demonstrated its potential, establishing essential evidence during emergencies. It emphasized the significance of data-driven approaches in dealing with complex and evolving public health crises, particularly those related to pathogens.

By integrating sequence data and associating information, our platform provides a comprehensive understanding of pathogens present in the pulmonary environment. Through sophisticated visualization techniques, users can navigate and interpret complex metadata, gaining valuable perspectives on the intricate interplay between pathogens and health.

This approach not only contributes to advancing scientific knowledge but also holds immense potential for shaping targeted strategies in the fight against infectious diseases. We selected nine bacterial genera that are reported in the literature as associated with the pathogenesis of the pulmonary environment.

---

## Quick Start

### Prerequisites

- Python 3.11+
- Conda (recommended) or pip

### Installation with Conda

```bash
# Clone the repository
git clone https://github.com/amoyabeltran/interfacebacteria.github.io.git
cd interfacebacteria.github.io

# Create and activate environment
conda env create -f environment.yml
conda activate infobacterias
```

### Installation with pip

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Running the Dashboard

```bash
streamlit run app.py
```

---

## Dashboard Sections

1. **Home** - Overview and bacteria descriptions
2. **Geo-localization** - World maps showing bacteria distribution by country
3. **Taxonomy** - Sunburst chart of taxonomic classification
4. **Host** - Pie chart and treemap of host distribution
5. **Genetic Variation** - Clustergram of genetic similarity
6. **Authors** - Project credits and acknowledgements

---

## Authors

This is the first version of the project and was fully developed by students and professors of [Universidad Tecnologica Metropolitana](https://www.utem.cl/universidad/).

### Student Contributors

- Fernanda Bravo Cornejo (bravoc@utem.cl)
- Diego Santibanez Oyarce (dsantibanezo@utem.cl)
- Camilo Cerda Sarabia (ccerdas@utem.cl)
- Hugo Osses Prado (hosses@utem.cl)
- Esteban Gomez Teran (egomez@utem.cl)

### Faculty Advisors

- Raul Caulier-Cisterna (rcaulier@utem.cl)
- Jorge Vergara-Quezada (jorgever@utem.cl)
- **Ana Moya-Beltran** (amoya@utem.cl) - *Corresponding author*

---

## Presentations

This work was presented at the *'1eras Jornadas de Ciencia de Datos y Salud Publica'* organized by Escuela de Salud Publica, Universidad de Chile. [More information](https://saludpublica.uchile.cl/extension/programas/1ras-jornadas-de-ciencia-de-datos-y-salud-publica/presentacion)

---

## Acknowledgements

- Departamento de Informatica y Computacion, UTEM
- Escuela de Informatica, UTEM
- Laboratorio de Investigacion Aplicada, Departamento de Informatica y Computacion, UTEM
