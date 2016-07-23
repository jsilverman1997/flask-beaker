============
Flask-Beaker
============

Beaker session interface for Flask.


INSTALLATION
============

First, you must do::

    pip install Flask-Beaker

Or::

    python setup.py install


Usage
=====

For using Beaker session management in Flask you only have to add this into your app::

  from flask_beaker import BeakerSession
  BeakerSession(app)

If you wish to use different Beaker session file paths than the default::

  from flask_beaker import BeakerSession
  BeakerSession(app, data_dir='/media/shared/data', lock_dir='/media/shared/lock')

TODOs and BUGS
==============
See: http://github.com/syrusakbary/flask-beaker/issues