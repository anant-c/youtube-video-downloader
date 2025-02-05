import yt_dlp
import os

def choose_quality():
    """Prompt the user to choose a video quality."""
    print("\nChoose a video quality:")
    print("1. 360p")
    print("2. 480p")
    print("3. 720p")
    print("4. Max Quality")
    
    choice = input("Enter your choice (1-4): ")
    
    quality_map = {
        "1": "bestvideo[height<=360]+bestaudio/best",
        "2": "bestvideo[height<=480]+bestaudio/best",
        "3": "bestvideo[height<=720]+bestaudio/best",
        "4": "bestvideo+bestaudio/best"
    }
    
    return quality_map.get(choice, "bestvideo+bestaudio/best")

def download_video(url, save_path="downloads/", audio_only=False):
    """Download a YouTube video or audio using yt-dlp with selected quality."""
    try:
        # Ensure the save path exists
        if not os.path.exists(save_path):
            os.makedirs(save_path)

        # Allow quality selection if not downloading audio
        format_choice = "bestaudio/best" if audio_only else choose_quality()

        # yt-dlp options
        ydl_opts = {
            'outtmpl': os.path.join(save_path, '%(title)s.%(ext)s'),
            'format': format_choice,
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
