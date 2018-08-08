from PIL import Image
import os
import time
import datetime
from vcr_apps.vcr_conf import ( i_small, i_tiny,
    i_middle, i_big, i_large, i_huge, i_massive
)
# import cv2
from skimage import io, transform
from vcr_apps.kuukann.models import ImgMsg

def img_compress(image, save_path, img_type):
    dt = time.time()
    img = io.imread(image)
    w = img.shape[0]  #图片宽度
    h = img.shape[1]  #图片高度
    px = img.size     #像素个数
    # 计算 压缩率
    ratio = get_comp_ratio(w, h)
    ratio = compensate_ratio(ratio, w, h, img_type)
             
    n_w, n_h = int( w*ratio), int( h*ratio)
    # 命名
    img_file_name = str(n_w)+ '_' + str(n_h) + '_' + str(time.time())+ '.'+ img_type
    save_path = os.path.join(save_path, img_file_name)

    # 压缩
    img = transform.resize(img, (n_w, n_h), order = 1)

    io.imsave(save_path, img)
    time_dlt = time.time() - dt

    img_msg = ImgMsg()
    img_msg.w = w
    img_msg.h = h
    img_msg.px = px
    img_msg.name = img_file_name
    img_msg.fmt = img_type
    img_msg.comp_time = time_dlt
    img_msg.ratio = ratio
    datetime.timedelta()
    img_msg.content = 'transform.resize(img, new_size, order = 1) - 分割 -' + str(image)
    img_msg.save()

    return save_path.replace('\\','/'), (n_w, n_h)

"""
    png-8:
        img_obj = Image.open(file_path)
        img_arr = np.array(img_obj).astype(np.unit8)
        
# 压缩图片
def img_compress(image, save_path):
    print('----------------------------- start ------------------------------')
    print('image = ', image)
    # 加载
    img = Image.open(image)
    img_type = img.format
    w = img.size[0]
    h = img.size[1]
    # 计算 压缩率
    ratio = get_comp_ratio(w, h)
    ratio = compensate_ratio(ratio, w, h, img_type)
             
    new_size = ( int( w*ratio), int( h*ratio) )
    # 命名
    img_file_name = str(new_size)+ '_'+ str(time.time())+ '.'+ img_type
    save_path = os.path.join(save_path, img_file_name)
    print('保存的路径 = ', save_path)
    # 压缩
    img = img.resize(new_size, Image.ANTIALIAS)
    # 储存
    img.save(save_path, img_type)
    print('比率 =', ratio, ' , 压缩后 size = ', img.size, ', save_path =', save_path)
    print('----------------------------- ending ------------------------------')
    return save_path.replace('\\','/'), new_size
    
def img_compress(image, save_path):
    image = 'save\\90.png'
    im = cv2.imread(image, cv2.IMREAD_UNCHANGED)
    size = im.shape
    img_type = im.dtype
    px = 'png'
    print('size = ', size, 'px = ', px)
    w = size[0]
    h = size[1]
    # Ratio
    ratio = get_comp_ratio(w, h)
    ratio = compensate_ratio(ratio, w, h, img_type)
             
    new_size = ( int( w*ratio), int( h*ratio) )
    # Name
    img_file_name = str(new_size)+ '_'+ str(time.time())+ '.'+ img_type
    save_path = os.path.join(save_path, img_file_name)

    # Comp
    res = cv2.resize(im, new_size, [int(cv2.IMWRITE_PNG_COMPRESSION),9])
    cv2.imwrite(save_path, res)

    print('----------------------------- ending ------------------------------')
    return save_path.replace('\\','/'), new_size
    
文档：
    cv2.IMREAD_COLOR : 默认使用该种标识。加载一张彩色图片，忽视它的透明度。
    cv2.IMREAD_GRAYSCALE : 加载一张灰度图。
    cv2.IMREAD_UNCHANGED : 加载图像，包括它的Alpha通道
    
def img_compress_simple(image):
    # 加载
    img = Image.open(image)
    img_type = img.format
    w = img.size[0]
    h = img.size[1]
    # 计算 压缩率
    ratio = get_comp_ratio(w, h)
    ratio = compensate_ratio(ratio, w, h, img_type)
    new_size = ( int( w*ratio), int( h*ratio) )
    # 压缩
    img = img.resize(new_size, Image.ANTIALIAS)
    return img, new_size
    
16 / 9 = 1.7
3 / 2 = 1.5
4 / 3 = 1.2
1 / 1 = 1
3 / 4 = 0.8
2 / 3 = 0.5
9 / 16 = 0.3
r_less      =    9 / 21  # ;// 0.428
r_mini     =    9 / 16   # ;// 0.562
r_tiny      =    2 / 3   # ;// 0.666
r_small     =    3 / 4   # ;// 0.75
r_middle    =    1 / 1   # ;// 1
r_big       =    4 / 3   # ;// 1.333
r_large     =    3 / 2   # ;// 1.5
r_huge    =    16 / 9    # ;// 1.777
r_massive   =    21 / 9  # ;// 2.333
"""
def get_img_msg(image):
    img = Image.open(image)
    return img.size[0], img.size[1], img.format

def compensate_ratio(ratio, w, h, fmt):
    fmt = fmt.upper()
    if (fmt == 'JPEG') or (fmt == 'JPG'):
        if w < i_big:
            ratio = 0.86
        elif (w < i_huge) and (w > i_big):
            ratio += 0.1
        elif (w > i_huge) and (w < i_massive):
            ratio += 0.0618
        else:
            ratio -= 0.1
    elif (fmt == 'PNG'):
        if w < i_big:
            ratio -= 0.05
        elif (w < i_huge) and (w > i_big):
            ratio -= 0.062
        elif (w > i_huge) and (w < i_massive):
            ratio -= 0.075
        else:
            ratio -= 0.09
    else:
        print(fmt)
    return ratio

def get_comp_ratio(w, h):
    print('i_middle = ', i_middle, 'i_big = ', i_big, 'i_huge = ', i_huge, 'i_massive = ', i_massive, 'i_small = ', i_small, 'i_tiny = ', i_tiny)
    i_ratio = w / h
    if i_ratio > 1.04:
        if (i_ratio < 1.2):
            print('1_iratio = ', i_ratio)
            if w > i_large:
                if w > i_massive:
                    return 0.09
                return 0.3
            else:
                return 0.5
        elif (i_ratio >= 1.2 ) and (i_ratio < 1.56):
            print('2_iratio = ', i_ratio)
            if w > i_large :
                if w > i_massive:
                    return 0.24
                return 0.32
            else:
                return 0.5
        elif (i_ratio >= 1.56) and (i_ratio < 2.0):
            print('3_iratio = ', i_ratio)
            if w > i_large:
                if w > i_massive:
                    return 0.2
                return 0.4
            else:
                return 0.6
        else:
            print('4_iratio = ', i_ratio)
            if w > i_large:
                if w > i_massive:
                    return 0.4
                return 0.5
            else:
                return 0.6
    elif i_ratio < 0.96:
        if (i_ratio > 0.84):
            print('5_iratio = ', i_ratio)
            if h > i_large:
                if h > i_massive:
                    return 0.09
                return 0.3
            else:
                return 0.4
        elif (i_ratio <= 0.84 ) and (i_ratio > 0.68):
            print('6_iratio = ', i_ratio)
            if h > i_large :
                if h > i_massive:
                    return 0.2
                return 0.4
            else:
                return 0.6
        elif (i_ratio <= 0.68) and (i_ratio > 0.5):
            print('7_iratio = ', i_ratio)
            if h > i_large:
                if h > i_massive:
                    return 0.2
                return 0.4
            else:
                return 0.6
        elif (i_ratio <= 0.5) and (i_ratio > 0.343):
            print('8_iratio = ', i_ratio)
            if h > i_large:
                if h > i_massive:
                    return 0.32
                return 0.43
            else:
                return 0.7
        else:
            print('9_iratio = ', i_ratio)
            if h > i_large:
                if h > i_massive:
                    return 0.38
                return 0.56
            else:
                return 0.6
    else:
        print('10_iratio = ', i_ratio)
        if w > i_large:
            if w > i_massive:
                return 0.08
            return 0.3
        else:
            return 0.5

"""
    level = 0
    ratio_list.append(i_ratio)
    ratio_list = list(set(ratio_list))
    for k in range(len(ratio_list)):
        if(ratio_list[k] == i_ratio):
            level = k
    if k > 5:
        if k > 8:
            pass
        elif k < 8:
            pass
        else:
            return 0.4
    elif k < 5
    
def get_img_size_cv2(image):
    img = cv2.imread(image)
    size = img.shape
    # height = sp[0]  # height(rows) of image
    # width = sp[1]  # width(colums) of image
    # chanael = sp[2]  # the pixels value is made up of three primary colors
    return size

# 图像转换
def skimage2opencv(src):
    src *= 255
    src.astype(int)
    cv2.cvtColor(src,cv2.COLOR_RGB2BGR)
    return src

def opencv2skimage(src):
    cv2.cvtColor(src,cv2.COLOR_BGR2RGB)
    src.astype(float32)
    src /= 255
    return src

"""