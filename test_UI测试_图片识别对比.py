# -*- encoding: utf-8 -*-
"""
@File    : test_UI测试_图片识别对比.py
@Time    : 2020/8/24 11:10
@Author  : wanglong
@Email   : 1836166651@qq.com
@Software: PyCharm
"""
from PIL import Image
from PIL import ImageChops


def compare_images(path_one_name, path_two_name, diffent_save_name):
    """
    比较图片，如果有不同则生成展示不同的图片
    @参数一: path_one: 第一张图片的路径
    @参数二: path_two: 第二张图片的路径
    @参数三: diff_save_location: 不同图的保存路径
    """
    all_path = r'D:\images\uitest' + '\\'
    diff_save_location = all_path + diffent_save_name
    path_one = all_path + path_one_name
    print(path_one)
    path_two = all_path + path_two_name
    print(path_two)
    image_one = Image.open(path_one)
    image_two = Image.open(path_two)
    try:
        diff = ImageChops.difference(image_one, image_two)

        if diff.getbbox() is None:
            # 图片间没有任何不同则直接退出
            print("【+】We are the same!")
        else:
            diff.save(diff_save_location)
    except ValueError as e:
        text = ("表示图片大小和box对应的宽度不一致，参考API说明：Pastes another image into this image."
                "The box argument is either a 2-tuple giving the upper left corner, a 4-tuple defining the left, upper, "
                "right, and lower pixel coordinate, or None (same as (0, 0)). If a 4-tuple is given, the size of the pasted "
                "image must match the size of the region.使用2纬的box避免上述问题")
        print("【{0}】{1}".format(e, text))


if __name__ == '__main__':
    compare_images('002.png','003.png','004.png')