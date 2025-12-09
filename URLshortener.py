"""  
to generate the URL Shortner with python and get the shortened link
create 3 main functions ( Random charater,shortening , orginal(redirect))
in shortening we are using a Ascii for url generating which consists of A-Z,a-Z,0-9
it will be in 6 characters, it can be done using Random library
i also use the url_map as a dictionary to store and keep the data , which also helps in making new and unique values
to run in terminal (python URLshortener.py)
"""
import random
url_map={}
def ran_char():
    x=random.randint(1,3)
    if x==1:# digit (Ascii values from 48 to 57)
        return chr(random.randint(48,57))
    elif x==2:# UpperCase letters (A to Z)
        return chr(random.randint(65,90))
    else:# LowerCase Letters(a to z)
        return chr(random.randint(97,122))
    
def shortner(url):
    # if url already exist
    for code,link in url_map.items():
        if link == url:
            return code
    code =""
    for i in range(6):# 6 digit code generation
        code+= ran_char()
    #unique value
    while code in url_map:
        code =""  #  emptying the contents of the code 
        for i in range(6):
            code+= ran_char()    
    url_map[code] =url
    return code
def redirect(code):
    #get is a key word used in dictionary for getting the values
    return url_map.get(code)
def show_all():
    if not url_map:
        print("No Url Stored Yet.")
    else: 
        print("Stored URL")
        for code, link in url_map.items():
            print(f"{code} --> {link}")

def menu():
    while True:
        print(" URL Shortener System ")
        print("1.Shorten url")
        print("2.Redirect (orginal link)")
        print("3.Show all URL")
        print("4.Exit")
        choice=input("Enter Your choice :")
        if choice == "1":
            URL = input("Enter the url Link :")
            code =shortner(URL)
            print("Shortened Code :",code)
        
        elif choice == "2":
            code = input("Enter The Shortened Code : ")
            original= redirect(code)
            if original:
                print("Orginal Url :",original)
            else:
                print("Code Not Found.")
        elif choice =="3":
            show_all()
        elif choice == "4":
            print ("EXITING")
            break
menu()