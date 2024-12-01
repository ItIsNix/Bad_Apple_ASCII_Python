from ascii import convert_image_to_ascii
from frames import extract_frames
from audio import extract_audio
import os
import time
import playsound
import ctypes

ctypes.windll.kernel32.SetConsoleTitleW("Bad Apple with the funny snake language")

video, audio = 'vid.mp4', 'bad apple.mp3'
frame_dir, fps = 'bad apple', 30

print('Extracting frames')
extract_frames(video, frame_dir, fps, 180, 135)
extract_audio(video, audio)
print('Preloading frames')

ascii_frames = []
for frame in os.listdir(f'Output/{frame_dir}'):
    ascii_frames.append(convert_image_to_ascii(f'Output/{frame_dir}/{frame}', 180))

input('Frames preloaded!\nPress Enter to start')

playsound.playsound(f'Output/{audio}', False)

for ascii_frame in ascii_frames:
    print(ascii_frame, '\n')
    time.sleep(1/(fps*1.15))

print('End of video.')
