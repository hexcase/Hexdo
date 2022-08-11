#!/usr/bin/env python3

from colored import fg, bg, attr
import sys

#print('%s%s Hello World %s' % (fg('red'), bg('blue'), attr('reset')))

tofile = "/home/syn/.todo.file"

######## VISUAL FUNCTIONS ###############

def func_ascii():
    print("""%s    __  __              __    
   / / / /__  _  ______/ /___ 
  / /_/ / _ \| |/_/ __  / __ \\
 / __  /  __/>  </ /_/ / /_/ /
/_/ /_/\___/_/|_|\__,_/\____/ 
%s""" % (fg("13"), attr("reset")))



def func_help():
    print("""%sHexdo usage:

%sadd   -> %sadd "text here": To add a new task. Quotes mendatory 
%srm    -> %srm <number>: Remove the line number X.
%shelp  -> %sPrints this. Can also use -h
%sshow  -> %sPrints the todo list
%s-b    -> %sPrints the banner and shows list
""" % (fg(13), fg("cyan"), fg(13), fg("cyan"), fg(13), fg("cyan"), fg(13), fg("cyan"), fg(13), fg("cyan"), fg(13)))

##########################################



def func_show():
    i = 0
    with open(tofile) as f:
        lines = f.readlines()
    f.close()
    print("%s************ Todo **********%s" % (fg("cyan"), fg(13)))
    while i < len(lines):
        print(str(i+1) + ". "+ str(lines[i]), end ='')
        i += 1
    print("%s****************************%s" % (fg("cyan"), attr("reset")))
    
def func_write(lwrite):
    f = open(tofile, "a")
    f.write(lwrite + "\n")
    f.close()
    func_show()
    exit()

def func_remove(lnum):
    
    #Read list and stores it in list
    with open(tofile) as f:
        lines = f.readlines()
    f.close()
    
    #Remove item from list
    lines.pop(lnum - 1)
    
    #Opens the file to write to it
    f = open(tofile,"w")
    for line in lines:
        f.write(line)
    f.close()
    func_show()


############ MAIN STUFF ###################


if len(sys.argv) == 1:
    func_ascii()
    func_show()
    sys.exit()

if sys.argv[1] == "add":
    func_write(sys.argv[2])

elif sys.argv[1] == "rm":
    if sys.argv[2].isnumeric() == 1:
        func_remove(int(sys.argv[2]))
    else:
        func_help()

elif sys.argv[1] == "show":
    func_show()

elif sys.argv[1] == "-b":
    func_ascii()
    func_show()

elif sys.argv[1] == "help" or sys.argv[1] == "-h":
    func_help()
