import os
import sys

# Add the current directory to the system path
sys.path.append(os.path.dirname(__file__))  

from main import extract_faces, swap_faces, compile_video  

def main():
    # Define directories
    base_dir = os.path.dirname(__file__)  # Get the current directory
    uploads_dir = os.path.join(base_dir, "uploads")
    workspace_dir = os.path.join(base_dir, "workspace")
    data_src = os.path.join(workspace_dir, "data_src")  # Directory for source frames
    data_dst = os.path.join(workspace_dir, "data_dst")  # Directory for user faces
    model_dir = os.path.join(workspace_dir, "model")    # Directory to save model training data
    final_output_path = os.path.join(base_dir, "output_video.mp4")  # Final output video path

    # Step 1: Extract faces from user image
    print("Extracting faces from user images...")
    extract_faces(uploads_dir, data_dst)

    # Step 2: Extract frames from the original video
    original_video_path = os.path.join(base_dir, "MF 8055 Boss Magnatrac Tractor Baki Sab Tractoro Hai ye #Massey Hai Sabka Boss.mp4")
    if not os.path.exists(original_video_path):
        print(f"Original video not found at {original_video_path}. Please add it to the folder.")
        return

    print("Extracting frames from the original video...")
    extract_faces(original_video_path, data_src)

    # Step 3: Swap faces
    print("Swapping faces...")
    swap_faces(data_src, data_dst, model_dir)

    # Step 4: Compile the output video
    print("Compiling the output video...")
    compile_video(model_dir, final_output_path)

    print(f"Face-swapped video saved at: {final_output_path}")

if __name__ == "__main__":
    main()
