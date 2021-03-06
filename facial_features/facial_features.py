# -*- coding: utf-8 -*-
# 自动识别人脸特征
# filename : find_facial_features_in_picture.py

# 导入pil模块 ，可用命令安装 apt-get install python-Imaging
from PIL import Image, ImageDraw
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

    image = face_recognition.load_image_file("test02.jpg")

    #查找图像中所有面部的所有面部特征
    face_landmarks_list = face_recognition.face_landmarks(image)

    print("I found {} face(s) in this photograph.".format(len(face_landmarks_list)))
    name_index = 0
    for face_landmarks in face_landmarks_list:

        name_index = name_index + 1
       #打印此图像中每个面部特征的位置
        facial_features = [
            'chin',
            'left_eyebrow',
            'right_eyebrow',
            'nose_bridge',
            'nose_tip',
            'left_eye',
            'right_eye',
            'top_lip',
            'bottom_lip'
        ]

        for facial_feature in facial_features:
            print("The {} in this face has the following points: {}".format(facial_feature, face_landmarks[facial_feature]))

       #让我们在图像中描绘出每个人脸特征！
        pil_image = Image.fromarray(image)
        d = ImageDraw.Draw(pil_image)

        for facial_feature in facial_features:
            d.line(face_landmarks[facial_feature], width=5)
        file_name = str(name_index) + '.jpg'
        path = os.path.join(args.save_path, file_name)
        pil_image.save(path)
        pil_image.show()

