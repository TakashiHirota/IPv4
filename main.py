from socket import gethostbyname

def ip(url):
    return gethostbyname(url)

while True:
    u = input("enter website: ")
    print(gethostbyname(u))
    
#website url cannot have https/http, can't have : or ::, nor / or //. just website.com/org/whatever
