#!/bin/bash

# how to query the misp rest search endpoint
curl https://misp.local/attributes/restSearch -H "Authorization: <api-key>" -H "Content-Type: application/json" -H "Accept: application/json" --data '{"returnFormat": "json", "last":"1d", "type": "ip-dst", "to_ids": true}' > out

# parsing output using jq
cat out | jq ."response"."Attribute"[]."value"
