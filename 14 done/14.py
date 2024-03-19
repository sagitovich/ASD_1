import hashlib

def hash_text(text):
    # Выбираем хеш-функцию (например, hashlib.sha256)
    hasher = hashlib.sha256()
    hasher.update(text.encode())
    return hasher.hexdigest()


def make_hash_table_with_lists():
    words = [] # список для хранения "чистых" слов
    # Открываем файл для чтения
    with open('/Users/a.sagitovich/programming/BFU/ASD/13/english_text.txt', "r", encoding="utf-8") as file:
    # with open('/Users/a.sagitovich/programming/lab_vscode/ASD/13/russian_text.txt', "r", encoding="utf-8") as file:
        lines = file.readlines()

        for line in lines:          # избавляемся от запятых, точек и так далее
            line = line.split()
            for word in line:
                if (word[-1] not in '.,:;!?)-') and (word[0] not in '('):
                    if word not in words:
                        words.append(word)

                elif (word[-1] in '.,:;!?)-') and (word[0] in '('):
                    word = word[:-1]
                    word = word[0:]
                    if word not in words:
                        words.append(word)

                elif (word[-1] in '.,:;!?)-') and (word[0] not in '('):
                    word = word[:-1]
                    if word not in words:
                        words.append(word)

                elif (word[-1] not in '.,:;!?)-') and (word[0] in '('):
                    word = word[0:]
                    if word not in words:
                        words.append(word)

    hash_table = {}  # Создаем пустую хеш-таблицу

    for word in words:
        word_length = len(word)  # Определяем длину каждого слова
        hash_value = hash_text(word)

        # Если ключа с такой длиной еще нет в хеш-таблице, создаем пустой список
        if word_length not in hash_table:
            hash_table[word_length] = []

        # Добавляем слово в список соответствующей длины
        hash_table[word_length].append(word)

    # Выводим хеш-таблицу
    print()
    for length, word_list in hash_table.items():
        print(f'Hash: {hash_value}\nKey: {length}\nValue: {word_list}')
        print()


make_hash_table_with_lists()