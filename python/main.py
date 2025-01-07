import requests
import json

def notify_teams(mention_id, message):
    print('Notifying Teams')
    webhook_url = 'https://1966akioka.webhook.office.com/webhookb2/24ce70d8-1691-4b5e-aa90-67e8f56b36de@2f4ef158-134f-4faa-8db9-ef94be3b003a/IncomingWebhook/06ec01534f77477f9679950d30ee326e/2300d87e-df72-43f2-9367-9269f638e309/V2IJW5BzNLuCXyS-1pxN-7C7Kz4wq_zOJuSow6OIc6hWU1'
    


    # Teamsに送るメッセージを定義
    payload = {
        "type": "message",
        "attachments": [
            {
                "contentType": "application/vnd.microsoft.card.adaptive",
                "content": {
                    "type": "AdaptiveCard",
                    "body": [
                        {
                            "type": "TextBlock",
                            "text": f"@<at>{mention_id}</at>",
                            "color": "attention",  # この行の色を赤に設定
                            "size": "large"  # この行の文字サイズを大きく設定
                        },
                        {
                            "type": "TextBlock",
                            "text": "コンテナが起動しました。",
                            "color": "default",  # この行の色をデフォルトに設定
                            "size": "default"  # この行の文字サイズをデフォルトに設定
                        },
                        {
                            "type": "TextBlock",
                            "text": f"{ message }",
                            "color": "good",  # この行の色を緑に設定
                            "size": "medium"  # この行の文字サイズを中程度に設定
                        }
                    ],
                    "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
                    "version": "1.0",
                    "msteams": {
                        "entities": [
                            {
                                "type": "mention",
                                "text": f"<at>{mention_id}</at>",
                                "mentioned": {
                                    "id": mention_id,
                                    "name": mention_id
                                }
                            }
                        ]
                    }
                }
            }
        ]
    }
    
    # Webhookに対してPOSTリクエストを送信
    response = requests.post(webhook_url, data=json.dumps(payload), headers={'Content-Type': 'application/json'})

    # レスポンスの確認
    if response.status_code == 200:
        print("通知が送信されました！")
    else:
        print(f"通知の送信に失敗しました。ステータスコード: {response.status_code}")


if __name__ == "__main__":
    # チームに通知
    notify_teams('to-murakami@akioka-ltd.jp', '送信完了！”')