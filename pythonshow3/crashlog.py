import functools
import logging
import logging.handlers


crashlogger = logging.getLogger('__crashes__')


def configure_crashreport(mailhost, fromaddr, toaddrs, subject, 
                          credentials, tls=False):
        crashlogger.addHandler(
            logging.handlers.SMTPHandler(
                mailhost=mailhost,
                fromaddr=fromaddr,
                toaddrs=toaddrs,
                subject=subject,
                credentials=credentials,
                secure=tuple() if tls else None
            )
        )


def crashreport(f):
    @functools.wraps(f)
    def _crashreport(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except Exception as e:
            crashlogger.exception(
                '{} crashed\n'.format(f.__name__)
            )
            raise
    return _crashreport



configure_crashreport(
        ('localhost', 1025),
        'no-reply@your-smtp-host.com',
        'crashes_receiver@another-smtp-host.com',
        'Automatic Crash Report from TestApp',
        credentials=None,
        tls=False
)


@crashreport
def hello_world(environ, start_response):
    if environ["PATH_INFO"] == "/CRASH":
        raise RuntimeError("Oh Oh, something crashed")

    start_response('200 OK', [('Content-Type', 'text/html')])
    return ['''Hello World''']

from wsgiref.simple_server import make_server
srv = make_server('localhost', 8080, hello_world)
srv.serve_forever()
