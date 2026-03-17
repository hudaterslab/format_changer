import subprocess

input_file = r"C:\Users\jwyoo\Downloads\2026_03_06_16_46_29_ch3.ssf"
h264_file = r"C:\Users\jwyoo\Downloads\2026_03_06_16_46_29_ch3.h264"
mp4_file = r"C:\Users\jwyoo\Downloads\2026_03_06_16_46_29_ch3.mp4"

with open(input_file, "rb") as f:
    data = f.read()

# H264 start code 찾기
start_code = b'\x00\x00\x00\x01'
start = data.find(start_code)

if start == -1:
    print("H264 start code not found")
    exit()

print(f"H264 stream found at offset: {start}")

# H264 추출
with open(h264_file, "wb") as f:
    f.write(data[start:])

print("H264 extracted:", h264_file)

# ffmpeg로 mp4 변환
cmd = [
    "ffmpeg",
    "-y",
    "-framerate", "30",
    "-i", h264_file,
    "-c", "copy",
    mp4_file
]

subprocess.run(cmd)

print("MP4 created:", mp4_file)
