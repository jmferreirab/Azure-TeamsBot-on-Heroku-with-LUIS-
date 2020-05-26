import re
import requests
import json
from flask import Flask
from flask import json
from flask import jsonify
from flask import request
from flask import Response

r = requests.get(f'https://westus.api.cognitive.microsoft.com/luis/prediction/v3.0/apps/349a200c-2e5d-41ff-9fc7-cac6fe9ab941/slots/production/predict?subscription-key=b70645171382440cbaf63ad0f332d077&verbose=false&show-all-intents=true&log=true&query='+text,headers=headers, params=params)
data=r.json()
#print(data['query'])
#print(data['prediction'])
print(data['prediction']['topIntent'])
topIntent=data['prediction']['topIntent']
print(data['prediction']['intents'][topIntent]['score'])

#data['prediction']['intents']['全部成績']['score']


app = Flask(__name__)

@app.route("/" , methods=['POST'])
def hello():
    # 取得webhook post訊息
    data = json.loads(request.get_data())
    # 需要的input在data['text']欄位中，並使用regex來正規化 
    text = re.sub('\<at\>.*\</at\>','',data['text'])
    # get response by chatbot() funciton
    response = chatbot(text)
    # response json至Teams webhook 
    message =jsonify( {"type": "message", # type: 回覆型態
                       "text": response}) # text: 回覆內容
    return message



if __name__ == "__main__":
    app.run()
