student = {'name': 'john', 'age': 25, 'courses': ['math', 'english']}

print(student['name'])
print(student.get('phone'))
print(student.get('phone', 'Not Found'))
print(student.get('age'))

student['phone'] = '212-333'

print(student.get('phone'))
print(student)

student['name'] = 'bob'
print(student)

student.update({'name': 'Rod'})
print(student)

del student['age']
print(student)

courses = student.pop('courses')
print(student)
print(courses)

print(student.keys())
print(student.values())
print(student.items())


for key in student:
    print(key)

for key, value in student.items():
    print(key, value)

#--- diff example -- 

word = ['hi', 'hi', 'bye']
word_freq = {}

for w in word:
    if w not in word_freq:
        word_freq[w] = 0
    word_freq[w] += 1

print(word_freq)










