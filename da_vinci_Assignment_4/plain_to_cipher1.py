import pexpect

plain_cipher = pexpect.spawn('/usr/bin/ssh students@172.27.26.188')
plain_cipher.expect('students@172.27.26.188\'s password:')
plain_cipher.sendline('cs641')
plain_cipher.expect('Enter your group name: ', timeout=50) 
plain_cipher.sendline("da_vinci")

plain_cipher.expect('Enter password: ', timeout=50)
plain_cipher.sendline("sap2023")

plain_cipher.expect('\r\n\r\n\r\nYou have solved 4 levels so far.\r\nLevel you want to start at: ', timeout=50)

# Note: After clearing level 4 this needs to be changed to "solved 4 levels so far"
plain_cipher.sendline("4")
plain_cipher.expect('.*')
plain_cipher.sendline("read")
plain_cipher.expect('.*')

f = open("plaintexts1.txt", 'r')
f1= open("ciphertexts1.txt",'w')

for line in f.readlines():
	plain_cipher.sendline(line)
	print(plain_cipher.before)
	f1.writelines(str(plain_cipher.before)[48:64]+"\n")
	plain_cipher.expect("Slowly, a new text starts*")
	plain_cipher.sendline("c")
	plain_cipher.expect('The text in the screen vanishes!')

data = plain_cipher.read()
print(data)
plain_cipher.close()
print(plain_cipher.before, plain_cipher.after)

f.close()
f1.close()
