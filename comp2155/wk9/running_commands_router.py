from connect_to_router import *

print(connection.find_prompt())
connection.enable()
print(connection.find_prompt())
print(connection.find_prompt())
connection.disable_paging() #terminal length 0
output = connection.send_command("show run")
print(output)

connection.exit_enable_mode()
print(connection.find_prompt())

from datetime import datetime
today = datetime.now()
day =  today.strftime("%d")
month = today.strftime("%m")
year = today.strftime("%Y")
hour = today.strftime("%H")
minutes = today.strftime("%M")
seconds = today.strftime("%S")

open(f"config_backup_{year}-{month}--{day}_{hour}--{minutes}--{seconds}.txt", "w").write(output)