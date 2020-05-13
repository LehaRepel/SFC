import yaml
def Create(a):
    if a == 1:
     runinfo_template = {'Script': Script.text, 'Read1:': Read1.text}
     to_yaml = {'RunInfo': runinfo_template}
     with open('sw_templates.yaml', 'w') as f:
         yaml.dump(to_yaml, f)