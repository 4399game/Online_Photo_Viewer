import celery
from vcr_apps.kuukann.models import Img

from vcr_extra.vcr_util.img_compress import img_compress

# 压缩 图片 与 保存图片到模型层
@celery.task
def task_dsi(img_id, save_path, img_type):
    img = Img.manager_one.get(id = img_id)
    img_image = img.full_img

    # 压缩图片
    img.tiny_img, new_size = img_compress(img_image, save_path, img_type)
    img.width = new_size[0]
    img.height = new_size[1]
    img.save()
