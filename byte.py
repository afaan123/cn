print('Note: Please Enter a space between words')
print('Example: A B ESC FLAG')
data=input('Enter the Data to be encoded: ')
data=data.upper()
words=data.split(' ')
encoded_data='FLAG  '
for word in words:
    if word=='ESC' or word=='FLAG':
        encoded_data+='ESC '
    encoded_data+=word+' '
encoded_data+=' FLAG'
print('Encoded Data: ',encoded_data)
