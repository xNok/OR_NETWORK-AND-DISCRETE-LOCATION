

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

`ansible-galaxy install arillso.traefik`

`ansible-playbook ansible-playbook/traefik/playbook.yml -i .inv`