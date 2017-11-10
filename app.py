from flask import Flask, render_template
import urllib2, json

my_app = Flask(__name__)

@my_app.route('/')


def root():
    u = urllib2.urlopen('https://api.nasa.gov/planetary/apod?api_key=3EtFP1nYRwC1RY1CMCfpXaH9yHmA4B1bkC65OFqt')

    text = u.read()
    d = json.loads(text)
    return render_template('apod.html',image=d['url'],summary=d['explanation'])


if __name__== '__main__':
    my_app.debug = True
    my_app.run()
    
