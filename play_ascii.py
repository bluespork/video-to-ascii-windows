import time
import os
import sys

# Path to the ASCII text file
ascii_file_path = "ascii_video.txt"

# Frame width (should match the width used in video_to_ascii)
frame_width = 100

def play_ascii_video(file_path, original_duration=15.0):
    """
    Play ASCII video from a text file, synchronized to match the original video duration.
    :param file_path: Path to the ASCII video text file
    :param original_duration: Original video duration in seconds
    """
    with open(file_path, "r") as f:
        # Split file into frames using the separator (adjust separator if needed)
        frames = f.read().split("=" * frame_width)

    # Calculate the target FPS based on the number of frames and original duration
    total_frames = len(frames)
    fps = total_frames / original_duration
    frame_time = 1 / fps  # Time per frame in seconds

    print(f"Total Frames: {total_frames}, Calculated FPS: {fps:.2f}")

    # Hide cursor for smoother playback
    os.system("tput civis")

    try:
        print("Starting playback... (Press Ctrl+C to stop)")
        for frame in frames:
            start_time = time.time()  # Record the start time of the frame

            # Move the cursor to the top and render the frame
            sys.stdout.write(f"\033[H{frame}")
            sys.stdout.flush()

            # Calculate elapsed time and delay to match target frame time
            elapsed_time = time.time() - start_time
            if elapsed_time < frame_time:
                time.sleep(frame_time - elapsed_time)

    except KeyboardInterrupt:
        print("\nPlayback stopped.")

    finally:
        # Show cursor again after playback ends
        os.system("tput cnorm")

# Play the ASCII video with original duration set
play_ascii_video(ascii_file_path, original_duration=15.0)  # Set the original video duration in seconds
