#1
sentence = input("Введите предложение: ")
words = sentence.split()
average_length = sum(len(word) for word in words) / len(words) if words else 0
print(f"Средняя длина: {average_length:.2f}")

#2
text = input("Введите текст: ")
word = input("Введите слово для поиска: ")
count = text.lower().count(word.lower())
print(f"Слово '{word}' встречается {count} раз.")

#3
text = input("Введите текст: ").lower()
most_common = max(set(text), key=text.count)
print(f"Чаще всего встречается буква: '{most_common}'")

#4
text = input("Введите ряд (до 50 символов): ")[:50]

for i in range(1, len(text) + 1):
    print(" " * (len(text) - i) + text[:i])
for i in range(1, len(text)):
    print(" " * i + text[i:])

#5
spam_keywords = [
    "кредит", "скорое одобрение", "наличные", "скидка", "распродажа", "выигрыш",
 "viagra", "похудение", "лучший продукт", "легкий заработок", "без риска",
 "быстрые деньги", "выиграй деньги", "деньги за регистрацию", "легко и быстро",
 "срочно", "только сегодня", "суперпредложение", "не упустите шанс",
 "подарки для вас", "новые скидки"
]

text = input("Введите текст: ").lower()

if any(keyword in text for keyword in spam_keywords):
    print("ЭТО НЕ СПАМ!")
else:
    print("Это не спам.")