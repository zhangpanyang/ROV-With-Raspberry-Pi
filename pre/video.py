import time
from moviepy import *
# from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip

def process():

    videoFileName = 'video.mp4'

    # 加载原始视频
    video = VideoFileClip(videoFileName)

    original_width, original_height = video.size
    fps = video.fps

    # 设置额外高度
    extra_height = 40
    new_height = original_height + extra_height

    # 创建文本区域
    text = "BONJOUR TOUT LE MONDE !"
    text_clip = TextClip(
        text=text,
        font="arial.ttf",
        font_size=24,
        color="white",
        bg_color="black",
        size=(original_width, extra_height),
        duration=video.duration
    )

    # 创建新的视频
    new_video = CompositeVideoClip([video, text_clip], size=(original_width, new_height))

    # 保存新视频
    new_video.write_videofile("output_video.mp4", codec="libx264", fps=fps)

    # 释放资源
    video.close()

process()