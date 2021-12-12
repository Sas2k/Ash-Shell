import commands

import blessed

term = blessed.Terminal()
ver = 'V.dev.3.1'

def main():
    while True:
        inp = input('# ')
        if inp == 'help':
            commands.ash_help()
        elif inp == 'exit':
            print('ash:bye!')
            exit()
        elif inp == 'clear':
            commands.clear()
        elif inp == 'ver':
            print(ver)
        elif '==' in inp:
            inp = inp.split('==')
            print(commands.equalto(inp[0], inp[1]))
        elif '!=' in inp:
            inp = inp.split('!=')
            print(commands.notequalto(inp[0], inp[1]))
        elif '>' in inp:
            inp = inp.split('>')
            print(commands.greaterthan(inp[0], inp[1]))
        elif '<' in inp:
            inp = inp.split('<')
            print(commands.lessthan(inp[0],inp[1]))
        elif '<=' in inp:
            inp = inp.split('<=')
            print(commands.lessthanorequal(inp[0],inp[1]))
        elif '>=' in inp:
            inp = inp.split('>=')
            print(commands.greaterthanorequal(inp[0], inp[1]))
        elif 'if' in inp:
            commands.ifstatement(inp)
        else:
            commands.execute_command(inp)

if '__main__' == __name__:
    main()