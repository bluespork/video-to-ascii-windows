# Video to ASCII for Windows

Convert video clips into ASCII art using Python.

## Requirements
- Python 3.6+
- Install dependencies:
  ```bash
  pip install -r requirements.txt
  ```

## Usage

1. **Prepare Your Video**:
   - Rename your video file to `input_video.mp4`.
   - Place the video in the same folder as the scripts.

2. **Convert video to ASCII text file**:
   ```bash
   python video_to_ascii_windows.py input_video.mp4
   ```
   This generates `ascii_video.txt`.

3. **Play the generated ASCII video**:
   ```bash
   python play_ascii.py
   ```
   Works in both Command Prompt and PowerShell.

## Notes
- This script dynamically adjusts to your Command Prompt or PowerShell window size and works across resolutions.
- **Best results are achieved on a 4K resolution**. Lower resolutions (e.g., 1080p) will still work but with reduced detail.
- For the best viewing experience, maximize your Command Prompt or PowerShell window.
