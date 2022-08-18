#byte stuffing input bit sequence
print('enter flag and esc in format [FLAG,ESC]')
original_str=input('Enter string : ')
flag=input('Enter flag bit string : ')
esc=input('enter esc bit string : ')
n=len(flag)
stuffed_str=original_str.split()

s=str(flag)+' '
for i in stuffed_str:
    if(i in [flag,esc]):
        s+=str(esc)+' '
    s+=i+' '

s+=str(flag)

print('stuffed string : ',s)

# at receivers side
stuffed_str=s.split()
stuffed_str=stuffed_str[1:n-1]


s=''
i=0
while i<len(stuffed_str)-1:
    if stuffed_str[i]==esc and stuffed_str[i+1] in [flag,esc]:
        s+=''.join(stuffed_str[i+1])+' '
        i+=2
    else:
        s+=''.join(stuffed_str[i])+' '
        i+=1

print('sequence received destuffing : ',s)