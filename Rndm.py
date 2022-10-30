import os,platform

os.system('git pull')

 

ass=platform.architecture()[0]

if ass=="64bit":

    __import__("RNDM").menu()
