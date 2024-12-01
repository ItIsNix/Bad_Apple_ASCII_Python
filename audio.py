from moviepy import VideoFileClip

def extract_audio(video_path, audio_path):
    video = VideoFileClip(video_path)
    audio = video.audio
    audio.write_audiofile(f'Output/{audio_path}')

    video.close()
    audio.close()
