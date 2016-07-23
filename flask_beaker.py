'''
    flaskext.beaker
    ---------------
    
    A Flask extension providing beaker session interface.
    
    :copyright: (c) 2012 by Syrus Akbary.
    :license: MIT, see LICENSE for more details.
'''

__version__ = '0.3.0'
try:
    from beaker.middleware import SessionMiddleware
except ImportError, e:
    print 'Beaker package is required to use Flask-Beaker'
    raise e

from flask.sessions import SessionInterface

class BeakerSessionInterface(SessionInterface):
    def open_session(self, app, request):
        return request.environ.get('beaker.session')

    def save_session(self, app, session, response):
        session.save()

class BeakerSession(object):
    def __init__(self, app=None, data_dir='/tmp/session/data', lock_dir='/tmp/session/lock'):
        if app is not None:
            self.init_app(app, data_dir, lock_dir)
    
    def init_app(self, app, data_dir, lock_dir):
        '''Initalizes the application with the extension.
        
        :param app: The Flask application object.
        '''
        self.app = app
        self._session_conf = app.config.get('BEAKER_SESSION', {
            'session.type': 'file',
            'session.data_dir': data_dir,
            'session.lock_dir': lock_dir
        })
        app.wsgi_app = SessionMiddleware(app.wsgi_app, self._session_conf)
        app.session_interface = BeakerSessionInterface()
