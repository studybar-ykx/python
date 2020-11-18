
Str = input()
for i in range(0, len(Str)):
    if Str[i] == ' ':
        print(' ', end="")
    elif Str[i] in ['x', 'y', 'z']:
        print(chr(ord(Str[i])-23), end='')
    else:
        print(chr(ord(Str[i]) + 3), end='')