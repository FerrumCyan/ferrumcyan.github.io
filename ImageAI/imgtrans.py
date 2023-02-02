"""
AI接口模块
接口文档：https://wiki.zhiyinlou.com/pages/viewpage.action?pageId=166504360
"""
from xes import aiBase
import requests

"""
图像风格转换
参数:
  imageFileName - string，图片名，例如"abc.png"
  style - string，风格，可选值如下
    cartoon：卡通画风格
    pencil：铅笔风格
    color_pencil：彩色铅笔画风格
    warm：彩色糖块油画风格
    wave：神奈川冲浪里油画风格
    lavender：薰衣草油画风格
    mononoke：奇异油画风格
    scream：呐喊油画风格
    gothic：哥特油画风格
    详见百度文档：https://ai.baidu.com/ai-doc/IMAGEPROCESS/xk3bclo77
返回值:
    字典
异常:
    图片不存在
"""
def trans(imageFileName,style,new_url):
    # 参数校验
    if imageFileName == "":
        raise Exception("图片不能为空")
    
    # 如果需要把图片链接作为参数，可以调用aiBase.uploadFile函数，把文件素材区的文件上传，得到url链接
    imageUrl = aiBase.uploadFile(imageFileName)
    
    # 在接口文档中查看接口地址、参数、返回值
    # 接口文档：https://wiki.zhiyinlou.com/pages/viewpage.action?pageId=166504360
    
    # 接口地址
    api = "https://code.xueersi.com/api/ai/image/style_trans"
    # 接口参数
    params = {
        "url": imageUrl,
        "style": style
    }
    # 调用aiBase.request函数，请求ai接口，返回结果字典
    rep = aiBase.request(api, params)
    
    # 解析rep字典，提取需要的字段并进行进一步加工然后返回
    url = rep["data"]["res"]["url"]
    r = requests.get(url, stream=True)
    img_content = r.content
    with open(new_url,"wb") as f:
        f.write(img_content)
    return None