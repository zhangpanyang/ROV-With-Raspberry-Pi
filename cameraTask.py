import time
import picamera

# 初始化相机
with picamera.PICamera() as camera:
    # 设置相机参数（可选）
    camera.resolution = (320, 240)  # 设置分辨率
    camera.framerate = 25  # 设置帧率
    
    # 等待相机启动（可选）
    time.sleep(2)

    # 开始录制视频
    camera.start_recording('video.h264')
    print("Recording... Press Ctrl+C to stop.")
    
    try:
        # 录制 10 秒的视频
        camera.wait_recording(10)
    finally:
        # 停止录制
        camera.stop_recording()
        print("Recording stopped. Video saved as 'video.h264'.")
