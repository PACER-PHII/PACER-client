# -*- coding: utf-8 -*-

import getopt
import json
import sys

import requests as requests

g_index_file = 'pacer-index-api.json'
g_url = 'http://localhost:8086/pacer-index-api/1.0.0/manage'


def read_indexes():
    # Read all PACER server indexes.
    headers = {'Content-Type': 'application/json'}
    r = requests.get(g_url, headers=headers, auth=('user', 'password'))
    if r.status_code == 200:
        # Data received. Store the data in filename = pacer-index-api.json
        with open(g_index_file, "w") as pacer_index_data_file:
            json.dump(r.json(), pacer_index_data_file, indent=4, sort_keys=True)
    else:
        print('Failed to get pacer-index-api service data content from {}'.format(g_url))


def push_indexes():
    # read json from pacer-index-api.json file.
    with open(g_index_file, "r") as pacer_index_data_file:
        index_data = json.load(pacer_index_data_file)

    # Push index data to indexing server
    headers = {'Content-Type': 'application/json'}

    if index_data['count'] <= 0:
        print('{} has no index entry.'.format(g_index_file))
        return
    for entry in index_data['list']:
        r = requests.post(g_url, headers=headers, auth=('user', 'password'), json=entry)
        print('writing {} : {}'.format(entry['id'], r.status_code))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    argList = sys.argv[1:]
    options = "hu:rw"
    long_opts = ["Help", "Url", "Read", "Write"]
    is_read = False
    is_write = False

    try:
        # Parsing argument
        args, vals = getopt.getopt(argList, options, long_opts)
        # checking each argument
        for currentArg, currentVal in args:
            if currentArg in ("-h", "--Help"):
                print("This will read pacer-index-api service data content and write them back to the API.")
                print("Use -r or --Read to read from Url (default http://localhost:8086/pacer-index-api/1.0.0/manage)")
                print("Use -w or --Write to write to Url (pacer-index-api.json file must exist")
                print("Use -u or --Url (optional) Default: http://localhost:8086/pacer-index-api/1.0.0/manage")

            elif currentArg in ("-u", "--Url"):
                g_url = currentVal

            elif currentArg in ("-r", "--Read"):
                is_read = True

            elif currentArg in ("-w", "--Write"):
                is_write = True

    except getopt.error as err:
        # output error, and return with an error code
        print(str(err))

    if is_read:
        read_indexes()

    if is_write:
        push_indexes()
