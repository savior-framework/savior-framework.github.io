import subprocess

input_video = "savior_demovideo.mp4"
output_video = "recovery.mp4"

# 0:35 -> 1:10
start_time = "00:02:05"
duration = "00:02:21"  # 1:10 - 0:35 = 35s

subprocess.run(
    [
        "ffmpeg", "-y",
        "-ss", start_time,
        "-i", input_video,
        "-t", duration,
        "-c:v", "libx264",
        "-pix_fmt", "yuv420p",
        "-movflags", "+faststart",
        "-an",
        output_video,
    ],
    check=True,
)

print(f"Saved: {output_video}")
