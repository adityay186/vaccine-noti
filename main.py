import requests
import time
link = "https://api.telegram.org/bot1895696163:AAHKY2IOKPb3zojihTE_8kxlZzslSm3P09I/sendMessage?chat_id=1482212406&text=Hello%20from%20utelegram"

while True:
    requests.post(link)
    time.sleep(2)