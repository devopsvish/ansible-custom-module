# Ansible Custom Modules

`Ansible` is a powerful Configuration Management tool that has many built-in modules to configure target systems but there would be cases where we would need to perform tasks that are not provided by Ansible. So we have the flexibility of writing our custom modules and using them. These modules can be written in any language of our choice and I have preferred writing here with the help of Python.


## Usage
I have dockerized this project so you can easily run and test it in your machine if you have docker installed as a prerequiste

Start the containers using the below `docker-compose` command

```bash
docker-compose up -d
```

#### Ansible Playbook Test
Once the container is up get into the container using the below command to test our ansible playbook

```bash
ansible-playbook -i inventory/inventory.ini playbooks/vishtest_playbook.yml
```

#### Ansible Custom Module Test
To test the custom module created use the below command
```bash
ansible-playbook -i inventory/inventory.ini playbooks/employee_info.yml
```

## Blog Link
If you need to understand the Ansible Custom Module concept please refer to my blog post explaning the same.

[Ansible Custom Module Blog](https://mjvish.hashnode.dev/ansible-custom-modules)