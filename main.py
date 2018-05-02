from socket import gethostbyname

#function for getting ip
def ip(url):
    return gethostbyname(url)

while True:
    u = input("enter website: ") #address here
    print(gethostbyname(u)) #prints IPv4
    
#website url cannot have https/http, can't have : or ::, nor / or //. just website.com.org/whatever
