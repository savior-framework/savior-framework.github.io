import cv2
from pathlib import Path

input_video = "real_robot.mp4"
output_dir = Path("frames_real_robot_gen")
frame_interval = 3  # lấy 1 frame mỗi 5 frame

output_dir.mkdir(parents=True, exist_ok=True)

cap = cv2.VideoCapture(input_video)
if not cap.isOpened():
    raise RuntimeError(f"Cannot open video: {input_video}")

frame_idx = 0
saved = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    if frame_idx % frame_interval == 0:
        out_path = output_dir / f"frame_{frame_idx:06d}.png"
        cv2.imwrite(str(out_path), frame)
        saved += 1

    frame_idx += 1

cap.release()
print(f"Total frames: {frame_idx}, saved: {saved} -> {output_dir}/")
