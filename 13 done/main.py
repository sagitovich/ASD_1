import hashlib

def hash_text(text):
    # Выбираем хеш-функцию (например, hashlib.sha256)
    hasher = hashlib.sha256()
    hasher.update(text.encode())
    return hasher.hexdigest()

def make_hash_table_with_superimposition():
    words = []  # список для хранения "чистых" слов
    # Открываем файл для чтения
    with open('/Users/a.sagitovich/programming/BFU/ASD/13/russian_text.txt', "r", encoding="utf-8") as file:
        lines = file.readlines()

        for line in lines:
            line = line.split()
            for word in line:
                # Обработка символов в начале и конце слова
                if word and word[-1] in '.,:;!?)-':
                    word = word[:-1]
                if word and word[0] in '(':
                    word = word[1:]

                if word and word not in words:
                    words.append(word)

    hash_table = {}  # Создаем пустую хеш-таблицу

    for word in words:
        word_length = len(word)  # Определяем длину каждого слова
        hash_value = hash_text(word)

        # Если ключа с такой длиной еще нет в хеш-таблице, создаем пустой список
        if word_length not in hash_table:
            hash_table[word_length] = {}

        # Если хеш-значение уже существует для данной длины, добавляем слово в список
        if hash_value in hash_table[word_length]:
            hash_table[word_length][hash_value].append(word)
        else:
            hash_table[word_length][hash_value] = [word]

    # Выводим хеш-таблицу
    for length, hash_values in hash_table.items():
        print(f'Key: {length}')
        for hash_value, word_list in hash_values.items():
            print(f'  Hash: {hash_value}\n  Value: {word_list}')
        print()

make_hash_table_with_superimposition()

