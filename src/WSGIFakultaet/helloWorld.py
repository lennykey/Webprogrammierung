from cgi import parse_qs, escape

def fibbo(x):
    if x < 1:
        return 0
    if x == 1:
        return 1    

    return fibbo(x-1) + fibbo(x-2)
        
def hello_world(environ, start_response):
    parameters = parse_qs(environ.get('QUERY_STRING', ''))
    if 'subject' in parameters:
        #subject = escape(parameters['subject'][0])
        subject = int(parameters['subject'][0])
        
        subject = fibbo(subject)
        
    else:
        subject = '0'
    start_response('200 OK', [('Content-Type', 'text/html')])
    return ['''<title>Hello %(subject)s</title>
    <p>Hello %(subject)s!</p>''' % {'subject': subject}]


if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    srv = make_server('localhost', 8080, hello_world)
    srv.serve_forever()
