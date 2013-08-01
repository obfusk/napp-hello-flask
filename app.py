import os, re, time, sys
from flask import Flask, Response

app = Flask(__name__)

@app.route('/')
def hello():
  t1 = """
    Hello World!
    The time is: %s

    - napp-hello-flask
  """ % time.strftime('%F %T')
  t2 = re.sub(r'^ {,4}', '', t1, flags = re.M)
  return Response(t2[1:], mimetype = 'text/plain')

if __name__ == '__main__':
  p = sys.argv[1] if len(sys.argv) > 1 else os.environ.get('PORT')
  app.run(port = int(p or 8888))
