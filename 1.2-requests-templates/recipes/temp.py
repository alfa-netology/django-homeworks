queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт',
]

# список количества слов в каждой фразе
word_counts = list()

for query in queries:
    word_counts.append(len(query.split(' ')))

print(word_counts)

# словарь {'количество фраз': 'количество слов в фразе'}
words = {i: word_counts.count(i) for i in word_counts}

print(words)
