print("Зашифрование")
text = input("Введите текст: ")
key = int(input("Введите ключ: "))

def caesar(text, key): 

  cipherText = ""

  for ch in text:
    if ch.isalpha():
      letter = ord(ch) + key 
      if letter > ord('я'):
        letter -= 32
      finalLetter = chr(letter)
      cipherText += finalLetter
  print("Шифр:", cipherText)

caesar(text, key)

print("---------------------------")

print("Расшифрование")
text = input("Введите текст: ")
key = int(input("Введите ключ: "))

def decaesar(text, key): 

  cipherText = ""

  for ch in text:
    if ch.isalpha():
      letter = ord(ch) - key 
      if letter > ord('я'):
        letter -= 32
      finalLetter = chr(letter)
      cipherText += finalLetter
  print("Расшифровка:", cipherText)

decaesar(text, key)
