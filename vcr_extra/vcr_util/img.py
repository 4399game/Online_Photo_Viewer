import os
import random
from PIL import Image
simple_w = 1366
NAME_CHOISE = 'ILOVEYOU'
#
def simple_image(image, save_path, flag):
    img_type = 'JPEG'
    if flag == 'save':
        im = Image.open(image)
        return simple_save(im, save_path, img_type)
    if flag == 'comp':
        im = Image.open(image)
        return simple_comp(im, save_path ,img_type)

def new_name():
    simple_name = 'VcrT_美图'
    return simple_name + '_' + str(random.randint(1, 100000)) + '_' + random.choice(NAME_CHOISE)

def new_size(w, h):
    ratio = False
    if (w > 8888) or (h > 8888):
        ratio = 0.6
    elif (w > 4666) or (h > 4666):
        ratio = 0.8
    if ratio != False:
        return (int(w * ratio), int(h * ratio))
    return ratio

def simple_save(im, save_path, img_type):
    save_path = os.path.join(save_path, new_name() + '.' + img_type)
    im.save(save_path, img_type)
    return save_path.replace('\\', '/')

def simple_comp(im, save_path , img_type):
    w = im.size[0]
    h = im.size[1]
    comp_size = new_size(w, h)
    if im.mode == 'RGBA':
        im = del_alpha(im)
    if comp_size != False:
        im = im.resize(comp_size, Image.BILINEAR)
    return simple_save(im, save_path, img_type)

def del_alpha(im):
    r, g, b, a = im.split()
    im = Image.merge('RGB', (r, g, b))
    return im

"""
    PIL 插值 参数:
        NEAREST : 最近邻插值
        BILINEAR: 双线性插值
        BICUBIC : 双立方插值
        ANTIALIAS: 高质量采样器
"""