from urllib import response
import mechanize
import os
import time import sleep
import datetime
import sys
browser mechanize.Browser()
browser.set_handle_robots(False)
cookies mechanize.CookieJar()
browser.set_cookiejar(cookies)
browser.addeaders = [('User-agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36')]
browser.set_handle_refresh(False)

url = 'https://m.facebook.com/login.php

def clear():
   if os.name == 'nt':
     os.system('cls')
      else:
      os.system('clear')

def sp(stri):
   for letter in stri:
       print(letter,end = ")
       sys.stdout.flush()
       sleep(0.01)

clear()

 def login():
   browser.open(url)
   browser.select_form(nr = 0)
   browser.form['email'] = USERNAME
   browser.form['pass'] = PASSWORD
   r = browser.submit() 
   f = open('login.html","wb")
   f.write(r.read())
   f.close()
   browser.select_form(nr = 0)
   print("\033[1;33;40m", end = ")
   sp("\nEnter two factor code by google authenticator:\n")
   print("\033[1;37;40m")
   apr = str(input())
   print()
   try:
      browser.form['approvals_code] = apr
  except mechanize._form_controls. ControlNotFoundError:
      print("wrong password or some shit, check generated file")
      f = open("epage_" + str(USERNAME) + "html","wb")
      f.write(r.read())
      f.close()
      exite(1)
   r = browser.submite()
   browser.select_form(nr = 0)
   try:
      browser.form['name_action_selected'] = ['save_device'] except mechanize._form_controls.controlNotFoundError:
      except mechanize._form_controls.controlNotFoundError:
      print("some shit gone down, check generated file")
      f = open("epage_" + str(USERNAME) + "html","wb")
      f.write(r.read())
      f.close()
      exite(1)
   r = browser.submit()
   f = open("full_login_" + str(USERNAME) + "html", "wb")
   f.write(r.read())
   f.close()

def findfbchat(curl):
    r = browser.open(curl)
    x = browser.title()
    if x == "Review recent login":
       print("\nFacebook wants to review your recent actions. \nPlease fix that and then re run the program.")
       exit(1)
   if x== "Login approval needed":
       print("\nYour account is stuck on verification\nPlease do it and then re run the program.")
       exit(1)
   if x == "Epsilon":
       print("\nYour account got locked, recover it kindly and re run the script.")
          exit(1)

def sendtextchat(comment):
    try:
        browser.select_form(nr = 1)
    except mechanize_mechanize.FormNotFoundError:
        print("\033[1:31:40m²,end=")
        print(">",comment, "\n")
    try:
        browser.form['body'] = comment
    except mechanize._form_controls.controlNotFoundError:
        print("\033[1;31;40m²,end=")
        print("", comment, "\n")
        r=browser.submit()
        print("\003[1:32:40m²,end = ")
        e = datetime.datetime.now()
        print (e.strftime("»» %d%m%Y %1%M%S%p"))
        print("", comment, "\n")


print ("MODE BY JULMI JAAT]])

print("\003[1;33;40m", end = ")
sp("\nEnter your email or mob no.. :\n")
print("\033[1;37;40m")
USERNAME = str(input())
print("\033[1;33;40m", end = "")
sp("\nEnter your password:\n")
print\033[1;37;40m²)
PASSWORD = str(input())
login()
print("\033[1;33;40", end = ")
sp("Enter the conversation id:\n")
print("\033[1;37;40m²)
cid str(input())
curl = 'https://m.facebook.com/messages/t/' + str(cid)
print("\033[1;33;40m², end = ")
sp("Enter kidx name :\n")
print("\033[1;37;40m²)
np1 str(input())
print("\033[1;33;40m", end = ")
sp("Enter notepad file:\n")
print("\033[1;37;40m²)
np str(input())
fopen(np, 'r')
lines f.readlines()
f.close
print()
print("\033[1;33;40m², end = ")
sp("Enter time delay in second:\n")
print("\033[1;37;40m²)
t int(input())

clear()
print("\033[1;37;40m²)
e datetime.datetime.now()
print(e.strftime) ('Start Time = %d/%m/%Y %I:%M:%S%p"))
prinf()
count = 0
while True:
    for line in lines:
     if len(line) > 0:
        if count != 0:
           sleep(t)
           findfbchat(curl)
           sendtextchat(str(np1) + line)
           count += 1
           if count% 50 0:
           sleep(1)
           clear()
           149
print("\033[1;37;40m")
e datetime.datetime.now()
print(e.strftime("Start Time = %d/%m/%Y
%I:%M:%S%p"))
print("\033[1;33;40m", end = "")
sp("Sent + str(count) +
messages.\n")
print("\033[1;37;40m")
