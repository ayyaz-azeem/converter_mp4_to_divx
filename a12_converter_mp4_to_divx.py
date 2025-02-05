import ffmpeg
import os
"""
def convert_to_divx(input_folder, output_folder):
    # Create output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)
    
    # Loop through all MP4 files in the input folder
    for file in os.listdir(input_folder):
        if file.endswith('.mp4'):
            input_path = os.path.join(input_folder, file)
            output_path = os.path.join(output_folder, os.path.splitext(file)[0] + '.divx')
            
            try:
                # Convert MP4 to DIVX
                (
                    ffmpeg
                    .input(input_path)
                    .output(output_path, vcodec='mpeg4', acodec='mp3')  # DIVX settings
                    .run(overwrite_output=True)
                )
                print(f"Converted: {file} -> {output_path}")
            except ffmpeg.Error as e:
                print(f"Error converting {file}: {e}")

# Replace with your input and output folder paths
input_folder = f"d:/new_coding/baby_videos"
output_folder = f"d:/new_coding/baby_videos/divx_output"

convert_to_divx(input_folder, output_folder)

"""
import ffmpeg
import os

def convert_to_divx(input_folder, output_folder):
    # Create output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)
    
    # Loop through all MP4 files in the input folder
    for file in os.listdir(input_folder):
        if file.endswith('.mp4'):
            input_path = os.path.join(input_folder, file)
            # Use .avi as the output file extension
            output_path = os.path.join(output_folder, os.path.splitext(file)[0] + '.avi')
            
            try:
                # Convert MP4 to DIVX
                (
                    ffmpeg
                    .input(input_path)
                    .output(output_path, vcodec='mpeg4', acodec='mp3')  # DIVX settings
                    .run(overwrite_output=True)
                )
                print(f"Converted: {file} -> {output_path}")
            except ffmpeg.Error as e:
                print(f"Error converting {file}: {e}")

# Replace with your input and output folder paths
input_folder = "d:/new_coding/baby_videos/"
output_folder = "d:/new_coding/baby_videos/divx_output"

convert_to_divx(input_folder, output_folder)

