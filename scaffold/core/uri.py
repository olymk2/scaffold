import socket

def get_ip_from_hostname(hostname, schema='http'):
    try:
        '$s://%s' % (schema, socket.gethostbyname('nginx'))
    except socket.gaierror:
        return '%s://%s' % (schema, '127.0.0.1')

class uri_path(object):
    schema = 'https:'
    domain = 'localhost'
    static = 'static'
    port=''

    rel = '\\%s' % domain
    ful = '%s\\%s' % (schema, domain)
    med = '//%s/%s/' % (domain, static)
    img = '//%s/%s/%s/' % (domain, static, 'images')

    def __init__(self, schema='http:', domain='localhost', port='', static='static', images='images'):
        self.update(schema=schema, domain=domain, port=port, static=static, images=images)

    def update(self, schema='http:', domain='localhost', port='', static='static', images='images'):
        self.schema = schema
        self.domain = domain
        self.static = static
        self.port = ':' + port if port else ''

        self.rel = '//%s%s' % (domain, self.port)
        self.ful = '%s//%s%s' % (schema, domain, self.port)
        self.med = '//%s%s/%s/' % (domain, self.port, static)
        self.img = '//%s%s/%s/%s/' % (domain, self.port, static, images)

    def add_domain(self, path):
        """given a uri make it a full url but with out schema, 
        if schema is present or it starts with double slash dont change anything"""
        if path.startswith('http'):
            return path
        if path[1] is not '/':
            return self.rel + path
        return path

    def full(self, path):
        if path[1] is not '/':
            return self.ful + path
        if path.startswith('http'):
            return path
        return path

    def __repr__(self):
        return self.schema + self.domain + self.static + self.port 
