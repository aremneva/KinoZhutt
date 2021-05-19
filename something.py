import json
import datetime
with open('./users.txt') as users:
	data=json.load(users)
	print(datetime.datetime.now().strftime("%d-%m-%Y"))
for key, val in data.items():
	val['name'] = "a"
	val['num'] = 1
	val['text']="..."
	val["data"]="01.02.2021"



