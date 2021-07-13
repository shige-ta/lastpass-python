# coding: utf-8
from __future__ import print_function

import pickle

import json
import os
from lastpass import (
    Vault,
    LastPassIncorrectYubikeyPasswordError,
    LastPassIncorrectGoogleAuthenticatorCodeError
)

with open(os.path.join(os.path.dirname(__file__), 'credentials.json')) as f:
    credentials = json.load(f)
    username = credentials['username']
    password = credentials['password']


jsonstr = []

try:
    with open('backup.json', 'r') as fp:
        jsonstr = json.load(fp)

except:
    # Get the code
    multifactor_password = input('Enter Google Authenticator code:')
    vault = Vault.open_remote(username, password, multifactor_password)

    for index, i in enumerate(vault.accounts):
        if i.notes.decode('utf-8') in '':
            jsonstr.append({'username' : i.name.decode('utf-8')})
            jsonstr.append({'url': i.url.decode('utf-8')})

print(jsonstr)

with open('backup.json', 'w') as f:
    json.dump(jsonstr, f, ensure_ascii=False)




