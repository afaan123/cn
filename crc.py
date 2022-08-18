def crc(data,generator_poly):
    temp_data=data
    for i in range(len(generator_poly)-1):
        temp_data+='0'

    i=0
    temp_data=list(temp_data)
    for i in range(len(temp_data)):
        if len(temp_data)-i<len(generator_poly):
            break
        if temp_data[i]=='1':
            for j in range(1,len(generator_poly)):
                if temp_data[i+j]==generator_poly[j]:
                    temp_data[i+j]='0'
                else:
                    temp_data[i+j]='1'

    codeword=''.join(temp_data[i:])
    print('Remainder: ',codeword)
    return codeword

# To Generate CRC
data=input('Enter Data to be coded: ')
generator_poly=input('Enter Generator Codeword: ')


encoded_data=data+crc(data,generator_poly)
print(encoded_data)

# To Check CRC
print('')
check_data=input('Enter Encoded Data: ')
generator_p=input('Enter Generator Polynomial: ')

if int(crc(check_data,generator_p))==0:
    print('No Error in Data')
else:
    print('Error in Data')