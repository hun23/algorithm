# A.    입력 예시 
# ['eat','tea','tan','ate','nat','bat']

# B.    출력 예시 
# [ ['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat'] ] 

def sort_word(s):
    s = list(s)
    s.sort()
    s = str(s)
    return s

def group_anagrams(inp):
    inp_sorted = [sort_word(x) for x in inp]
    inp_sorted = set(inp_sorted)
    answer = []
    for word_sorted in inp_sorted:
        temp = []
        for word in inp:
            if sort_word(word) == word_sorted:
                temp.append(word)
        if len(temp) != 0:
            answer.append(temp)
    print(answer)


inp = ['eat','tea','tan','ate','nat','bat']
group_anagrams(inp)
    
