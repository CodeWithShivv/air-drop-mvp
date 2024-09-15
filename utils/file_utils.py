# File utilities (e.g., file size, chunking)
import os

def get_file_size(file_path):
    return os.path.getsize(file_path)
