import yt_dlp
import os

def download_video(url, save_path="downloads/", audio_only=False):
    """Download a YouTube video or audio using yt-dlp."""
    try:
        # Ensure the save path exists
        if not os.path.exists(save_path):
            os.makedirs(save_path)

        # yt-dlp options
        ydl_opts = {
            'outtmpl': os.path.join(save_path, '%(title)s.%(ext)s'),
            'format': 'bestaudio/best' if audio_only else 'bestvideo+bestaudio/best',
            'merge_output_format': 'mp4' if not audio_only else 'mp3',
            'socket_timeout': 60 
        }

        # Download video or audio
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        print("✅ Download completed!")

    except Exception as e:
        print(f"❌ Error: {e}")

# Get user input
video_url = input("Enter YouTube Video URL: ")
download_video(video_url)
    