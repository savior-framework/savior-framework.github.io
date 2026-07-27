from moviepy.editor import VideoFileClip
import moviepy.video.fx.all as vfx

input_video = "demo_wan2.2.mp4" # Thay bằng đường dẫn file của bạn
output_video = "wan2.2_propose.mp4"
target_duration = 5.0 # số giây bạn muốn

# Tải video
clip = VideoFileClip(input_video)

# Tính toán hệ số tốc độ (speed_factor)
speed_factor = clip.duration / target_duration

# Tua nhanh video
fast_clip = clip.fx(vfx.speedx, speed_factor)

# Lưu video mới (bỏ âm thanh hoặc giữ qua audio=False/True)
fast_clip.write_videofile(output_video, codec="libx264", audio=False)