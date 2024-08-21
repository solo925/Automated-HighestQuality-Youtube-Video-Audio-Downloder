# Automated-HighestQuality-Youtube-Video-Audio-Downloder

# YouTube Downloader Script

This Python script allows you to download high-quality videos or audio from YouTube using `yt-dlp`. It is configured to run from any directory in your terminal, utilizing a virtual environment for dependency management.

## Features

- Download YouTube videos in the highest available quality.
- Download audio-only versions of YouTube videos.
- Run the script from any directory in your terminal.

## Prerequisites

pip install requirements.txt

- Linux-based operating system (Tested on Parrot OS)

## Setup Instructions

### 1. Clone the Repository

```bash
git clone <repository_url>
cd <repository_name>
```

### 2. Create and Activate Virtual Environment

Create a virtual environment to manage dependencies.

```bash
python3 -m venv myenv
source myenv/bin/activate
```

### 4. Modify the Script

Ensure the shebang (`#!`) at the top of the script points to the Python interpreter in your virtual environment.

Open `youtube.py` and verify the first line:

```bash
#!/path/to/your/virtualenv/bin/python
```

Replace `/path/to/your/virtualenv/bin/python` with the actual path to the Python interpreter in your virtual environment.

### 5. Make the Script Executable

Grant execute permissions to the script:

```bash
chmod +x /path/to/youtube.py
```

### 6. Create a Symlink for Global Access

To run the script from anywhere in your terminal, create a symbolic link in `/usr/local/bin`:

```bash
sudo ln -s /path/to/youtube.py /usr/local/bin/youtube
```

### 7. Verify Installation

To verify that the setup is correct, run the following command from any directory:

```bash
youtube --version
```

If the command executes without errors, the setup is complete.

## Usage Instructions

To download a video or audio file, simply use the following commands:

### Download Video

```bash
youtube <video_url>

option 1
```

### Download Audio

option 2

## Troubleshooting

### `ModuleNotFoundError: No module named 'yt_dlp'`

- Ensure that the script's shebang points to the Python interpreter inside your virtual environment.
- Verify that `yt-dlp` is installed in the active virtual environment with:
  ```bash
  pip show yt_dlp
  ```

### `bash: /usr/local/bin/youtube: cannot execute: required file not found`

- Double-check the path in the shebang line at the top of your script.
- Ensure that the symbolic link is correctly pointing to your script.

## License

This project is licensed under the MIT License.

## Contributing

Feel free to open issues or submit pull requests with improvements or new features.

## Acknowledgments

- Thanks to the developers of `yt-dlp` for the amazing download tool.

```

### Explanation:
- **Prerequisites**: Lists the required software.
- **Setup Instructions**: Guides through the steps of setting up the script, including virtual environment creation, dependency installation, and creating a symlink for easy execution.
- **Usage Instructions**: Explains how to use the script for downloading videos and audio.
- **Troubleshooting**: Provides solutions to common issues that might occur.
- **License & Contributing**: Basic sections for open-source projects.

Feel free to customize this `README.md` to fit your project needs!
```
