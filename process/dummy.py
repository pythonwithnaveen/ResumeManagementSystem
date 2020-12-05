import requests
import json
url = "https://www.fast2sms.com/dev/bulk"
message = "Hello Project students this is a test message fot OTP"
querystring = {
    "authorization":"C7JgpgQCJasy39bpXV0nbSYuyrcVS3mywHfp2Iu1ldz5BuKOFq0OhSFt2zzw",
    "sender_id":"FSTSMS",
    "message": message,
    "language":"english",
    "route":"p",
    "numbers":"6370196863,8459634434,9798211265,8919736316"}

headers = {
    'cache-control': "no-cache"
}

response = requests.request("GET", url, headers=headers, params=querystring)

json_data = response.text
d1 = json.loads(json_data)

if d1['return']:
    print("Messages sent")
else:
    print("Message is not sent")
