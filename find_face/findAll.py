# -*- coding: utf-8 -*-
#  识别图片中的所有人脸并显示出来
# filename : find_faces_in_picture.py

# 导入pil模块 ，可用命令安装 apt-get install python-Imaging
from PIL import Image
# 导入face_recogntion模块，可用命令安装 pip install face_recognition
import face_recognition
import argparse
import os, sys

def parse_args():
    """
    Parse input arguments
    """
    parser = argparse.ArgumentParser(description='test face-reconginition')
    parser.add_argument('--save_path', dest='save_path',
                        help='save_path',
                        default='./results', type=str)

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)

    args = parser.parse_args()
    return args

if __name__ == '__main__':
    args = parse_args()

    # 将jpg文件加载到numpy 数组中
    image = face_recognition.load_image_file("yiqi.jpg")

    # 使用默认的给予HOG模型查找图像中所有人脸
    # 这个方法已经相当准确了，但还是不如CNN模型那么准确，因为没有使用GPU加速
    # 另请参见: find_faces_in_picture_cnn.py
    face_locations = face_recognition.face_locations(image)

        # 使用CNN模型
        # face_locations = face_recognition.face_locations(image, number_of_times_to_upsample=0, model="cnn")

        # 打印：我从图片中找到了 多少 张人脸
    print("I found {} face(s) in this photograph.".format(len(face_locations)))

        # 循环找到的所有人脸
    name_index = 0

    for face_location in face_locations:
        name_index = name_index + 1
        # 打印每张脸的位置信息
        top, right, bottom, left = face_location
        print("A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom, right))
# 指定人脸的位置信息，然后显示人脸图片
        face_image = image[top:bottom, left:right]
        pil_image = Image.fromarray(face_image)
        file_name = str(name_index) + '.jpg'
        if not os.path.isdir(args.save_path):
            os.makedirs(args.save_path)
        path = os.path.join(args.save_path, file_name)
        pil_image.save(path)
        pil_image.show()
