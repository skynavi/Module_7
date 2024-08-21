from pprint import pprint


def custom_write(file_name, strings):
    #strings_positions = {}
    for i in range(len(strings)):
        file = open(file_name, 'a', encoding='utf-8')
        #print(i+1)
        strings_positions = {(i+1, file.tell()): strings[i]}
        print(strings_positions)
        file.write(strings[i] + '\n')
        file.close()

        #file = open(file_name, 'r', encoding='utf-8')
        #byte_ = (file.tell())
        #pprint(file.read())
        #byte_ = (file.tell())
        #file.close()


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
