from moviepy.editor import VideoFileClip
import moviepy.video.fx.all as vfx

input_video = "demo_video.mp4"
output_video = "demo_video_cropped.mp4"
target_duration = 5.0

clip = VideoFileClip(input_video)

# Cắt 2cm (khoảng 76 pixel) ở dưới mỗi frame
def crop_bottom(get_frame, t):
    frame = get_frame(t)
    return frame[:-82, :, :]

cropped_clip = clip.fl(crop_bottom)

speed_factor = clip.duration / target_duration
fast_clip = cropped_clip.fx(vfx.speedx, speed_factor)

fast_clip.write_videofile(output_video, codec="libx264", audio=False)
