import random
person = ['Moris', 'chittagong']

name =person[0]
location = person[1]

sentence_one_group =[
    f'This is {name}',
    f'My name is {name}',
    f'{name} is my name',
]

sentence_two_group =[
    f'i live in {location},'
    f'{location} is the place where i live',
    f'i was raised in {location}',
]
sentence_one = random.choice(sentence_one_group)
sentence_two = random.choice(sentence_two_group)
paragraph = f'{sentence_one} {sentence_two}'

print(paragraph)