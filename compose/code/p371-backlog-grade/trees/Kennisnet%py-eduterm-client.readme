[![Build Status](https://travis-ci.org/kennisnet/py-eduterm-client.svg?branch=master)](https://travis-ci.org/kennisnet/py-eduterm-client)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/edutermclient.svg)](https://pypi.org/project/edutermclient/)
[![PyPI version](https://img.shields.io/pypi/v/edutermclient.svg)](https://pypi.org/project/edutermclient/)

# EdutermClient
Python library for interfacing with the Eduterm API.

## usage
Initiate the client with a valid api key, and request with a queryname and optional arguments. The response table will allow you to iterate the response rows.
```python
from edutermclient.edutermclient import EdutermClient

c = EdutermClient("4c6ef653-44cf-4537-88f5-379d41575f0a")
c.request("VakLeergebieden", {"onderwijsniveau": "bk:512e4729-03a4-43a2-95ba-758071d1b725"})

for row in c.response_table:
    print(row["vakLabel"])
```
