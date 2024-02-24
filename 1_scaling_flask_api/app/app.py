import subprocess
from flask import Flask
app = Flask(__name__)

def hostname():
    result = subprocess.run(['hostname'], stdout=subprocess.PIPE)
    return result.stdout.decode('utf-8')

@app.route('/')
@app.route('/index')
def index():
    try:
        f = open('/app/color.txt')
        color = f.read()
        f.close()
    except:
        color = 'unknown'

    color = color.strip().upper()

    return 'Hello world from ' + color + '!'


@app.route('/ping')
def ping():
    hn = hostname()
    return 'PONG from ' + hn, 200


if __name__ == '__main__':
    app.run('0.0.0.0', debug=True, port=8000)
