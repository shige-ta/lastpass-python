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

try:
    with open('backup.dat', 'rb') as fp:
        vault = pickle.load(fp)
    if vault == None:
        # First try without a multifactor password
        vault = Vault.open_remote(username, password, None)
except:
    # Get the code
    multifactor_password = input('Enter Google Authenticator code:')

    # And now retry with the code
    vault = Vault.open_remote(username, password, multifactor_password)

for index, i in enumerate(vault.accounts):
    if i.notes.decode('utf-8') in '':
        print('url:' + i.url.decode('utf-8'))


# 書き込み
with open('backup.dat', 'wb') as fp:
    pickle.dump(vault, fp)

