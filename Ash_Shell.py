import commands

import blessed

term = blessed.Terminal()
ver = 'v2.5'

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
        elif '==' in inp and not inp[0:1] == 'if':
            inp = inp.split('==')
            print(commands.equalto(inp[0], inp[1]))
        elif '!=' in inp and not inp[0:1] != 'if':
            inp = inp.split('!=')
            print(commands.notequalto(inp[0], inp[1]))
        elif '>' in inp and not inp[0:1] != 'if':
            inp = inp.split('>')
            print(commands.greaterthan(inp[0], inp[1]))
        elif '<' in inp and not inp[0:1] != 'if':
            inp = inp.split('<')
            print(commands.lessthan(inp[0],inp[1]))
        elif '<=' in inp and not inp[0:1] != 'if':
            inp = inp.split('<=')
            print(commands.lessthanorequal(inp[0],inp[1]))
        elif inp[0:1] == 'if':
            commands.ifstatement(inp)
        else:
            commands.execute_command(inp)

if '__main__' == __name__:
    main()