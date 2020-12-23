# 入库客户头像

import pymysql

import cv2
from arcface.engine import *
import os

# # 数据库
# conn = pymysql.connect(host='39.99.231.153', user='yld',
#                        passwd="1qaz!QAZ", db='yld')
# cur = conn.cursor()
# cur.execute("SELECT * FROM customer")
# for r in cur:
#     print(r)
# cur.close()
# conn.close()


def face_features():
    APPID = b'Bxz9VZNGW8VRp1bu6A5wX12zVzYhRYfgQopvtdCjqvhq'
    SDKKey = b'C19n792c3rg7upRf12PK746teLwmbje52QwjnTCmSZcY'

    # 激活接口,首次需联网激活
    res = ASFOnlineActivation(APPID, SDKKey)
    if (MOK != res and MERR_ASF_ALREADY_ACTIVATED != res):
        print("ASFActivation fail: {}".format(res))
    else:
        print("ASFActivation sucess: {}".format(res))

    # 获取激活文件信息
    res, activeFileInfo = ASFGetActiveFileInfo()

    if (res != MOK):
        print("ASFGetActiveFileInfo fail: {}".format(res))
    else:
        print(activeFileInfo)

    # 获取人脸识别引擎
    face_engine = ArcFace()

    # 需要引擎开启的功能
    mask = ASF_FACE_DETECT | ASF_FACERECOGNITION | ASF_AGE | ASF_GENDER | ASF_FACE3DANGLE | ASF_LIVENESS | ASF_IR_LIVENESS

    # 初始化接口
    res = face_engine.ASFInitEngine(
        ASF_DETECT_MODE_IMAGE, ASF_OP_0_ONLY, 30, 10, mask)
    if (res != MOK):
        print("ASFInitEngine fail: {}".format(res))
    else:
        print("ASFInitEngine sucess: {}".format(res))

    # 读取图像，取得face_feature，入库
    dir_name = 'static/customer'
    fullname_list, filename_list = [], []

    for root, dirs, files in os.walk(dir_name):
        for filename in files:

            img1 = cv2.imread('static/customer/' + filename)
            # cv2.imshow('', img1)
            # cv2.waitKey(0)
            # cv2.destroyAllWindows()

            x, y = img1.shape[0:2]
            img1 = cv2.resize(img1, (y*4, x*4))
            # cv2.imshow('', img1)
            # cv2.waitKey(0)
            # cv2.destroyAllWindows()

            res, detectedFaces1 = face_engine.ASFDetectFaces(img1)

            if res == MOK:
                single_detected_face1 = ASF_SingleFaceInfo()
                single_detected_face1.faceRect = detectedFaces1.faceRect[0]
                single_detected_face1.faceOrient = detectedFaces1.faceOrient[0]
                res, face_feature1 = face_engine.ASFFaceFeatureExtract(
                    img1, single_detected_face1)

                # print(face_feature1)
                face_features.append(face_feature1)

                if (res != MOK):
                    print("ASFFaceFeatureExtract 1 fail: {}".format(res))
            else:
                print("ASFDetectFaces 1 fail: {}".format(res))

    # 反初始化
    face_engine.ASFUninitEngine()

    return face_features
