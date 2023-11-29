

import cv2
import os

def save_frames_to_folder(chunk, chunk_index, temp_dir):
    """
    Saves frames in a chunk to a dedicated folder within the temporary directory.
    """
    chunk_folder = os.path.join(temp_dir, f"chunk_{chunk_index}")
    os.makedirs(chunk_folder, exist_ok=True)
    
    
    for i, frame in enumerate(chunk):
        frame_path = os.path.join(chunk_folder, f"frame_{i}.jpg")
        cv2.imwrite(frame_path, frame)

    return chunk_folder
