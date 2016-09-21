#!/usr/bin/env python
#a dead lock which you cannot exit unless you know the pasowrd. uncomment the other line if you want 
#the pc to reboot after a wrong pasword to avoid bruteforce and other hackery
import os
import getpass
import base64
from Crypto.Cipher import AES
import signal
BLOCKSIZE = 0
PADDING = "a"
KEY = "a"
message = "a"
decrypted = "a"
decrypt = "a"
portal = "tLPfn192GsPkuwFo3xyU7iq5DQ9+qh0GF18hiD2wkv4="

def comparison(decrypt, zportal):
	if decrypted == portal:
		quit()
	else:
		os.system("clear")
		os.system("poweroff")
		main()
def padd(data, pad_with=PADDING):
	return data + (BLOCKSIZE - len(data) %  BLOCKSIZE) * PADDING
def encrypt(secretkey, data):
	cipher = AES.new(padd(secretkey, '@')[:32])
	return base64.b64encode(cipher.encrypt(padd(data)))
def decrypt(secretkey, encrypteddata):
	cipher = AES.new(padd(secretkey, '@')[:32])
	return cipher.decrypt(base64.b64decode(encrypteddata)).rstrip(PADDING)

def handler(signum, frame):
	os.system("clear")
	print 'welcome to team 7 unique notepad where you can fuck up at life :)'
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
		#BLOCKSIZE = int(getpass.getpass("please input yer big black size"))
		#PADDING = getpass.getpass('enter whisper pads with wings')
		#KEY= getpass.getpass("insert your key hahaha")
		#message = getpass.getpass("please enta your message")
		decrypted = encrypt(KEY, message)
		comparison(portal, decrypted)
	except ZeroDivisionError:
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
	#4
def main():
	signal.signal(signal.SIGTSTP, handler)
	os.system("clear")
	#os.system("xmodmap -e 'keycode 13='")
	while True:
		try:
			welcome()
		except KeyboardInterrupt:
			welcome()
		except ValueError:
			welcome()		
		except EOFError:
			welcome()
		except AttributeError:
			welcome()
		except SyntaxError:
			welcome()
while True:
	#os.system("xmodmap -e 'keycode 13='")
	welcome()

#tLPfn192GsPkuwFo3xyU7iq5DQ9+qh0GF18hiD2wkv4=
#tLPfn192GsPkuwFo3xyU7iq5DQ9+qh0GF18hiD2wkv4=
