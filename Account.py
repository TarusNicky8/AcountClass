# import libraries
import hashlib
import random
import string
import json
import binascii
import numpy as np
import pandas as pd
import pylab as pl
import logging
import datetime
import collections

self._private_key = RSA.generate(1024, random)
self._public_key = self._private_key.publickey()

class Client:
   def __init__(self):
      random = Crypto.Random.new().read
      self._private_key = RSA.generate(1024, random)
      self._public_key = self._private_key.publickey()
      self._signer = PKCS1_v1_5.new(self._private_key)

   @property
   def identity(self):
      return
binascii.hexlify(self._public_key.exportKey(format='DER')).decode('ascii')

def __init__(self, sender, recipient, value):
   self.sender = sender
   self.recipient = recipient
   self.value = value
   self.time = datetime.datetime.now()


   identity == self.sender.identity
   return collections.OrderedDict({
   'sender': identity,
   'recipient': self.recipient,
   'value': self.value,
   'time' : self.time})

def to_dict(self):
   if self.sender == "Genesis":
      identity = "Genesis"
   else:
      identity = self.sender.identity

   return collections.OrderedDict({
      'sender': identity,
      'recipient': self.recipient,
      'value': self.value,
      'time' : self.time})

def create_hd_wallet(wallet_name, xpubkey, api_key, subchain_indices=[], coin_symbol='btc'):
    '''
    Create a new wallet from an extended pubkey (xpub... for BTC)

    You can delete the wallet with the delete_wallet method below
    '''
    inferred_coin_symbol = coin_symbol_from_mkey(mkey=xpubkey)
    if inferred_coin_symbol:
        assert coin_symbol in inferred_coin_symbol
    assert api_key, 'api_key required'
    assert len(wallet_name) <= 25, wallet_name

    data = {
            'name': wallet_name,
            'extended_public_key': xpubkey,
            }
    params = {'token': api_key}

    if subchain_indices:
        data['subchain_indexes'] = subchain_indices

    url = make_url(coin_symbol, **dict(wallets='hd'))

    r = requests.post(url, json=data, params=params, verify=True, timeout=TIMEOUT_IN_SECONDS)
    return get_valid_json(r) 