# Create your views here.
import json

import requests
from django.http import JsonResponse


def send_dingding(res):
    data = {
        "msgtype": "markdown",
        "markdown": {
            "title": res.get('title', ''),
            "text": "#### {}\n".format(res.get('title', ''))+
                    "\n".join(["- {}".format(json.dumps(match)) for match in res.get("evalMatches")]) +
                    "\n> [view]({link}) \n".format(link=res.get("ruleUrl", ""))
        },
    }
    x = requests.post(
        url="https://oapi.dingtalk.com/robot/send?access_token=f43fa72e23241abfa5c5c22f32b85ea1e34fce11bd05276ad795d3bf420f2c5f",
        json=data
    )
    print(x.content)


def webhook(request):
    res = json.loads(request.body.decode())
    send_dingding(res)
    return JsonResponse(data={})