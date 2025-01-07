from collections import Counter

case_num = 1

while True:
    word1 = input().strip()
    word2 = input().strip()
	
    if word1 == 'END' and word2 == 'END':
        break
       
    if Counter(word1) == Counter(word2):
        print(f'Case {case_num}: same')
    else:
        print(f'Case {case_num}: different')
    
    case_num += 1