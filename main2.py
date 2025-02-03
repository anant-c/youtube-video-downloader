from flask import Flask, request, jsonify, send_from_directory
import yt_dlp
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for React frontend

DOWNLOAD_FOLDER = "downloads/"
if not os.path.exists(DOWNLOAD_FOLDER):
    os.makedirs(DOWNLOAD_FOLDER)

def download_video(url, audio_only=False):
    """Download YouTube video or audio using yt-dlp."""
    try:
        ydl_opts = {
            'outtmpl': os.path.join(DOWNLOAD_FOLDER, '%(title)s.%(ext)s'),
            'format': 'bestaudio/best' if audio_only else 'bestvideo+bestaudio/best',
            'merge_output_format': 'mp4' if not audio_only else 'mp3',
            'socket_timeout': 60
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=True)
            filename = ydl.prepare_filename(info_dict)
            return os.path.basename(filename)  # Only return filename, not full path

    except Exception as e:
        return None

@app.route("/download", methods=["POST"])
def download():
    data = request.get_json()
    video_url = data.get("url")
    audio_only = data.get("audio_only", False)

    filename = download_video(video_url, audio_only)

    if filename and os.path.exists(os.path.join(DOWNLOAD_FOLDER, filename)):
        return jsonify({"success": True, "file": filename})
    else:
        return jsonify({"success": False, "error": "Download failed"}), 500

@app.route("/get-file/<filename>", methods=["GET"])
def get_file(filename):
    try:
        return send_from_directory(DOWNLOAD_FOLDER, filename, as_attachment=True)
    except FileNotFoundError:
        return jsonify({"error": "File not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
