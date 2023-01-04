# DynamicRender

用于将B站的动态渲染为图片（需要配合适配器将动态转化为特定格式）

## 使用

### 1. 格式化动态

```python

# 如果数据是grpc返回的数据
from google.protobuf.json_format import MessageToDict
from dynamicadaptor.DynamicConversion import formate_message
from bilirpc.api import get_dy_detail
import asyncio


async def sample1():
    dynamic_grpc = await get_dy_detail("746530608345251842")
    dynamic: dict = MessageToDict(dynamic_grpc[0])
    dynamic_formate = formate_message("grpc", dynamic)
    print(dynamic_formate)
    
asyncio.run(sample1())



# 如果是web返回的数据

from dynamicadaptor.DynamicConversion import formate_message
import asyncio
import httpx

async def sample2():
    url = "https://api.bilibili.com/x/polymer/web-dynamic/v1/detail?timezone_offset=-480&id=746530608345251842"
    headers = {
        "Referer": "https://t.bilibili.com/746530608345251842"
    }
    result = httpx.get(url, headers=headers).json()
    dynamic_formate = formate_message("web", result["data"]["item"])
    
    print(dynamic_formate)


asyncio.run(sample2())

```
