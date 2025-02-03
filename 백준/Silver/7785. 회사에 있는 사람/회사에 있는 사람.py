n = int(input())
states = set()

for _ in range(n):
    name, state = input().split()
    
    if state == 'enter':
        states.add(name)
    
    elif state == 'leave':
        states.remove(name)

sorted_states = sorted(states, reverse = True)
print('\n'.join(sorted_states))