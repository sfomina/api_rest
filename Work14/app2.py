from watson_developer_cloud import watson_developer_cloud_service
from watson_developer_cloud import tone_analyzer_v3
import json
from flask import Flask, render_template, request


tone_analyzer = tone_analyzer_v3.ToneAnalyzerV3(
  username= "1040bc05-8ffa-4577-a465-43d95b55737d",
  password= "0xvV0yqEOsyy",
  version='2016-05-19'
)

'''
with open('tone.json') as tone_json:
  tone = tone_analyzer.tone(json.load(tone_json)['text'], tones='emotion',
    content_type='text/plain')
'''
'''
tone = tone_analyzer.tone(text="I like to have fun", tones='emotion',content_type='text/plain')

print(json.dumps(tone, indent=2))
'''


my_app = Flask(__name__)

@my_app.route('/')

def root():
    return render_template("home.html", text = "");


@my_app.route('/angry', methods = ['GET', 'POST'])

def angry():
  text_input = request.form['body']

  #tone is already a python dictionary
  tone = tone_analyzer.tone(text=text_input, tones='emotion',content_type='text/plain')

  #print tone

  angry_score = (((((tone["document_tone"])["tone_categories"])[0])["tones"])[0])["score"]
  print angry_score

  return render_template("angry.html", text = text_input, score = angry_score);
  
  



if __name__== '__main__':
  my_app.debug = True
  my_app.run()
