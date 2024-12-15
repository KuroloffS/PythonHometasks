#lesson2 #string #problem5
matn = input ("Put your text: ")
a = matn.count('a')
e = matn.count('e')
y = matn.count('y')
i = matn.count('i')
o = matn.count('o')
u = matn.count('u')
per = matn.count(' ')
vowels = a + u + y + o + e + i
length = len(matn) 
consonant = length - vowels - per 
print(consonant)