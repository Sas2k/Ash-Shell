import os
import blessed

from Ash_Shell import *

term = blessed.Terminal()

help_msg = '''===+++help+++===
===commands===
help - Displays this message
clear - clears the terminal
help "obj/cmd" - displays the help message for that command or object
put "string" - prints the string
put [int] - prints the interger inside the brackets
exit - exits the shell
ver - displays the version
[Note: The Spaces Matter]
[Note: When using the help command put the "" aroung the command or object your trying to get help]
===gates===
| [and gate] - does the commands even if one is unsuccesful
==Math==
=Arithmatic=
[+] - addition
[-] - substraction
[*] - multiplication
[/] - division
[Math] #this is the help command for all of the commands here
*******
=Logic=
== - equal to[eql]
!= - not equal to[nql]
> - greater than[gt]
< - less than[lt]
(>=) - greater than or equal to[gteql]
(<=) - less than or equal to[lteql]
**********
===Statement===
if#statement#command - the command is run if the statement is true [if]
=statement logic=
-eq - equal to
-neq - not equal to
-gt - greater than
-lt - less than
-gtoeq - greater than or equal
-ltoeq - less than or equal
[Note: The [] in front of the defenition if the help command name, The name you use for this command ex***help "if",\nThe commands that doesn't have a [] are the ones you just type the command in as usual (help "help")]
Example:
if#1-eq1#put "hello"
'''
def ash_help():
    print(term.lightgreen(help_msg))

def clear():
    # for windows
    if os.name == 'nt':
        _ = os.system('cls')
    # for mac and linux(here, os.name is 'posix')
    if os.name != 'nt':
        _ = os.system('clear')

def equalto(s1, s2):
    global equal
    if s1[0] == '"' or "'":
        s1 = str(s1)
    else:
        s1 = int(s1)
    if s2[0] == '"' or "'":
        s2 = str(s2)
    else:
        s2 = int(s2)
    if s1 == s2:
        equal = True
    else:
        equal = False
    return equal

def notequalto(s1, s2):
    global notequal
    if s1[0] == '"' or "'":
        s1 = str(s1)
    else:
        s1 = int(s1)
    if s2[0] == '"' or "'":
        s2 = str(s2)
    else:
        s2 = int(s2)
    if s1 != s2:
        notequal = True
    else:
        notequal = False
    return notequal

def greaterthan(s1, s2):
    s1 = int(s1)
    s2 = int(s2)
    if s1 > s2:
        greater = True
    else:
        greater = False
    return greater

def lessthan(s1, s2):
    s1 = int(s1)
    s2 = int(s2)
    if s1 < s2:
        lesser = True
    else:
        lesser = False
    return lesser

def lessthanorequal(s1, s2):
    s1 = int(s1)
    s2 = int(s2)
    if s1 <= s2:
        lessequal = True
    else:
        lessequal = False
    return lessequal

def greaterthanorequal(s1,s2):
    s1 = int(s1)
    s2 = int(s2)
    if s1 >= s2:
        greaterequal = True
    else:
        greaterequal = False
    return greaterequal

def test():
    print('TESTING')

def execute_command(command):
    if '|' not in command:
        command = command.split(' ')
        for cmd in range(0, len(command)):
            if command[cmd] == 'help':
                if command[cmd+1] == '"clear"':
                    print(term.lightgreen('help:Clears the screen'))
                elif command[cmd+1] == '"exit"':
                    print(term.lightgreen('help:Exits the shell'))
                elif command[cmd+1] == '"put"':
                    print(term.lightgreen('help:displays the text after the command \nExample:put "hello"'))
                elif command[cmd+1] == '"and gate"':
                    print(term.lightgreen('help: AND Gate does the commands even if one or more of those are unsuccessful\nExample: cmd1 | cmd2'))
                elif command[cmd+1] == '"Math"':
                    print(term.lightgreen('help:Simple Arithmetic commands\nExample: put 1[+]1, put 1[-]1, put 1[/]1, put 1[*]1'))
                elif command[cmd+1] == '"eql"':
                    print(term.lightgreen('help: the equal sign just prints out whether it is true or false\nExample:1==1'))
                elif command[cmd+1] == '"if"':
                    print(term.lightgreen('help: the if statement is just a normal if statement.\nexample:if#1-eq1#put "hello"'))
                else:
                    print(term.lightgreen('help:obj/command not found'))
            elif command[cmd] == '':
                pass
            elif command[cmd] == 'put':
                if command[cmd+1][0] == '"' and command[cmd+1][-1] == '"' or command[cmd+1][0] == "'" and command[cmd+1][-1] == "'":
                    print(command[cmd+1][1:-1])
                elif command[cmd+1][0]== '[' and command[cmd+1][-1] == ']':
                    num = command[cmd+1][1:-1]
                    num = int(num)
                    print(num)
                elif '[+]' in command[cmd+1]:
                    ex = str(command[cmd+1])
                    ex = ex.split('[+]')
                    count = 0
                    total = 0
                    for count in range(0, len(ex)): 
                        num = int(ex[count])
                        total += num
                    print(total)
                elif '[-]' in command[cmd+1]:
                    ex = str(command[cmd+1])
                    ex = ex.split('[-]')
                    count = 0
                    total = int(ex[0])
                    for count in range(0, len(ex)-1):
                        num = int(ex[count+1])
                        total = total - num
                    print(total)
                elif '[*]' in command[cmd+1]:
                    ex = str(command[cmd+1])
                    ex = ex.split('[*]')
                    count = 0
                    total = int(ex[0])
                    for count in range(0, len(ex)-1):
                        num = int(ex[count+1])
                        total = total * num
                    print(total)
                elif '[/]' in command[cmd+1]:
                    ex = str(command[cmd+1])
                    ex = ex.split('[/]')
                    count = 0
                    total = int(ex[0])
                    for count in range(0, len(ex)-1):
                        num = int(ex[count+1])
                        total = total / num
                    print(total)
            elif command[cmd][0] == '"' and command[cmd][-1] == '"' or command[cmd][0] == "'" and command[cmd][-1] == "'":
                pass
    elif '|' in command:
        command = command.split('|')
        for cmd in range(0, len(command)):
            if command[cmd] == 'help ' or command[cmd] == ' help':
                ash_help()
            elif command[cmd] == 'clear ' or command[cmd] == ' clear':
                clear()
            elif command[cmd] == 'exit ' or command[cmd] == ' exit':
                exit()
            elif command[cmd][0:3] == 'put ' or command[cmd][0:4] == ' put ':
                if command[cmd][4] == "'" or '"' and command[cmd][-1] == "' " or '" ' or '"' or "'":
                    print(command[cmd][5:-2])
                elif command[cmd+1][0]== '[' and command[cmd+1][-1] == ']':
                    num = command[cmd+1][1:-1]
                    num = int(num)
                    print(num)
            elif command[cmd][0] == '"' and command[cmd][-1] == '"' or command[cmd][0] == "'" and command[cmd][-1] == "'":
                pass

def ifstatement(statement):
    statement = str(statement)
    statement = statement.split('#')
    st = statement[1]
    cmd = statement[2]
    st = str(st)
    run = False
    if '-eq' in st:
        st = st.split('-eq')    
        run = equalto(st[0],st[1])
    elif '-neq' in st:
        st = st.split('-neq')
        run = notequalto(st[0], st[1])
    elif '-gt' in st:
        st = st.split('-gt')
        run = greaterthan(st[0],st[1])
    elif '-lt' in st:
        st = st.split('-lt')
        run = lessthan(st[0],st[1])
    elif '-ltoeq' in st:
        st = st.split('-ltoeq')
        run = lessthanorequal(st[0],st[1])
    elif '-gtoeq' in st:
        st = st.split('-gtoeq')
        run = greaterthanorequal(st[0],st[1])
    if run == True:
        if cmd == 'help':
            commands.ash_help()
        elif cmd == 'exit':
            print('ash:bye!')
            exit()
        elif cmd == 'clear':
            commands.clear()
        elif cmd == 'ver':
            print(ver)
        elif '==' in cmd:
            inp = cmd.split('==')
            print(commands.equalto(inp[0], inp[1]))
        elif '!=' in cmd:
            inp = cmd.split('!=')
            print(commands.notequalto(inp[0], inp[1]))
        elif '>' in cmd:
            inp = cmd.split('>')
            print(commands.greaterthan(inp[0], inp[1]))
        elif '<' in cmd:
            inp = cmd.split('<')
            print(commands.lessthan(inp[0],inp[1]))
        elif '<=' in cmd:
            inp = cmd.split('<=')
            print(commands.lessthanorequal(inp[0],inp[1]))
        elif '>=' in cmd:
            inp = cmd.split('>=')
            print(commands.greaterthanorequal(inp[0], inp[1]))
        elif 'if' in cmd:
            commands.ifstatement(cmd)
        else:
            commands.execute_command(cmd)
    else:
        return 