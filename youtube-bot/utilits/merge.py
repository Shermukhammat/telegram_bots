import subprocess
import time

class ManualMerge:
    def __init__(self, save_path = 'data') -> None:
        self.path = save_path

    def merge(self, video_file : str = None, audio_file : str = None, output_file : str = "out.mp4"):
        command = f"ffmpeg -i {self.path}/{video_file} -i {self.path}/{audio_file} -c:v copy -c:a aac {self.path}/{output_file}"
        try:
            subprocess.run(command, shell=True, capture_output=True, text=True)
            return True
        except:
            return False



if __name__ == '__main__':
    start = time.time()

    manual_merge = ManualMerge()
    manual_merge.merge(video_file='test.mp4', audio_file = 'audio.webm', output_file = 'out_test.mp4')
    
    end = time.time()
    print(round(end - start, 1), "sec")