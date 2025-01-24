word = input()

alpha = ['c=', 'c-','dz=','d-','lj','nj','s=','z=']

for a in alpha:
    word = word.replace(a, '0')

print(len(word))