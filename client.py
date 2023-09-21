import requests,os

class CallRedStar:
	def __init__(self, key: str, phone: str):
		super().__init__()
		self.key = key
		self.phone = phone
	
	def sendreq(self):
		params = {
			"clientKey": self.key,
			"phone": self.phone
		}
		resp = requests.post("https://cvc.originnamnice.repl.co/api/call", json = params).json()
		print("\x1b[00m",resp)
		
def clear():
	if os.name == "nt":
		os.system("cls")
	else:
		os.system("clear")
		

clear()
print("""
   \x1b[31m ██████╗ ███████╗██████╗ ███████╗████████╗ █████╗ ██████╗ 
    ██╔══██╗██╔════╝██╔══██╗██╔════╝╚══██╔══╝██╔══██╗██╔══██╗
    \x1b[00m██████╔╝█████╗  ██║  ██║███████╗   ██║   ███████║██████╔╝
    ██╔══██╗██╔══╝  ██║  ██║╚════██║   ██║   ██╔══██║██╔══██╗
   \x1b[31m ██║  ██║███████╗██████╔╝███████║   ██║   ██║  ██║██║  ██║
    ╚═╝  ╚═╝╚══════╝╚═════╝ ╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝
                     \x1b[00m[ \x1b[32mREST-API CALLING V.1\x1b[00m ]
"""
)
clientkey = input("    \x1b[36mclientKey : \x1b[31m")
phon = input("    \x1b[36mPhone-Num : \x1b[31m")
print()
run = CallRedStar(clientkey, phon)
run.sendreq()