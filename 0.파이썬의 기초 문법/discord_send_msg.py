# # webhook: 
# # https://discordapp.com/api/webhooks/1344086029489143910/RBic3z8_q7itigPhxaYrJQQlOBjy04d7dciJMUug3kUCt8LIHBftfQ-_FeBvpOwLYVWV
# import requests

# headers = {
#     "Content-Type": "application/json"
# }
# json_data = {
#     "content": "디스코드 봇으로 보내는 메시지입니다: 안녕하세요?"
# }
# requests.post("https://discordapp.com/api/webhooks/1344086029489143910/RBic3z8_q7itigPhxaYrJQQlOBjy04d7dciJMUug3kUCt8LIHBftfQ-_FeBvpOwLYVWV", headers=headers, json=json_data)


import requests

headers = {
    "Content-Type" : "application/json"
}
json_data = {
    "content" : "오오 신기하다"
}
#https://discordapp.com/api/webhooks/1344086029489143910/RBic3z8_q7itigPhxaYrJQQlOBjy04d7dciJMUug3kUCt8LIHBftfQ-_FeBvpOwLYVWV

requests.post("https://discordapp.com/api/webhooks/1344103312454320210/sXJ6suATBATnomk-25h48OuLv50rOpKcm5G4Cq821rAIMZsHMqfEyPKhay8Jb-o7HBdw", headers=headers, json=json_data)