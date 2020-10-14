FROM jupyter/scipy-notebook

# Jupyterhub compatibility
ARG JUPYTERHUB_VERSION=1.1.0
RUN pip install --no-cache \
    jupyterhub==$JUPYTERHUB_VERSION

# Environment Variables
ENV JUPYTER_ENABLE_LAB=yes
ENV PROJ_LIB=/opt/conda/share/proj

# Install conda plugin
RUN conda install -c conda-forge -y jupyterlab jupyterlab-git
RUN jupyter lab build

# Specific to our infra
RUN conda install -c conda-forge -y pymongo basemap cartopy
