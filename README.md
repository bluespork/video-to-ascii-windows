# Video to ASCII for Windows

Convert video clips into ASCII art using Python.

## Requirements
- Python 3.6+
- Install dependencies:
  ```bash
  pip install -r requirements.txt
  ```

## Usage

1. **Convert video to ASCII text file**:
   ```bash
   python video_to_ascii_windows.py input_video.mp4
   ```
   This generates `ascii_video.txt`.

2. **Play the generated ASCII video**:
   ```bash
   python play_ascii.py
   ```
   Plays the ASCII video in the terminal.

## Notes
- This script dynamically adjusts to your terminal size and works across resolutions.
- **Best results are achieved on a 4K resolution**. Lower resolutions (e.g., 1080p) will still work but with reduced detail.
- For the best viewing experience, maximize your terminal window.
