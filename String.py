import requests
import time
from datetime import date

html = (
    "<strong>សរុប: {grand_total}</strong>\n"
    "<code>បានទទួលប្រាក់: {received_amount}</code>\n"
    "<code>📆 {date}</code>\n"
    "<code>=======================</code>\n"
    "<code>1. coca 10x0.25</code>\n"
    "<code>2. abc 1x25</code>\n"
).format(
    grand_total='1,000 $',
    received_amount='100 $',
    date=date.today()
    ,
)

html = requests.utils.quote(html)

# Send notification to the request leave employee
bot_token = "6414826349:AAHD2aY3UD2Rd3u1b5TdWhOAcrMcWC3tVqU"
chat_id = "@ss_20_attendance_notify_bot"
config_url = f"https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={html}&parse_mode=HTML"
res = requests.get(config_url)
print(res)
