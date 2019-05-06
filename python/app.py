from bottle import route, run
from line import line

@route('/line/<message>')
def line(message):
  line(message)
  return 'OK! message: ' + message

if __name__ == "__main__":
    run(host='0.0.0.0', port=8080)