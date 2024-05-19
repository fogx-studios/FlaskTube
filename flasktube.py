from flask import Flask, render_template, request, send_file
from pytube import YouTube
from moviepy.editor import VideoFileClip
import os

app = Flask(__name__, static_folder='static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    video_url = request.form['url']
    yt = YouTube(video_url)
    stream = yt.streams.first()
    file_path = stream.download()

    format_option = request.form['format']

    if format_option == 'Download MP4':
        return "<h1>Mp4 Download Complete</h1>"
    elif format_option == 'Download MP3':
        # Convert video to MP3
        video_clip = VideoFileClip(file_path)
        audio_clip = video_clip.audio
        mp3_file_path = file_path.replace(".mp4", ".mp3")
        audio_clip.write_audiofile(mp3_file_path)
        audio_clip.close()
        video_clip.close()

        return "<h1>Mp3 Downlaod Complete</h1>"
    

if __name__ == '__main__':
    app.run(debug=True)
