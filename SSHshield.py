#!/usr/bin/env python
#works under no licence
#and other legal craps what so ever.
#DISCLAIMER. DMAAGES TO YOUR COMPUTER WILL NOT BE MY FAULT
#(number 4 will be disabled when script is running to avoid quitting when using GUI
"""
a note from the maker:ONLY WORKS ON LINUX. ALSO WORKS AS ssh shield. or if you dont have gnome also works as another layer of protection
copy this, paste this, sell this, do whatever you like
THIS FILE DISABLES NUMBER 4 ON YOUR KEYBOARD WHEN RUNNING. I AM A NEWBIE ON DEVELOPING THINGS. PLEASE DONT BE TO HARD ON MY. IF THERE IS BUG. 
YOU CAN LIKE MAAIL ME OR NOTIFY ME. 
EXPLAINATION ON HOW THIS SCRIPT WORKS ARE STATED BELOW. PELASE READ BEFORE EXECUTING
PLASE GENERATE YOUR ENCRYPTED PASSWORD BEFORE USING. PASSWORD GENERATOR WILL BE INCLUDED ON MY GITHUB PAGE :)
namly GENERATOR.py
"""
#for this to run automatically. chmod +x (name of python file).py ex. chmod +x cryptofinal.py
#to run ./cyrptofinal.py ./(whateverthename).py
#to shield your ssh just put ./cryptofinal.py ./(whateverthename).py

""" AND OH if you found a way to make this work at rc.local please mail me. paulogrian@gmail.com
and if you also want to give me a job ^_^ im 19 no job. i have a daughter. i can work as a networker(system admin stuff) and as a python dev. willing to be trained. 
i will gradute this march 2016 :)"""
import os
import getpass
import base64
from Crypto.Cipher import AES
import signal
BLOCKSIZE = 0 #BLOCK SIZE MUST BE 32 (i just keep asking users for block size so it will add another layer of security
PADDING = "" #insert the character that you want to use as padding (it fills up the gaps) [example: your key and password did not reach 32 chartacters. padding will be used to fill the remaininng required characters]
#[like] padding is $ and hello is key and message is hey so
#hello$$$$$$$$$$$$$$$$$$$$$$$$$$$ (32 characters)
#hey$$$$$$$$$$$$$$$$$$$$$$$$$$$ (until 32 characters)
#then encryption (AES)
#tLPfn192GsPkuwFo3xyU7iQh=39+qh0GF18hiD2wkv4 (encrypted output) (this is just an example)
#decryption. (the key you used to encrypt will be the key to decrypt)
#tLPfn192GsPkuwFo3xyU7iQh=39+qh0GF18hiD2wkv4  (DECRYPTION WITH 
KEY = "" #the key. will be used to encrypt and decrypt (example: like-hello-this-is-my-keybalblablaHARAMBEISDEADorLOVEORANGEIHATEAPPLE
message = ""
decrypted = ""
decrypt = ""
portal = "tLPfn192GsPkuwFo3xyU7iq5DQ9+qh0GF18hiD2wkv4=" #insert the encrypted password here

def repair(): #so you can type number 4 again :) (4 will be disabled. while script is running)
	os.system("xmodmap -e 'keycode 13=4'")
def comparison(decrypt, zportal): #comparison
	if decrypted == portal:
		repair()
		quit()
	else:
		os.system("clear")
		#uncomment below if you want a reboot
		#os.system("reboot")
		os.system("exit") # this exits the current shell if the passwrod is wrong
		main()
def padd(data, pad_with=PADDING): #padds
	return data + (BLOCKSIZE - len(data) %  BLOCKSIZE) * PADDING
def encrypt(secretkey, data):
	cipher = AES.new(padd(secretkey, '@')[:32]) #encryption function
	return base64.b64encode(cipher.encrypt(padd(data)))
def decrypt(secretkey, encrypteddata): #decryption function
	cipher = AES.new(padd(secretkey, '@')[:32])
	return cipher.decrypt(base64.b64decode(encrypteddata)).rstrip(PADDING)

def handler(signum, frame): #FUNCTION TO AVOID CTRL Z for quitting
	os.system("clear")
	signal.signal(signal.SIGTSTIP, handler)

def welcome():
	os.system("clear")
	signal.signal(signal.SIGTSTP, handler)
	global BLOCKSIZE
	global PADDING
	global KEY
	global message
	global decrypted 
	global decrypt
	global portal
	try:
		print "input block size"
		BLOCKSIZE = input(int())
		PADDING = raw_input("padding")
		KEY = raw_input("insert key")
		message = raw_input("message")
		"""
		UNCOMMENT BELOW IF YOU WANT NO DISPLAY OF CHARACTERS WHEN TYPING CREDENTIALS
		"""
		#BLOCKSIZE = int(getpass.getpass("please input yer big black size"))
		#PADDING = getpass.getpass('enter padding with wings')
		#KEY= getpass.getpass("insert your key *wink *wink")
		#message = getpass.getpass("please enta your message/password")
		decrypted = encrypt(KEY, message)
		comparison(portal, decrypted)
	except ZeroDivisionError: #ALL THESE EXCEPTONS SO THAT SKRIPT WONT QUIT ON ERROR
		main()
	except KeyboardInterrupt:
		main()
	except ValueError:
		main()
	except EOFError:
		main()
	#uncomment below for real life implementation
	except AttributeError:
		main()
	except SyntaxError:
		main()
	except NameError:
		main()
	except OverflowError:
		main()	
	except MemoryError:
		main()
	#4
def main():
	signal.signal(signal.SIGTSTP, handler)
	os.system("clear")
	os.system("xmodmap -e 'keycode 13='")
	while True:
		try:
			welcome()
		except KeyboardInterrupt: #ALL THESE EXCEPTIONS SO THAT SCRIPT WONT QUIT ON ERROR
			welcome()
		except ValueError:
			welcome()		
		except EOFError:
			welcome()
		except AttributeError:
			welcome()
		except SyntaxError:
			welcome()
		except NameError:
			welcome()
		except OverflowError:
			welcome()
		except MemoryError:
			welcome()
while True:
	os.system("xmodmap -e 'keycode 13='")
	welcome()
