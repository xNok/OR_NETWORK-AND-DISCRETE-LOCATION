traefik_local:
	cd ./Environnements/ansible-playbook/traefik/ && docker stack deploy traefik --compose-file ./docker-compose.yml --compose-file ./docker-compose.local.yml