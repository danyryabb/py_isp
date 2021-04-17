import re

def check_email(email):
    regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
    if(re.search(regex, email)):
        print("Valid Email")
    else:
        print("Invalid Email")

def check_float(num):
    regex = '[+-]?[0-9]+\.[0-9]+'
    if(re.search(regex, num)): 
        print("Floating point number") 
    else: 
        print("Not a Floating point number")

def check_url(url):
    obj1 = re.findall('(\w+)://', url)
    print(obj1)
    obj2 = re.findall('://([\w\-\.]+)', url)
    print(obj2)
    obj3 = re.findall('://([\w\-\.]+)(:(\d+))?', url)
    print(obj3)
    obj4 = re.findall('(\w+)://([\w\-\.]+)/(\w+).(\w+)', url)
    print(obj4)

check_float('sefgs')
check_float('-44.412')
check_url('file://localhost:4040/abc_file')
check_url('http://www.example.com/index.html')





