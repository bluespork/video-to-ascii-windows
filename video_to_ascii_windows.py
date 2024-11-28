import cv2
import shutil
import numpy as np

# Custom ASCII characters optimized for emphasizing midtones
ASCII_CHARS = " .:-=+*#%@"

def apply_histogram_equalization(frame):
    """
    Apply histogram equalization to enhance contrast dynamically.
    """
    # Convert to grayscale
    grayscale_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Apply histogram equalization
    equalized_frame = cv2.equalizeHist(grayscale_frame)
    return equalized_frame

def adaptive_brightness_mapping(frame):
    """
    Adjust brightness dynamically within localized regions for better detail.
    """
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    return clahe.apply(frame)

def blend_first_frames(current_frame, previous_frame, frame_count, blend_until=5, alpha=0.8):
    """
    Blend the first few frames for smoother transitions.
    :param current_frame: Current video frame.
    :param previous_frame: Previous video frame.
    :param frame_count: Current frame index.
    :param blend_until: Number of frames to blend.
    :param alpha: Weight of the current frame (0.0 to 1.0).
    :return: Blended frame for the first few frames or original frame afterward.
    """
    if frame_count <= blend_until and previous_frame is not None:
        return cv2.addWeighted(current_frame, alpha, previous_frame, 1 - alpha, 0)
    return current_frame

def frame_to_ascii(frame, width=600):
    """
    Convert a video frame to ASCII using adaptive brightness mapping.
    """
    # Apply histogram equalization
    equalized_frame = apply_histogram_equalization(frame)

    # Apply adaptive brightness mapping
    adaptive_frame = adaptive_brightness_mapping(equalized_frame)

    # Calculate height based on width and aspect ratio
    height, aspect_ratio = frame.shape[0], frame.shape[1] / frame.shape[0]
    new_height = int(width / aspect_ratio / 2)  # Adjust for 2:1 character aspect ratio

    # Resize the frame
    resized_frame = cv2.resize(adaptive_frame, (width, new_height))

    # Map each pixel to an ASCII character
    scale = 255 // (len(ASCII_CHARS) - 1)
    ascii_frame = [
        ASCII_CHARS[min(pixel // scale, len(ASCII_CHARS) - 1)]  # Safeguard index
        for row in resized_frame for pixel in row
    ]
    ascii_frame = ''.join(ascii_frame)

    # Return the ASCII frame split into lines
    return '\n'.join(
        ascii_frame[i:(i + width)] for i in range(0, len(ascii_frame), width)
    )

def video_to_ascii(video_path, output_path="ascii_video.txt"):
    """
    Convert a video to ASCII art optimized for the terminal with initial frame blending.
    """
    # Use the detected terminal width
    term_width, term_height = shutil.get_terminal_size()
    ascii_width = min(600, term_width - 2)  # Increased resolution

    print(f"Using ASCII width: {ascii_width}")

    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Error: Cannot open video file.")
        return

    fps = int(cap.get(cv2.CAP_PROP_FPS))
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    print(f"Video FPS: {fps}, Total Frames: {total_frames}")

    previous_frame = None  # Initialize the previous frame for blending
    with open(output_path, "w") as f:
        frame_count = 0
        while True:
            ret, frame = cap.read()
            if not ret:
                break

            # Blend the first few frames
            blended_frame = blend_first_frames(frame, previous_frame, frame_count, blend_until=5, alpha=0.8)
            previous_frame = blended_frame.copy()  # Save the current frame for the next iteration

            # Convert blended frame to ASCII
            ascii_art = frame_to_ascii(blended_frame, width=ascii_width)
            
            # Write frame as ASCII
            f.write(ascii_art)
            f.write("\n" + "=" * ascii_width + "\n")  # Frame separator
            
            frame_count += 1
            print(f"Processed frame {frame_count}/{total_frames}", end="\r")
    
    cap.release()
    print(f"\nASCII video saved to {output_path}")

# Example usage
video_to_ascii("input_video.mp4", output_path="ascii_video.txt")
