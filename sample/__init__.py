import sys
sys.path.append("/home/dmc/Python/DynamicRender")



import json
import httpx
import asyncio
from bilirpc.api import get_dy_detail
from dynamicrender.Core import DyRender
from dynamicadaptor.DynamicConversion import formate_message
from google.protobuf.json_format import MessageToJson


async def grpc_test():
    message = await get_dy_detail("756200529630068741")
    if message:
        message_str = MessageToJson(message[0])
        message_json = json.loads(message_str)
        message_formate = await formate_message("grpc", message_json)
        img = await DyRender().dyn_render(message_formate)
        img.save("1.png")
        # img.show()


async def web_test():
    dyn_id = "755703296984875092"
    url = f"https://api.bilibili.com/x/polymer/web-dynamic/v1/detail?timezone_offset=-480&id={dyn_id}&features=itemOpusStyle"
    headers = {
        "referer": f"https://t.bilibili.com/{dyn_id}"
    }
    message_json = httpx.get(url, headers=headers).json()
    message_formate = await formate_message("web", message_json["data"]["item"])
    img = await DyRender().dyn_render(message_formate)
    img.save("1.png")


if __name__ == "__main__":
    
    asyncio.run(grpc_test())
    # asyncio.run(web_test())
    
    
