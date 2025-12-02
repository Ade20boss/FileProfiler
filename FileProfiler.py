"""
A collection of utility functions for file statistics computations, dictionary operations,
and data formatting.

This module contains functions to perform common operations such as converting file sizes to
megabytes, finding keys in dictionaries by their values, formatting timestamps, and calculating file
statistics for a directory. The `calc_statistics` function analyzes files in a given directory to
categorize them based on types such as images, documents, or others, and retrieves statistical
details like total size, counts, and the newest file in each category.
"""
import os
import re
from datetime import datetime

def convert_to_megabytes(size_in_bytes):
    """
    Converts a given size in bytes to megabytes with precision up to two decimal points.

    This function takes an input size in bytes and converts it into megabytes by
    dividing it by the number of bytes in a megabyte (1024 * 1024). The result
    is rounded to two decimal places.

    :param size_in_bytes: The size in bytes to be converted.
    :type size_in_bytes: int
    :return: The converted size in megabytes, rounded to two decimal places.
    :rtype: float
    """
    return round(size_in_bytes / (1024 * 1024), 5)

def find_key_dict(dictionary, value):
    """
    Find the key in a dictionary corresponding to the given value.

    This function iterates through the key-value pairs of a dictionary to find
    the first occurrence of a specified value. If the value is found, the
    associated key is returned. If no such value exists, the function returns
    None.

    :param dictionary: The dictionary to search in.
    :type dictionary: dict
    :param value: The value to be matched to a key.
    :return: The key associated with the given value, or None if the value
        doesn't exist in the dictionary.
    :rtype: str or None
    """
    for key, val in dictionary.items():
        if val == value:
            return key
    return None

def format_date(timestamp):
    """
    Converts a given timestamp to a human-readable UTC date-time string.

    This function takes a Unix timestamp (seconds since epoch) as input and
    returns a formatted date-time string in UTC. The output format is
    "YYYY-Mon-DD HH:MM:SS".

    :param timestamp: Unix timestamp value representing time in seconds since the
        epoch.
    :type timestamp: int

    :return: A formatted UTC date-time string in the "YYYY-Mon-DD HH:MM:SS" format.
    :rtype: str
    """
    utc_time = datetime.utcfromtimestamp(timestamp) #Converts seconds to utc time
    formated_datetime = utc_time.strftime("%Y-%b-%d %H:%M:%S") #Converts utc time to human readable format
    return formated_datetime

def find_three_largest(custom_dict):
    if len(custom_dict) < 1:
        return custom_dict
    if len(custom_dict) == 1:
        return f"{list(custom_dict.keys())[0]} - {list(custom_dict.values())[0]}MB"
    else:
        sorted_values = list(custom_dict.values())[:3] if len(custom_dict) >= 3 else list(custom_dict.values())
        sorted_values.sort(reverse=True)
        new_list = []
        for item in sorted_values:
            key = find_key_dict(custom_dict, item)
            new_list.append(f"{find_key_dict(custom_dict, item)} - {custom_dict[key]}MB")
        new_list.sort(reverse=True)
        return ", ".join(new_list)




def directory_audit(directory):
    """
    Calculates statistics of files in the given directory, categorizing them into images, documents,
    and other files. For each category, it calculates the total size (in megabytes),
    counts the number of files, and identifies the most recently modified file.

    :param directory: Path to the directory to scan for file statistics
    :type directory: str
    :return: None
    """
    images = {}
    images_sizes = {}
    documents = {}
    documents_sizes = {}
    others = {}
    others_sizes = {}
    music = {}
    music_sizes = {}
    videos = {}
    videos_sizes = {}
    code_scripts = {}
    code_scripts_sizes = {}
    archives = {}
    archives_sizes = {}
    directory_entries = os.scandir(directory)
    image_extension_pattern = re.compile(r"\.(jpg|jpeg|png)$")
    docs_extension_pattern = re.compile(r"\.(pdf|docx|xlsx|pptx)$")
    music_regex = re.compile(r"\.(mp4|wav|flac)$")
    video_regex = re.compile(r"\.(mp4|mkv|mov|wmv|m4v)$")
    code_scripts_regex = re.compile(r"\.(py|js|cpp|java)$")
    archive_regex = re.compile(r"\.(zip|tar.gz|tar.bz2)$")
    for directory_entry in directory_entries:
        if directory_entry.is_file():
            if image_extension_pattern.search(directory_entry.name):
                images[directory_entry.name] = directory_entry.stat().st_ctime
                images_sizes[directory_entry.name] = convert_to_megabytes(directory_entry.stat().st_size)
            elif docs_extension_pattern.search(directory_entry.name):
                documents_sizes[directory_entry.name] = convert_to_megabytes(directory_entry.stat().st_size)
                documents[directory_entry.name] = directory_entry.stat().st_ctime
            elif music_regex.search(directory_entry.name):
                music_sizes[directory_entry.name] = convert_to_megabytes(directory_entry.stat().st_size)
                music[directory_entry.name] = directory_entry.stat().st_ctime
            elif video_regex.search(directory_entry.name):
                videos_sizes[directory_entry.name] = convert_to_megabytes(directory_entry.stat().st_size)
                videos[directory_entry.name] = directory_entry.stat().st_ctime
            elif code_scripts_regex.search(directory_entry.name):
                code_scripts_sizes[directory_entry.name] = convert_to_megabytes(directory_entry.stat().st_size)
                code_scripts[directory_entry.name] = directory_entry.stat().st_ctime
            elif archive_regex.search(directory_entry.name):
                archives_sizes[directory_entry.name] = convert_to_megabytes(directory_entry.stat().st_size)
                archives[directory_entry.name] = directory_entry.stat().st_ctime
            else:
                others_sizes[directory_entry.name] = convert_to_megabytes(directory_entry.stat().st_size)
                others[directory_entry.name] = directory_entry.stat().st_ctime



    if not images:
        print("No images found in the directory.")
    else:
        print("__________________________________________________")
        print("Images:")
        print("")
        print(f"Found {len(images)} Image(s) taking up {sum(list(images_sizes.values()))}MB\n"
              f"Newest image: {find_key_dict(images, max(images.values()))}\n"
              f"({format_date(max((images.values())))}) Oldest Image: {find_key_dict(images, min(images.values()))} ({format_date(min((images.values())))})\n"
              f"Largest documents: {find_three_largest(images_sizes)}")
        print("__________________________________________________")
        print("")
    if not documents:
        print("No documents found in the directory.")
    else:
        print("__________________________________________________")
        print("Documents:")
        print("")
        print(f"Found {len(documents)} document(s) taking up {sum(list(documents_sizes.values()))}MB\n"
              f"Newest document: {find_key_dict(documents, max(documents.values()))} ({format_date(max(documents.values()))})\n"
              f"Oldest document: {find_key_dict(documents, min(documents.values()))} ({format_date(min((documents.values())))})\n"
              f"Largest documents: {find_three_largest(documents_sizes)}")
        print("__________________________________________________")
        print("")

    if not music:
        print("No music found in the directory.")
    else:
        print("__________________________________________________")
        print("Music:")
        print("")
        print(f"Found {len(music)} music taking up {sum(list(music_sizes.values()))}MB\n"
              f"Newest music: {find_key_dict(music, max(music.values()))} ({format_date(max(music.values()))})\n"
              f"Oldest music: {find_key_dict(music, min(music.values()))} ({format_date(min((music.values())))})\n"
              f"Largest music: {find_three_largest(music_sizes)}")
        print("__________________________________________________")
        print("")

    if not videos:
        print("No video found in the directory.")
    else:
        print("__________________________________________________")
        print("Videos:")
        print("")
        print(f"Found {len(videos)} video(s) taking up {sum(list(videos_sizes.values()))}MB\n"
              f"Newest video: {find_key_dict(videos, max(videos.values()))} ({format_date(max(videos.values()))})\n"
              f"Oldest video: {find_key_dict(videos, min(videos.values()))} ({format_date(min((videos.values())))})\n"
              f"Largest videos: {find_three_largest(videos_sizes)}")
        print("__________________________________________________")
        print("")

    if not code_scripts:
        print("No code/scripts found in the directory.")
    else:
        print("__________________________________________________")
        print("Code/Scripts:")
        print("")
        print(f"Found {len(code_scripts)} document(s) taking up {sum(list(code_scripts_sizes.values()))}MB\n"
              f"Newest  code/script: {find_key_dict(code_scripts, max(code_scripts.values()))} ({format_date(max(code_scripts.values()))})\n"
              f"Oldest code/script: {find_key_dict(code_scripts, min(code_scripts.values()))} ({format_date(min((code_scripts.values())))})\n"
              f"Largest code/scripts: {find_three_largest(code_scripts_sizes)}")
        print("__________________________________________________")
        print("")

    if not archives:
        print("No archive found in the directory.")
    else:
        print("__________________________________________________")
        print("Archives:")
        print("")
        print(f"Found {len(archives)} archive(s) taking up {sum(list(archives_sizes.values()))}MB\n"
              f"Newest Archive: {find_key_dict(archives, max(archives.values()))} ({format_date(max(archives.values()))})\n"
              f"Oldest Archive: {find_key_dict(archives, min(archives.values()))} ({format_date(min((archives.values())))})\n"
              f"Largest Archives: {find_three_largest(archives_sizes)}")
        print("__________________________________________________")
        print("")


    if not others:
        print("No other files found in the directory.")
    else:
        print("__________________________________________________")
        print("OTHER FILES:")
        print("")
        print(f"Found {len(others)} other file(s) taking up {sum(list(others_sizes.values()))}MB\n"
              f"Newest file: {find_key_dict(others, max(others.values()))} ({format_date(max(others.values()))})\n"
              f"Oldest document: {find_key_dict(others, min(others.values()))} ({format_date(min((others.values())))})\n"
              f"Largest documents: {find_three_largest(others_sizes)}")
        print("__________________________________________________")
        print("")

directory_audit("C:\\Users\\ASUS\\PycharmProjects\\New_beginning\\data_structures\\dictionaries")





