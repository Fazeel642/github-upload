import os
import time
from discord_webhook import DiscordWebhook

webhook_url = "https://discord.com/api/webhooks/834007103277629480/PQ0KXAjMlAl1Il_6UGowOwcsvKYQ3949hmkKSjvLMsnJfO4IjoD4IlGx8YlGM1cOF9_2"

print (webhook_url)
while True:
    DiscordWebhook(url=webhook_url, content='Webhook Message').execute()
    time.sleep(10)