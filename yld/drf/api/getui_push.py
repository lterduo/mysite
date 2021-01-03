# 个推推送消息

from gt_push_sdk.igt_push import *
from gt_push_sdk.igetui.template.igt_notification_template import NotificationTemplate
from gt_push_sdk.igetui.template.style.Style0 import Style0


# STEP1：获取应用基本信息
APPID = "zBxiroHDk887RnxHS3R3j"
APPKEY = "mCgsyd6AlX61vKourbmaB1"
MASTERSECRET = "M7PCSAGb9f938ZCOkyaAc2"
HOST = "http://api.getui.com/apiex.htm"

push = IGeTui(HOST, APPKEY, MASTERSECRET)

style = Style0()
# STEP2：设置推送标题、推送内容
style.title = "注意！有客户进店！"
style.text = "请输入通知栏内容"
style.logo = "客户.png"  # 设置推送图标
# STEP3：设置响铃、震动等推送效果
style.isRing = True  # 设置响铃
style.isVibrate = True  # 设置震动

# STEP4：选择通知模板
template = NotificationTemplate()
template.appId = APPID
template.appKey = APPKEY
template.style = style

# STEP5：定义"AppMessage"类型消息对象,设置推送消息有效期等推送参数
appIds = [APPID]
message = IGtAppMessage()
message.data = template
message.appIdList = appIds
message.isOffline = True
message.offlineExpireTime = 1000 * 600

# STEP6：执行推送
ret = push.pushMessageToApp(message)
print(ret)
