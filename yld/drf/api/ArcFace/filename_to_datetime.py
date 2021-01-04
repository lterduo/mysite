# 将customer中文件名改为datetime，唯一性

from datetime import datetime
import os

# 防止误操作，运行后注释路径
# 完成后运行 customer_add_batch.py 提取特征
dir_name = '../../static/customer/'

for root, dirs, files in os.walk(dir_name):
    for filename in files:
        print(filename)
        s_time = str(datetime.now())
        s_time = s_time.replace(':', '_')
        s_time = s_time.replace(' ', '_')
        try:
            os.rename('../../static/customer/' + filename,
                      '../../static/customer/' + s_time + '.jpg')
        except Exception as e:
            with open('errlog.txt', 'a+') as f:
                f.writelines(str(datetime.now()) + '  filename_to_datetime.py')
                # f.write(str(datetime.now()) + '  filename_to_datetime.py')
                f.writelines(str(e))
                f.close()
