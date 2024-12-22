from typing import List

def play(words: List[str]) -> List[int]:
    seen_words = set()  # Множество для хранения уже произнесенных слов
    error_indices = []  # Список для хранения индексов слов с ошибками
    
    if not words:
        return error_indices
    
    last_valid_word = words[0]
    seen_words.add(last_valid_word)
    
    for i in range(1, len(words)):
        word = words[i]
        
        # Проверка на повторение слова
        if word in seen_words:
            error_indices.append(i + 1)  # Индексы начинаются с 1
            continue
        
        # Проверка на правильность начала слова
        if word[0] != last_valid_word[-1]:
            error_indices.append(i + 1)
            
        else:
            seen_words.add(word)
            last_valid_word = word
        
    
    return error_indices

# Пример использования
words =["sunflower", "river", "river", "rabbit", "tree", "eagle", "tree"]
print(play(words))  # Вывод: [3, 4, 6]
