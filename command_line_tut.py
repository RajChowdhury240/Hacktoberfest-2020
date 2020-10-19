
"""command line arguments are one of the most important topic in python
python has a module named sys which provide interaction with any command line argument via sys.argv
if you are famiiliar to python scripting or any anykind of scripting you know about command line argument then if you dont know then RIP
ok no worry open a text file name it like luck.py ok now write a hello World code and save it somewhere in desktop and now
go to that path and and save the path and your path name will be like this c:/users/Desktop you can find it in properties
ok now run it like this python luck.py
now this is how you run a file in command prompt
linux users you have to do like this
cd "file location"
python3 luck.py
if python is not installed then you have to do like this
apt-get install python3
"""

"""
now for the command line argument 
type the code dont do shitty copy and paste """

import sys
print("number of students :",len(sys.argv))
print("all the students:",sys.argv)
"""now if you run this code by saving it somewhere or with command prompt then the output will be different
try it 
btw len(sys.argv) : is here for the length of the arguments given here btw sys.argv is the arguments u passed here okay i hope all are clear by the you can print any value like sys.argv[1] it will print that specific value """

#more on sys module
"""try this in console it will tell you about python version and all
import sys; print('Python %s on %s' % (sys.version, sys.platform))
you can also try sys.copyright or sys.flags or sys.api_version"""
