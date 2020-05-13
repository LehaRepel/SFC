import yaml_creator
import time
import tkinter
import yaml
from pprint import pprint

with open('sample_sheet_exp.yaml', 'r') as f:
    templates = yaml.safe_load(f)

#pprint(templates)
for i in templates:
    print(i)