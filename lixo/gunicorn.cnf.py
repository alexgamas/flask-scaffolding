#DEBUG = True
debug = True
workers = 4
bind = "0.0.0.0:5000"
proc_name = 'gunicorn.proc'
pidfile = '/tmp/gunicorn.pid'
logfile = '/tmp/gunicorn.debug.log'
loglevel = 'debug'
