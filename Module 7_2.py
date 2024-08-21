from pprint import pprint


def custom_write(file_name, strings):
    strings_positions = {}
    for i in range(len(strings)):
        file = open(file_name, 'a', encoding='utf-8')
        strings_positions.update({(i+1, file.tell()): strings[i]})
        file.write(strings[i] + '\n')
        file.close()
    return strings_positions



info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
