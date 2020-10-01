import re

def word_count(s):
    l = ['"', ':', ';', ',', '.', '-', '+', '=', '/', '\\', '|',
         '[', ']', '{', '}', '(', ')', '*', '^', '&']
    wordList = re.sub("[^\w]", " ",  s).split()
    d = {}
    if len(wordList) == 0:
        return d
    for i in l:
        s = s.replace(i, "")
    lst = s.split(' ')
    for i in range(len(lst)):
        lst[i] = lst[i].replace(' ', '')
        # lst[i] = lst[i].replace('"', '')
        # lst[i] = lst[i].replace(',', '')
    lst = list(filter(('').__ne__, lst))
    lst = [n.lower() for n in lst]
    lst1 = list(set(lst))
    for i in range(len(lst1)):
        d[lst1[i]] = lst.count(lst1[i])
    return d




if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))