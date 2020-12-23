## 文件夹说明

* file_path.py 定义路径，其他模块调用（已取消，都写死）
* captured 抓拍到的图片 

* processed  预处理过的，captured目录去掉会员

* seated 服务员确认已经入座消费，待入库

* customer 入库的会员图片
* customer_face_features 会员头像特征，保存成二进制文件，节省时间
  * customer_add.py 添加会员时生成
  * compare.py 对比时读取



## 90127 错误

* ASFDetectFaces 1 fail: 90127

* 涉及到传入图片的函数操作，要确保送入的图片宽度为 4 的整数倍，如果不是则要提前做好裁剪，或者做resize操作。



## ASF_FaceFeature 

* arcface/struct_info.py

* 读写时，要调用get、set方法

* face_feature1.get_feature_bytes() 将特征读出，写入文件

* 读文件时，set_feature

  ~~~
  with open(filename, 'rb+') as f:
              face_feature = ASF_FaceFeature()
              face_feature.set_feature(f.read())
  ~~~



## 文件列表

* customer_add.py

  ~~~
  customer_add(filename) 函数，
  路径 static/customer/ ，上线时要修改
  
  ~~~

* customer_add_batch.py

* compare.py