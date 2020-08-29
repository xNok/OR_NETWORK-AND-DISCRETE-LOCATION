traefik_local:
	cd ./Environnements/ansible-playbook/traefik/ && docker stack deploy traefik --compose-file ./docker-compose.yml --compose-file ./docker-compose.local.yml

ansible_traefik:
	cd ./Environnements/ && ansible-playbook ansible-playbook/traefik/playbook.yml -i .inv