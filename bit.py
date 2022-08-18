#BIT STUFFING
original_str=input('Enter string : ')
flag=input('Enter flag sequence : ')
n=8
i=0
s=flag
while i<len(original_str):
    if(original_str[i:i+5]=='11111'):
        s+=original_str[i:i+5]+'0'
        i+=5
    else:
        s+=original_str[i]
        i+=1
s+=flag

print('stuffed sting : ', s)

# at receiver side
print('at receivers side')
stuffed_str=s
n=len(flag)
stuffed_str=stuffed_str[n:len(stuffed_str)-n]
# print('after remove flag stuffed_str: ',stuffed_str)
s=''
i=0
while i<len(stuffed_str):
    if(stuffed_str[i:i+5]=='1'*5 and stuffed_str[i+5]=='0'):
        s+=stuffed_str[i:i+5]
        i+=6
    else:
        s+=stuffed_str[i]
        i+=1
print('string received after destuffing : ',s)
