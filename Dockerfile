# Interface Bacteria Dashboard - Docker Configuration
# Optimized for the new project structure

FROM python:3.11-slim-bookworm

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONPATH=/app \
    # Streamlit configuration
    STREAMLIT_SERVER_PORT=8501 \
    STREAMLIT_SERVER_ADDRESS=0.0.0.0 \
    STREAMLIT_BROWSER_GATHER_USAGE_STATS=false

# Set working directory
WORKDIR /app

# Install system dependencies required for geopandas, fiona, and other packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libgdal-dev \
    libgeos-dev \
    libproj-dev \
    gdal-bin \
    curl \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get clean

# Set GDAL environment variables
ENV GDAL_CONFIG=/usr/bin/gdal-config

# Copy requirements first for better cache utilization
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY app.py .
COPY dashboard/ ./dashboard/
COPY data/ ./data/

# Create Streamlit config directory and configuration
RUN mkdir -p ~/.streamlit
RUN echo '\
    [server]\n\
    port = 8501\n\
    \n\
    [theme]\n\
    primaryColor = "#1f77b4"\n\
    backgroundColor = "#ffffff"\n\
    secondaryBackgroundColor = "#f0f2f6"\n\
    textColor = "#262730"\n\
    ' > ~/.streamlit/config.toml

# Expose the Streamlit default port
EXPOSE 8501

# Health check - verify the app is running
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD curl --fail http://localhost:8501/_stcore/health || exit 1

# Run the Streamlit application
CMD ["streamlit", "run", "app.py"]
