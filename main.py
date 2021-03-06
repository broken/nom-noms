from bottle import Bottle
from bottle import static_file

bottle = Bottle()

# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.

@bottle.route('/')
def main(name=''):
  return static_file('main.html', root='views')

@bottle.route('/components/nom-noms/<filepath:path>')
def nomnoms(filepath):
  return static_file(filepath, root='components/nom-noms')

@bottle.route('/components/<filepath:path>')
def components(filepath):
  return static_file(filepath, root='bower_components')

# Define an handler for 404 errors.
@bottle.error(404)
def error_404(error):
  """Return a custom 404 error."""
  return 'Sorry, nothing at this URL.'
