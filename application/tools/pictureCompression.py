import os
from PIL import Image

def compress_image(infile, mb=60, step=10, quality=80):
    """不改变图片尺寸压缩到指定大小
    :param infile: 压缩源文件
    :param mb: 压缩目标，KB
    :param step: 每次调整的压缩比率
    :param quality: 初始压缩比率
    :return: outfile: 压缩文件后的文件
    """
    o_size = os.path.getsize(infile) / 1024
    if o_size <= mb:
        return infile

    outfile = infile.replace('.jpg', '_compressed.jpg')  # 新的输出文件名

    while o_size > mb and quality >= 0:
        im = Image.open(infile)
        im.save(outfile, optimize=True, quality=quality)
        o_size = os.path.getsize(outfile) / 1024

        if quality - step < 0:
            break
        quality -= step

    return outfile
