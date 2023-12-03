"""This module extracts credentials from a valid salesforce.json file
{
  "username": "example@turingtrust.co.uk.uat",
  "password": "pass",
  "security_token": "token",
  "domain": "test"
}
domain is optional as simple_salesforce will default to "login"
"""

import os
import sys
import json
import jsonschema
from modules.schema import credentials_schema
from loguru import logger

def GetCredentials(environment="production"):
    requiresAppend = False
    if os.path.isfile(str(os.path.join(os.path.expanduser("~"),f'.cred/salesforce_readonly_{environment}.json'))):
        credentials_filepath = str(os.path.join(os.path.expanduser("~"),f'.cred/salesforce_readonly_{environment}.json'))
    else:
        credentials_filepath = str(os.path.join(os.path.expanduser("~"),'.cred/salesforce_readonly.json'))
        requiresAppend = True

    credentials = {}

    try:
        with open(credentials_filepath, 'r') as f:
            credentials = json.load(f)
            logger.info(f"Read credentials from {credentials_filepath}")
    except FileNotFoundError:
        logger.critical(f'ERROR: can not find salesforce.json in {credentials_filepath}')
        exit(1)

    try:
        jsonschema.validate(instance=credentials, schema=credentials_schema)
    except jsonschema.exceptions.ValidationError as err:
        logger.critical(f'ERROR: salesforce.json format is incorrect, Reason: {err.message}')
        #print(json.dumps(credentials, indent=1))
        exit(1)

    if environment != "production" and requiresAppend:
        credentials['domain'] = "test"
        credentials['username'] += f'.{environment}'
        logger.debug(f'---{environment} Sandbox---')

    return credentials
