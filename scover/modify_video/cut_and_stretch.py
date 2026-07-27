#!/usr/bin/env python3
"""Cut first N seconds, then stretch to target duration (slow-mo)."""
import subprocess

input_video = "wan2.6_propose_fix.mp4"
cut_video = "wan2.6_propose_2s.mp4"
output_video = "wan2.6_propose_5s.mp4"

cut_seconds = 2.5
target_duration = 5.2
slow_factor = target_duration / cut_seconds  # 2.5x slower

# 1) Cut first 2s
subprocess.run(
    [
        "ffmpeg", "-y",
        "-i", input_video,
        "-t", str(cut_seconds),
        "-c:v", "libx264",
        "-pix_fmt", "yuv420p",
        "-movflags", "+faststart",
        "-an",
        cut_video,
    ],
    check=True,
)

# 2) Stretch 2s -> 5s (setpts slows video)
subprocess.run(
    [
        "ffmpeg", "-y",
        "-i", cut_video,
        "-filter:v", f"setpts={slow_factor}*PTS",
        "-c:v", "libx264",
        "-pix_fmt", "yuv420p",
        "-movflags", "+faststart",
        "-an",
        output_video,
    ],
    check=True,
)

print(f"Cut:     {cut_video} ({cut_seconds}s)")
print(f"Stretched: {output_video} ({target_duration}s, {slow_factor}x slower)")
