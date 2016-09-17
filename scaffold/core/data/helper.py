import os
import sys

def required_values(data, required):
    # changed from viewkeys for python3
    #if not data.keys() >= required:
    #    print(required.difference(data.keys()))
    #    print('required params = ' + str(required))
    #    print('actual params = ' + str(data.keys()))
    #    raise ValueError('Missing Required values')
    for key in required:
        if key not in data:
            print(required.difference(data.keys()))
            print('required params = ' + str(required))
            print('actual params = ' + str(data.keys()))
            raise ValueError('Missing Required values')
        if data.get(key) is None:
            print('Missing values')
            print(required)
            print(data)
            print(key)
            raise ValueError('Expected value got None Type')

def optional_values(data, optional):
    # changed from viewkeys for python3
    if not data.keys() >= {'title', 'owner_user_id', 'milestone_id'}:
        raise ValueError

def load_sql(filename):
    query = ''
    try:
        with open(os.path.abspath('./data/sql/' + filename)) as fp:
            query = fp.read()
    except:
        print('Failed to load sql file %s ' % filename)
    return query
