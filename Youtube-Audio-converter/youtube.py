#!/home/davinci/Desktop/python/Youtube-Audio-converter/tube/bin/python

import yt_dlp
import os

def download_video(youtube_url, output_folder):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Download the highest quality video
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'outtmpl': os.path.join(output_folder, '%(title)s.%(ext)s'),
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([youtube_url])

    print(f"Video saved to: {output_folder}")

def download_audio(youtube_url, output_folder):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Download the audio and convert to 320 kbps MP3
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(output_folder, 'temp_audio.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '320',
        }],
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([youtube_url])

    # Rename the file to the video title
    info_dict = ydl.extract_info(youtube_url, download=False)
    temp_audio_path = os.path.join(output_folder, 'temp_audio.mp3')
    mp3_file = os.path.join(output_folder, info_dict.get('title', 'audio') + '.mp3')
    
    if os.path.exists(temp_audio_path):
        os.rename(temp_audio_path, mp3_file)

    print(f"Audio saved to: {mp3_file}")

if __name__ == "__main__":
    # Prompt user for YouTube URL
    youtube_url = input("Enter the YouTube video URL: ").strip()
    
    # Prompt user for download option
    choice = input("Enter 1 for video or 2 for audio: ").strip()
    
    if choice == '1':
        # Path to your videos folder
        videos_folder = os.path.expanduser("~/Videos")
        download_video(youtube_url, videos_folder)
    elif choice == '2':
        # Path to your music folder
        music_folder = os.path.expanduser("~/Music")
        download_audio(youtube_url, music_folder)
    else:
        print("Invalid choice. Please enter 1 for video or 2 for audio.")
