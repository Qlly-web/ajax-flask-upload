from flask import Flask, render_template, request
from os import path
import time
import re

u_path = path.dirname(__file__)
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/ufile', methods=['post'])
def ufile():
    try:
        file = request.files['file']
        r = re.search(r'(\.\S+)', file.filename)
        fn = ""
        if(r != None):
            fn = r.group()
            file.save(u_path + '/static/file/' + str(time.time())+fn)
            return 'success'
    except Exception as e:
        print(e)
        return 'fail'


if __name__ == '__main__':
    app.run(debug=True)
