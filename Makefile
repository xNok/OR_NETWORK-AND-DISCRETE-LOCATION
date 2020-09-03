traefik_local:
	cd ./Environnements/ansible-playbook/traefik/ && docker stack deploy traefik --compose-file ./docker-compose.yml --compose-file ./docker-compose.local.yml

portainer_local:
	cd ./Environnements/ansible-playbook/portainer/ && docker stack deploy portainer --compose-file ./docker-compose.yml --compose-file ./docker-compose.local.yml

ansible_traefik:
	cd ./Environnements/ && ansible-playbook ansible-playbook/traefik/playbook.yml -i .inv

ansible_portainer:
	cd ./Environnements/ && ansible-playbook ansible-playbook/portainer/playbook.yml -i .inv