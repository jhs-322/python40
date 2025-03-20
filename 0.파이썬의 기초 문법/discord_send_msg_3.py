import requests

def send_discord_msg(webhook, msg):
    headers = {
        "Content-Type" : "application/json"
    }
    json_data = {
        "content" : msg
    }
    requests.post(webhook, headers=headers, json=json_data)


webhook = "https://discordapp.com/api/webhooks/1344103312454320210/sXJ6suATBATnomk-25h48OuLv50rOpKcm5G4Cq821rAIMZsHMqfEyPKhay8Jb-o7HBdw"
message = "디스코드 봇으로 보내는 메시지입니다: 안녕하세요?"
send_discord_msg(webhook, message)