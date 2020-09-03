

# Ansible Playbooks

## Prepare SSH keys

`ansible-playbook ansible-playbook/password-less-ssh/playbook.yml --extra-vars "node= user= password= passphrase="`

## test connectivity

You should use ssh-agent to avoid typing the passphrase for each host

```
ssh-agent bash
ssh-add ~/.ssh/id_rsa
```

`ansible all -m ping -i .inv`

## Install docker

`ansible-playbook ansible-playbook/docker_debian/playbook.yml -i .inv`

## Prepare docker swarm

`ansible-playbook ansible-playbook/docker_swarm/playbook.yml -i .inv`

## Install Traefik

`ansible-playbook ansible-playbook/traefik/playbook.yml -i .inv`

Traefik is availiables at:
* traefik.${DOMAINE}/api
* traefik.${DOMAINE}/dashboard


* https://github.com/acmesh-official/acme.sh
* https://github.com/acmesh-official/acme.sh/wiki/dnsapi
* https://github.com/acmesh-official/acme.sh/wiki/How-to-use-OVH-domain-api


## Local testing

`docker stack deploy traefik --compose-file .\docker-compose.yml --compose-file .\docker-compose.local.yml`

## References

* https://www.codementor.io/@slavko/unobtrusive-local-development-with-traefik2-docker-and-letsencrypt-15qw1ypoi8
* https://dev.to/ohffs/traefik-v2-with-docker-swarm-2cgh
* https://medium.com/@jakub.hajek/container-orchestration-with-traefik-2-x-and-docker-swarm-with-canary-deployment-27e7ea62af6f

Let's Encrypt:
* https://medium.com/nephely/configure-traefik-for-the-dns-01-challenge-with-ovh-as-dns-provider-c737670c0434
* https://docs.traefik.io/user-guides/docker-compose/acme-dns/

Ansible Vault:
*https://symfonycasts.com/screencast/ansible/variable-vault