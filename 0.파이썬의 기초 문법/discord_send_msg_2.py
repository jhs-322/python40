# webhook: 
# https://discordapp.com/api/webhooks/1344086029489143910/RBic3z8_q7itigPhxaYrJQQlOBjy04d7dciJMUug3kUCt8LIHBftfQ-_FeBvpOwLYVWV

import requests
import json
headers = {
	"Content-Type": "application/json"
}

json_data = {
	"embeds": [{
		"title": f"제목",
		"description": f"글 내용",
		"url": f"https://www.adobe.com/go/samsung_cci",
		"thumbnail": {
			"url": f"https://i.namu.wiki/i/NsfJyTxrZzu0jt1cBtwrK2xYFB_EKD4QoQrYM8Gbx-xoyDxwxWdxFZIATiW1APRF2m6amiwaCFi6phCuVda8yzxttwnBlVJBJnZKUoj2qmko2bDz1SQ6HPD5EgxAvJyKJBGAdiHP5Zs--NKSOnwh2Q.webp"
		}
	}]
}

requests.post("https://discordapp.com/api/webhooks/1344103312454320210/sXJ6suATBATnomk-25h48OuLv50rOpKcm5G4Cq821rAIMZsHMqfEyPKhay8Jb-o7HBdw", headers=headers, data=json.dumps(json_data))