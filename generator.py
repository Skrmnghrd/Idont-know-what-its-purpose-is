import os
import base64
from Crypto.Cipher import AES
BLOCKSIZE = 0
PADDING = "a"
KEY = "a"
message = "a"
decrypted = "a"
decrypt = "a"

def padd(data, pad_with=PADDING):
	return data + (BLOCKSIZE - len(data) %  BLOCKSIZE) * PADDING


def encrypt(secretkey, data):
	cipher = AES.new(padd(secretkey, '@')[:32])
	return base64.b64encode(cipher.encrypt(padd(data)))
def decrypt(secretkey, encrypteddata):
	cipher = AES.new(padd(secretkey, '@')[:32])
	return cipher.decrypt(base64.b64decode(encrypteddata)).rstrip(PADDING)

def welcome():
	os.system("clear")
	global BLOCKSIZE
	global PADDING
	global KEY
	global message
	global decrypted 
	global decrypt
	global portal
	print "input block size  ( jsut type 32 :) )"
	BLOCKSIZE = input(int())
	PADDING = raw_input("padding (JUST ONE CHAR): ")
	KEY = raw_input("insert key ")
	message = raw_input("insert passphrase ")
	decrypted = encrypt(KEY, message)
	#print decrypted
	zz = decrypt(KEY, decrypted)
	print zz
	os.system("clear")
	print ("Your passphrase is [ %s ] \nWith block size of [ %d ] \nYour secretkey is [ %s ] \n" % (message, BLOCKSIZE, KEY,))
	one = 'Encryption is ['
	two = decrypted 
	three = '] \nAnd raw word is [' 
	four = message
	five = ']'
	print one+two+three+four+five 
	print '\nCopy encryption and paste in the portal variable '
	print '\nRepeat the steps on the ssh lock to be authenticated'
welcome()