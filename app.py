from flask import Flask, request
from youtube_transcript_api import YouTubeTranscriptApi
app = Flask(__name__)

@app.route('/getcaption',methods=['POST'])
def post_data():
    try:
        data = request.get_json()
        srt - YouTubeTranscriptApi.get_transcript(data["id"])
        return str
    except Exception as e:
        return 'Error: {}'.format(str(e)), 404

if __name__ == '__main__':
    app.run(debug==True)