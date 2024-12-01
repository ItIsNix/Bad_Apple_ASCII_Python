import cv2
import os


def extract_frames(video_path, output_folder, new_fps=24, width=640, height=360):
    os.makedirs(f'Output/{output_folder}', exist_ok=True)

    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        raise Exception(f"Failed to open video file: {video_path}")

    orig_fps = cap.get(cv2.CAP_PROP_FPS)
    frame_interval = int(orig_fps / new_fps)

    frames = 0
    saved_frames = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        if frames % frame_interval == 0:
            resized_frame = cv2.resize(frame, (width, height))

            output_file = os.path.join(f'Output/{output_folder}', f"frame_{saved_frames:04d}.jpg")
            cv2.imwrite(output_file, resized_frame)

            saved_frames += 1

        frames += 1

    cap.release()
    print(f"Extracted {saved_frames} frames at {new_fps} FPS.")


