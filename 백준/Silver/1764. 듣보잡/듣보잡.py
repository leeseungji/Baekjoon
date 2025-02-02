n, m = map(int, input().split())

n_people = set()
m_people = set()

for _ in range(n):
    n_person = input().strip()
    n_people.add(n_person)

for _ in range(m):
    m_person = input().strip()
    m_people.add(m_person)

ans = sorted(n_people & m_people)

print(len(ans))
print('\n'.join(ans))