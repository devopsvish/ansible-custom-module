from ansible.module_utils.basic import AnsibleModule

def main():
    parameters = {
        'name': {"required": True, "type": 'str'},
        'designation': {"required": True, "type": 'str'},
        'skills': {"required": True, "type": 'str'},
        'location': {"required": False, "type": 'str'}
    }

    module = AnsibleModule(argument_spec=parameters)

    name = module.params['name']
    designation = module.params['designation']
    skills = module.params['skills']
    location = module.params['location']

    output = {
        'name': name,
        'designation': designation,
        'skills': skills,
        'location': location,
        'message': f"{name} is a {designation} with {skills} from {location}",
        # 'location_type': f"{type(location)}"
    }

    module.exit_json(changed=False, **output)

if __name__ == '__main__':
    main()
