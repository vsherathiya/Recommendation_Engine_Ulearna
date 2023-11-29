
# import cv2
# import os
# import tempfile
# from multiprocessing import Pool
# from video_processing import save_frames_to_folder

# def split_video_into_chunks(video_path, chunk_size):
#     """
#     Splits a video into chunks of frames.
#     """
#     cap = cv2.VideoCapture(video_path)
#     if not cap.isOpened():
#         print("Error: Unable to open video file.")
#         return []

#     chunks = []
#     current_chunk = []
#     frame_count = 0

#     while True:
#         ret, frame = cap.read()
#         if not ret:
#             if current_chunk:
#                 chunks.append(current_chunk)
#             break

#         current_chunk.append(frame)
#         frame_count += 1

#         if frame_count % chunk_size == 0:
#             chunks.append(current_chunk)
#             current_chunk = []

#     cap.release()
#     return chunks

# def process_video_chunks(video_path, num_processes=4):
#     """
#     Processes the video by splitting it into chunks and saving frames of each chunk in separate folders.
#     """
#     chunks = split_video_into_chunks(video_path, chunk_size=100)  # Customize the chunk size as needed
#     temp_dir = tempfile.mkdtemp()  # Create a temporary directory

#     with Pool(num_processes) as pool:
#         # Save each chunk in a separate process
#         chunk_folders = pool.starmap(save_frames_to_folder, [(chunk, i, temp_dir) for i, chunk in enumerate(chunks)])

#     print(f"Saved frames in temporary folders: {chunk_folders}")
#     # Return the path to the temporary directory containing all the chunk folders
#     return temp_dir

# if __name__ == "__main__":
#     temp_directory = process_video_chunks(r"D:\Recommendation_Engine\Dataset\01safe.mp4")
#     print(f"Frames saved in {temp_directory}")


# main_script.py

# import cv2
# import os
# import tempfile
# from multiprocessing import Pool
# from video_processing import save_frames_to_folder

# def split_video_into_time_chunks(video_path, seconds_per_chunk):
#     """
#     Splits a video into chunks based on time (in seconds).
#     """
#     cap = cv2.VideoCapture(video_path)
#     if not cap.isOpened():
#         print("Error: Unable to open video file.")
#         return []

#     fps = cap.get(cv2.CAP_PROP_FPS)  # Frames per second
#     frames_per_chunk = int(fps * seconds_per_chunk)
#     chunks = []

#     while True:
#         current_chunk = []
#         for _ in range(frames_per_chunk):
#             ret, frame = cap.read()
#             if not ret:
#                 break
#             current_chunk.append(frame)

#         if not current_chunk:
#             break
#         chunks.append(current_chunk)

#     cap.release()
#     return chunks

# def process_video_chunks(video_path, num_processes=3):
#     """
#     Processes the video by splitting it into time-based chunks and saving frames of each chunk in separate folders.
#     """
#     chunks = split_video_into_time_chunks(video_path, 5)  # 5 seconds per chunk
#     temp_dir = tempfile.mkdtemp()  # Create a temporary directory

#     with Pool(num_processes) as pool:
#         # Save each chunk in a separate process
#         chunk_folders = pool.starmap(save_frames_to_folder, [(chunk, i, temp_dir) for i, chunk in enumerate(chunks)])

#     print(f"Saved frames in temporary folders: {chunk_folders}")
#     # Return the path to the temporary directory containing all the chunk folders
#     return temp_dir

# if __name__ == "__main__":
#     temp_directory = process_video_chunks(r"D:\Recommendation_Engine\Dataset\01safe.mp4")
#     print(f"Frames saved in {temp_directory}")

########################################################################################################################
# main_script.py
# import cv2
# import os
# from multiprocessing import Pool
# from video_processing import save_frames_to_folder

# def split_video_into_time_chunks(video_path, seconds_per_chunk):
#     """
#     Splits a video into chunks based on time (in seconds).
#     """
#     cap = cv2.VideoCapture(video_path)
#     if not cap.isOpened():
#         print("Error: Unable to open video file.")
#         return []

#     fps = cap.get(cv2.CAP_PROP_FPS)  # Frames per second
#     frames_per_chunk = int(fps * seconds_per_chunk)
#     chunks = []

#     while True:
#         current_chunk = []
#         for _ in range(frames_per_chunk):
#             ret, frame = cap.read()
#             if not ret:
#                 break
#             current_chunk.append(frame)

#         if not current_chunk:
#             break
#         chunks.append(current_chunk)

#     cap.release()
#     return chunks

# def process_video_chunks(video_path, output_dir, num_processes=3):
#     """
#     Processes the video by splitting it into time-based chunks and saving frames of each chunk in separate folders.
#     """
#     if not os.path.exists(output_dir):
#         os.makedirs(output_dir)

#     chunks = split_video_into_time_chunks(video_path, 5)  # 5 seconds per chunk

#     with Pool(num_processes) as pool:
#         # Save each chunk in a separate process
#         chunk_folders = pool.starmap(save_frames_to_folder, [(chunk, i, output_dir) for i, chunk in enumerate(chunks)])

#     print(f"Saved frames in folders: {chunk_folders}")
#     # Return the path to the directory containing all the chunk folders
#     return output_dir

# if __name__ == "__main__":
#     output_directory = "Frames"  # Replace with your desired path
#     temp_directory = process_video_chunks(r"D:\Recommendation_Engine\Dataset\01safe.mp4", output_directory)
#     print(f"Frames saved in {temp_directory}")


####################################################################################


# main_script.py

import cv2
import os
import multiprocessing
from multiprocessing import Pool
from video_processing import save_frames_to_folder

def get_video_info(video_path):
    """
    Get video information such as length, frame rate, and frame size.
    """
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Error: Unable to open video file.")
        return None

    length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    
    cap.release()
    
    return length, fps, frame_width, frame_height

def calculate_chunk_params(video_path, num_processes):
    """
    Calculate chunk parameters based on video length, fps, frame size, and CPU count.
    """
    length, fps, frame_width, frame_height = get_video_info(video_path)
    print(length, fps, frame_width, frame_height)
    # Calculate seconds per chunk based on video length, CPU count, and target number of chunks
    seconds_per_chunk = length / (num_processes * 2 * fps)

    return seconds_per_chunk, frame_width, frame_height

def split_video_into_time_chunks(video_path, seconds_per_chunk):
    """
    Splits a video into chunks based on time (in seconds).
    """
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Error: Unable to open video file.")
        return []

    fps = cap.get(cv2.CAP_PROP_FPS)  # Frames per second
    frames_per_chunk = int(fps * seconds_per_chunk)
    chunks = []

    while True:
        current_chunk = []
        for _ in range(frames_per_chunk):
            ret, frame = cap.read()
            if not ret:
                break
            current_chunk.append(frame)

        if not current_chunk:
            break
        chunks.append(current_chunk)

    cap.release()
    return chunks

def process_video_chunks(video_path, output_dir, num_processes):
    """
    Processes the video by splitting it into time-based chunks and saving frames of each chunk in separate folders.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    seconds_per_chunk, frame_width, frame_height = calculate_chunk_params(video_path, num_processes)
    chunks = split_video_into_time_chunks(video_path, seconds_per_chunk)

    with Pool(num_processes) as pool:
        # Save each chunk in a separate process
        chunk_folders = pool.starmap(save_frames_to_folder, [(chunk, i, output_dir) for i, chunk in enumerate(chunks)])

    print(f"Saved frames in folders: {chunk_folders}")
    # Return the path to the directory containing all the chunk folders
    return output_dir

if __name__ == "__main__":
    output_directory = r"Frames3"  # Replace with your desired path
    num_processes = multiprocessing.cpu_count()
    print(num_processes)
    temp_directory = process_video_chunks(r"D:\Recommendation_Engine\Dataset\01safe.mp4", output_directory, num_processes)
    print(f"Frames saved in {temp_directory}")

