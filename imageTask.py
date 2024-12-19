from PIL import Image, ImageDraw, ImageFont

def add_text_to_bottom(image_path, text, font_path="arial.ttf", font_size=30, black_bar_height=60):
    """
    给图片底部添加黑色条，并在黑色条内居中显示文本。

    :param image_path: 原始图片的路径
    :param text: 要添加的文本
    :param font_path: 字体文件路径，默认使用 Arial 字体
    :param font_size: 字体大小，默认为 40
    :param black_bar_height: 黑色条的高度，默认为 100
    :return: 无返回，原始图像被修改
    """
    # 打开原始图像
    img = Image.open(image_path)

    # 获取原图的尺寸
    width, height = img.size

    # 创建一个新的图像，尺寸为原图的宽度和原图高度加上黑色区域的高度
    new_img = Image.new('RGB', (width, height + black_bar_height), (0, 0, 0))  # 创建黑色背景的新图像

    # 将原始图像粘贴到新图像的顶部
    new_img.paste(img, (0, 0))

    # 创建可绘制的对象
    draw = ImageDraw.Draw(new_img)

    # 定义字体和大小
    font = ImageFont.truetype(font_path, font_size)

    # 计算文本的宽度和高度
    text_width, text_height = draw.textsize(text, font=font)

    # 计算文本的位置，使其居中
    text_x = (width - text_width) // 2  # 使文本在x轴居中
    text_y = height + (black_bar_height - text_height) // 2  # 在黑色区域中垂直居中

    # 定义文字颜色（白色）
    text_color = (255, 255, 255)

    # 在黑色区域内绘制文本
    draw.text((text_x, text_y), text, font=font, fill=text_color)

    # 保存处理后的图片，覆盖原来的文件
    new_img.save(image_path)