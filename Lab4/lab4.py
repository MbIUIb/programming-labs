letters = [chr(i) for i in range(1072, 1104)] + [chr(i) for i in range(97, 122+1)] + ['ё']
ru_vowels = 'аоэеиыуёюя'
en_vowels = 'aeiouy'
vowels = ru_vowels + en_vowels
char_in_text = {}


# чтение файла
file = open('test.txt', encoding='utf-8')
text = file.read().lower()
file.seek(0)
text_list = file.readlines()
text_len = len(text)


# словарь со всеми символами из файла
for char in text:
    char_in_text.setdefault(char, 0)
    char_in_text[char] += 1


if ' ' in char_in_text:
    space = char_in_text[' ']
else:
    space = 0
if '\n' in char_in_text:
    n = char_in_text['\n']
else:
    n = 0


# подсчет гласных
count_ru_vowels = 0
count_en_vowels = 0
for vowel in char_in_text:
    if vowel in ru_vowels:
        count_ru_vowels += char_in_text[vowel]
    if vowel in en_vowels:
        count_en_vowels += char_in_text[vowel]
count_vowels = count_ru_vowels + count_en_vowels


# самая часто употребляемая буква
max_letter = [('', 0)]
for char in char_in_text:
    if char in letters:
        if char_in_text[char] > max_letter[0][1]:
            max_letter.clear()
            max_letter.append((char, char_in_text[char]))
        elif char_in_text[char] == max_letter[0][1]:
            max_letter.append((char, char_in_text[char]))


# запись ответов в файл
answer = open('answer.txt', 'w', encoding='utf-8')

answer.write('#### ДЛИНА ФАЙЛА ####\n')
answer.write(f'с учетом " ": {text_len-n}\n')
answer.write(f'без " ": {text_len-(n+space)}\n')

answer.write('\n#### КОЛИЧЕСТВО ГЛАСНЫХ ####\n')
answer.write(f'ru и en: {count_vowels}\n')
answer.write(f'ru: {count_ru_vowels}\n')
answer.write(f'en: {count_en_vowels}\n')

answer.write('\n#### САМАЯ ЧАСТО УПОТРЕБЛЯЕМАЯ БУКВА ####\n')
answer.write(f'количество повторений: {max_letter[0][1]}\n')
for i in range(len(max_letter)):
    answer.write(f'{max_letter[i][0]}\n')


answer.write('\n#### КОЛИЧЕСТВО СТРОК ####\n')
answer.write(f'{len(text_list)}\n')

# закрытие файлов
file.close()
answer.close()
