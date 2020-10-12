# Do not forget to pin down the version
FROM jupyterhub/jupyterhub

# Copy the JupyterHub configuration in the container
COPY jupyterhub_config.py .

# Download script to automatically stop idle single-user servers
ADD https://raw.githubusercontent.com/jupyterhub/jupyterhub/0.9.3/examples/cull-idle/cull_idle_servers.py /srv/jupyterhub/cull_idle_servers.py

# Install dependencies (for advanced authentication and spawning)
RUN pip install \
    dockerspawner==0.11.1 \
    oauthenticator==0.11.0 \
    jupyterhub-dummyauthenticator