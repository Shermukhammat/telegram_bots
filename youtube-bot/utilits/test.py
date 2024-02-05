# import subprocess
# import time

# start = time.time()
# # Example command to list files in the current directory
# command = f"ffmpeg -i data/video.mp4 -i data/audio.mp3 -c:v copy -c:a aac output.mp4"

# # Run the command
# result = subprocess.run(command, shell=True, capture_output=True, text=True)

# end = time.time()

# print(f"Run time : {end - start}\n\n")

# # Print the output
# print("Command Output:")
# print(result.stdout)


def write_log(file_path : str = None, log : str = 'New text'):
    """This function helps you write logs

    Args:
        file_path (str, optional): You wnated write logs file. Defaults to None.
        log (str, optional): log text. Defaults to 'New text'.
    """
    with open(file_path, 'a') as file:
        file.write(log+"\n")
        file.close()
