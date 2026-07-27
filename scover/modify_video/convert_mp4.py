import subprocess
import json

def get_video_duration(input_file):
    """Hàm lấy tổng thời lượng của video (tính bằng giây)"""
    cmd = [
        'ffprobe', '-v', 'quiet', '-print_format', 'json', 
        '-show_format', '-show_streams', input_file
    ]
    result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    data = json.loads(result.stdout)
    return float(data['format']['duration'])

def cut_last_second(input_file, output_file):
    try:
        # 1. Lấy tổng thời gian video gốc
        total_duration = get_video_duration(input_file)
        
        # 2. Tính thời gian kết thúc mới (trừ đi 1 giây)
        target_duration = total_duration - 1.5
        
        if target_duration <= 0:
            print("Lỗi: Video quá ngắn, không thể cắt bỏ 1 giây!")
            return

        print(f"Tổng thời lượng gốc: {total_duration}s -> Cắt còn: {target_duration}s")

        # 3. Chạy lệnh FFmpeg để cắt video
        # Sử dụng các tham số tối ưu độ nét và sửa lỗi fps/kích thước lẻ từ các bước trước của bạn
        command = [
            'ffmpeg',
            '-i', input_file,
            '-to', str(target_duration), # Cắt từ 0 đến giây thứ (Tổng - 1)
            '-vf', 'scale=trunc(iw/2)*2:trunc(ih/2)*2,fps=30', 
            '-r', '30',
            '-c:v', 'libx264',
            '-crf', '17',
            '-preset', 'slow',
            '-tune', 'animation',
            '-c:a', 'aac',
            output_file,
            '-y'
        ]
        
        subprocess.run(command, check=True)
        print(f"Đã cắt xong! File mới lưu tại: {output_file}")
        
    except Exception as e:
        print(f"Có lỗi xảy ra: {e}")

# Chạy thử nghiệm
cut_last_second("demo_terminal.mp4", "demo_terminal_cut.mp4")