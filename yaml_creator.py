import yaml

a = '1'
trunk_template = [
    ['switchport trunk encapsulation dot1q'], 'switchport mode trunk',
    'switchport trunk native vlan 999', 'switchport trunk allowed vlan'
]

access_template = [
    'switchport mode access', 'switchport access vlan',
    'switchport nonegotiate', 'spanning-tree portfast',
    'spanning-tree bpduguard enable'
]
to_yaml1 = {'acsees': access_template}
to_yaml = {'trunk': trunk_template, 'access': to_yaml1, 'a': a}


with open('sw_templates.yaml', 'w') as f:
    yaml.dump(to_yaml, f)

with open('sw_templates.yaml') as f:
    print(f.read())