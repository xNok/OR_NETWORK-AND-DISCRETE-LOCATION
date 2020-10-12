FROM jupyter/scipy-notebook

# Environment Variables
ENV JUPYTER_ENABLE_LAB=yes
ENV PROJ_LIB=/opt/conda/share/proj

# Specific to our infra
RUN conda install -c conda-forge -y pymongo basemap cartopy
