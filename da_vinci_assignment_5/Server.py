

import pexpect





child = pexpect.spawn('/usr/bin/ssh student@172.27.26.188')   
que=['student@172.27.26.188\'s password:','Enter your group name: ','Enter password: ','\r\n\r\n\r\nYou have solved 5 levels so far.\r\nLevel you want to start at: ','.','.','.','.','.*']
response=['cs641',"da_vinci","sap2023","5","go","wave","dive","go","read"]





for i in range(len(response)):
    child.expect(que[i])
    child.sendline(response[i])

child.expect('.*')

with open("plaintexts.txt", 'r') as file1,open("ciphertexts.txt",'w') as file2:
    for line in file1.readlines():
        li = line.split()
        for l in li:
            child.sendline(l)
            s = str(child.before)[48:64]
            file2.write(s)
            file2.write(" ")
            child.expect("Slowly, a new text starts*")
            child.sendline("c")
            child.expect('The text in the screen vanishes!')
        file2.write("\n")

    child.sendline("ffffffffffffffmu")
    s = str(child.before)[48:64]
    file2.write(s)
    file2.write(" ")
    child.close()







