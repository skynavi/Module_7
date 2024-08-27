class WordsFinder:
    def __init__(self, *file):
        self.file_names = []
        for file_ in file:
            file_names = self.file_names.append(file_)

    def get_all_words(self):
        all_words = {}
        for file_ in self.file_names:
            with (open(file_, encoding='utf-8') as file_work):
                word_ = file_work.read().lower()
                for sym in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                    word_ = word_.replace(sym, '')
            all_words[file_] = word_.split()
            return all_words

    def find(self, word):
        numb_words = {}
        for name, words in self.get_all_words().items():
            if word.lower() in words:
                numb_words[name] = words.index(word.lower()) + 1
        return numb_words

    def count(self, word):
        count = {}
        for words, name in self.get_all_words().items():
            count_word = name.count(word.lower())
            count[words] = count_word
        return count


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT'))  # 4 слова teXT в тексте всего
