ip = input("Please enter IP address:")
def Validate_IP(ip):
    if ip.count('.') != 3:
        return ('Invalid Ip address')

    st = set()
    for i in range(0, 256):
        st.add(str(i))
    counter = 0
    temp = ""
    for i in range(0, len(ip)):
        if(ip[i] != '.'):
            temp = temp+ip[i]
        else:
            if(temp in st):
                counter = counter+1
            temp = ""
    if(temp in st):
        counter = counter+1
 
    # verifying all conditions
    if(counter == 4):
        return 'Valid Ip address'
    else:
        return 'Invalid Ip address'
 
 
# Driver Code
print(Validate_IP(ip))
