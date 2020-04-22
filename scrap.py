import requests
import bs4
import sys
import os
from termcolor import colored, cprint

Obj=requests.get('https://loksabha.nic.in/')         #Make a request to the website 'https://loksabha.nic.in'
soup=bs4.BeautifulSoup(Obj.text,'lxml')              #Pass the Request object 'Obj' to bs4.beautifulSoup and im using 'lxml' struct here.


rawStrings=str(soup.select('#ticker2'))              #Select the id="ticker2" for scrapping the data.
rawStrings=rawStrings.split('<li>')                  #Splitting the String.

scrapData=[]                                         #List of all the Titles(the text of hyperlinks) and hyperlinks will append here.
os.system("mkdir Data")                              #Making a Directory to store all the data.   
for flag in rawStrings:
    x= flag.find('href="')                           #Flag for splitting the string for hyperlinks.
    y= flag.find('" target')                         #Flag for splitting the string.
    l= flag[x+6:]
    hyperLink=l[:y-x-6]                              #Hardcoded value are depends on the Flag to split the strings. 

    a=flag.find('">')                                #Same Splitting and getting string for Titles.   
    b=flag.find('</')
    k=flag[a+2:]
    m=k.find('<img')
    if(m!=-1):                                       #Some of the titles has img tag for gif.
        title=k[:b-a-m+1]                            #This will filter the img tag
    else:
        title=k[:b-a-2]

    cprint("TITLE --> "+title, 'red', attrs=['bold'], file=sys.stderr)    #For Colorful representation.
    cprint("HYPERLINK --> "+hyperLink, 'red', attrs=['bold'], file=sys.stderr)

    cprint("------------------------------------------------------------------------------------------------",'green',
    'on_cyan')
    data=[]                                           #list for one pair of Title and hyperLink.
    data.append(title)
    data.append(hyperLink)
    scrapData.append(data)
    os.system("cd Data && wget "+ hyperLink)          #This will Download all the files in the /Data 
    
print("Wash your hands its a reminder :)")


