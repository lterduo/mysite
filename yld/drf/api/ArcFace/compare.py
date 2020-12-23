import cv2
from arcface.engine import *

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


# 初始化时读取图像，取得face_features，
# 后续进来的图片直接比对
dir_name = 'static/customer_face_features'
fullname_list, filename_list = [], []

face_features = []

for root, dirs, files in os.walk(dir_name):
    for filename in files:

        # 读文件
        filename = 'static/customer_face_features/'+filename
        with open(filename, 'rb+') as f:
            face_feature = ASF_FaceFeature()
            face_feature.set_feature(f.read())
            print(filename)

            face_features.append(face_feature)
            filename_list.append(filename)
            f.close()

# 待对比人脸
img1 = cv2.imread("static/captured/1.jpg")
# 尺寸*4，不是4的倍数报错
x, y = img1.shape[0:2]
img1 = cv2.resize(img1, (y*4, x*4))
res, detectedFaces1 = face_engine.ASFDetectFaces(img1)

if res == MOK:
    single_detected_face1 = ASF_SingleFaceInfo()
    single_detected_face1.faceRect = detectedFaces1.faceRect[0]
    single_detected_face1.faceOrient = detectedFaces1.faceOrient[0]
    res, face_feature1 = face_engine.ASFFaceFeatureExtract(
        img1, single_detected_face1)
    if (res != MOK):
        print("ASFFaceFeatureExtract 1 fail: {}".format(res))
else:
    print("ASFDetectFaces 1 fail: {}".format(res))

# 循环头像库
i = 0
for face in face_features:
    res, score = face_engine.ASFFaceFeatureCompare(face_feature1, face)
    if score > 0.99:
        print(filename_list[i], ' 相似度：', score)
        break

    i = i + 1
# print(sys.getsizeof(face_features))

# 反初始化
face_engine.ASFUninitEngine()
