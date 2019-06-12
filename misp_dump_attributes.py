#!/usr/bin/env python

from pymisp import PyMISP
import json

misp = PyMISP('https://misp.localhost/', '<api-key>', True, 'json')

ret = ""
result = misp.search('attributes', type_attribute = 'ip-dst', to_ids = True)
for attribute in result['response']['Attribute']:
    ret += attribute['id'] + ","
    ret += attribute['event_id'] + ","
    ret += attribute['value'] + "\n"

print (ret)
