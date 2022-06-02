from flask import Flask, request, render_template
import requests
import time


def get_transcribe_id(token,url):
    '''
        Parameter:
        token: The AssemblyAI API key
        url  : Url to uploaded file
        Return Value:
        id   : The transcribe id of the file
    '''
    endpoint = "https://api.assemblyai.com/v2/transcript"
    json = {
      "audio_url": url
    }
    headers = {
      "authorization": token,
      "content-type": "application/json"
    }
    response = requests.post(endpoint, json=json, headers=headers)
    id_ = response.json()['id']
    print("Made request and file is currently queued")
    return id_



def get_text(token,transcribe_id):
    '''
      Parameter:
        token: The AssemblyAI API key
        transcribe_id: The ID of the file which is being
      Return Value:
        result : The response object
    '''
    endpoint = f"https://api.assemblyai.com/v2/transcript/{transcribe_id}"
    headers = {
      "authorization": token
    }
    result = requests.get(endpoint, headers=headers).json()
    return result



app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('my-form.html')

@app.route('/', methods=['POST'])
def my_form_post():
    assemblyai_token= '1717426a768a4748a6ed25b07cb31160'
    recording_endpoint = request.form['text']
    transcribe_id = get_transcribe_id(assemblyai_token,recording_endpoint)
    result = {}
    while result.get("status") != 'completed' and result.get("status") != 'error':
        time.sleep(2)
        result = get_text(assemblyai_token,transcribe_id)
    
    #results = { 'TranscribedText' : [ result['text']] }
    results = "{ 'TranscribedText' : [ " + str(result['text']) + " ] }"
    return render_template('my-form-1.html',processed_text=results)


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)