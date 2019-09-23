import  random
import sys

#Password set options
p_Upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
p_Lower = 'abcdefghijklmnopqrstuvwxyz'
p_Digit = '0123456789'
p_Sysbol = "!\"#$%&'()*+,-./:;<=>?@[]^_{|}~"

p_set = ''
x = 0

#Check argv count
if len(sys.argv) < 3:
    print("Error in command line")
    exit(0)

#Get password length
length = int(sys.argv[1])
#Get the number of passwords to make
total = int(sys.argv[2])

#Check password flag options
for flag in sys.argv:
    if flag[0] == '/':
        flag = str.upper(flag)

        if flag == '/U':
            p_set += p_Upper
        if flag == '/L':
            p_set += p_Lower
        if flag == '/D':
            p_set += p_Digit
        if flag == '/S':
            p_set += p_Sysbol

x = 0
#Set defaults
if len(p_set) == 0:
    p_set = p_Upper + p_Lower + p_Digit

def getPassword():
    #Create single password
    s_pass = ''
    y = 0
    while y < length:
        r = random.choice(p_set)
        s_pass += r
        y += 1
    return s_pass

while x < total:
    x += 1
    #Print out password
    print(getPassword())
