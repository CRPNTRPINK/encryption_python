def encrypt(text, step):
    encrypt_text = ""
    for i in text:
        encrypt_text += chr(ord(i) + step)
    return encrypt_text


def decrypt(text, step):
    decrypt_text = ""
    for i in text:
        decrypt_text += chr(ord(i) - step)
    return decrypt_text


def find_max(text):
    count = {}
    for i in text:
        if count.get(i) is None:
            count.setdefault(i, 1)
        else:
            count[i] += 1
    max_word = list(filter(lambda x: x[1] == max(count.values()), count.items()))[0]
    return max_word


def hack(text):
    max_word = find_max(text)
    result = ""
    step = 0
    do = True
    try:
        while do:
            step += 1
            for i in max_word[0]:
                if chr(ord(i) + step) == " ":
                    for word in text:
                        result += chr(ord(word) + step)
                    do = False
                    break

    except ValueError:
        step = 0
        while do:
            step += 1
            for i in max_word[0]:
                if chr(ord(i) - step) == " ":
                    for word in text:
                        result += chr(ord(word) - step)
                    do = False
                    break
    return result


enc = encrypt("hello world                    ", 5)
dec = decrypt(enc, 5)

if __name__ == '__main__':
    print(enc)
    print(dec)
    print(hack(enc))