
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__) ) )

# 用户键名
key_kouza = 'kouza_'
key_kouza_ctrl = 'kouza_ctrl_'

# 网站键名
vcrting = 'vcrting'

# 其他键名
key_kuukann = vcrting+ '_kuukann'
key_pic = key_kuukann+ '_key_pic'
key_img = '_img'

# 后台 相关配置
pre_page_num = 50
admin_title = 'VcrT'
admin_header = 'VcrT'
none_show = '- 空白 -'

# VcrTing 的邮箱
vcrting_mail_name = 'vcrting@163.com'
vcrting_email = 'vcrting@163.com'
vcrting_code_pwd = 'ZT123voez'

# 访问 url
url = {
    'web': '',
    'user': 'メリー',
    'option': 'する',
    'kuukann': 'kuukann',
    
    'web_kuukann': 'ントルコレク',
    'web_pic': 'ラガール',

    'user_station': 'ゴミはこ',
}

# 使用 url
kuukann_url = '/域/'
kouza_url = '/メリー/'

station_url = 'ゴミはこ/'
ajax_img_url = '/kuukann/img'

# 文件夹 地址
kouza_path = os.path.join(BASE_DIR, 'media', 'kouza')
vcr_web_path = os.path.join(BASE_DIR, 'media', 'vcr')

# 缓存
cache_time_short = 60*3
cache_time_middle = 60*30
cache_time_long = 60*60*3

# 图片大小限制标准
i_middle = 2166

i_small = i_middle - int(i_middle / 4)
i_tiny = i_small - int(i_small / 4)
i_mini = i_tiny - int(i_tiny / 4)
i_less = 200

i_big = i_middle + int(i_middle / 2)
i_large = i_big + int(i_big / 1.8)
i_huge = i_large + int(i_large / 1.7)
i_massive = i_huge + int(i_huge / 1.618)

# 图片像素限制标准
px_middle = 6200000
px_huge = 30000000
px_massive = 0

# 标志
station_pic_flag = 'pic'
station_img_flag = 'img'
station_full_flag = 'full_img'

# 所有用户 通用配置
def_keep_day = 30