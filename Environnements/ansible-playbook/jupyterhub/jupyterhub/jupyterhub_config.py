import os

# We start with the configuration of the spawner:
# we use the class DockerSpawner to spawn single-user servers in a separate Docker container.
#  We use here the environment variables that we have set in docker-compose.yml:
c.JupyterHub.hub_ip = '0.0.0.0'
c.JupyterHub.spawner_class = 'dockerspawner.SwarmSpawner'
c.DockerSpawner.image = os.environ['DOCKER_JUPYTER_IMAGE']

# Network configurations
# https://jupyterhub-dockerspawner.readthedocs.io/en/latest/spawner-types.html#swarmspawner
network_name = os.environ['DOCKER_NETWORK_NAME']
c.SwarmSpawner.network_name = network_name

# Optionally, we may want to stop the single-user servers after a certain amount of idle time. Following this example, we register a JupyterHub service like this:
# c.JupyterHub.services = [
#     {
#         'name': 'cull_idle',
#         'admin': True,
#         'command': 'python /srv/jupyterhub/cull_idle_servers.py --timeout=3600'.split(),
#     },
# ]

# Redirect to JupyterLab, instead of the plain Jupyter notebook
c.Spawner.default_url = '/lab'

#The quickest way to get a JupyterHub server running with a working authentication, is to delegate to an authentication service such as Github.
# from oauthenticator.github import GitHubOAuthenticator
# c.JupyterHub.authenticator_class = GitHubOAuthenticator

# for local testing
c.JupyterHub.authenticator_class = 'dummyauthenticator.DummyAuthenticator'
c.DummyAuthenticator.password = "your strong password"

# user data persistence
# see https://github.com/jupyterhub/dockerspawner#data-persistence-and-dockerspawner
notebook_dir = os.environ.get('DOCKER_NOTEBOOK_DIR') or '/home/jovyan/work'
c.SwarmSpawner.notebook_dir = notebook_dir
# c.DockerSpawner.volumes = { 'jupyterhub-user-{username}': notebook_dir }