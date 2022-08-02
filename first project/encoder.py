alphabet = ["a", "b", "c", "d", "e", "f", "g",
            "h", "i", "j", "k", "l", "m", "n",
            "o", "p", "q", "r", "s", "t", "u",
            "v", "w", "x", "y", "z"]
alphabet_encrypted = ["01-", "02-", "03-", "04-", "05-", "06-", "07-",
                      "08-", "09-", "10-", "11-", "12-", "13-", "14-",
                      "15-", "16-", "17-", "18-", "19-", "20-", "21-",
                      "22-", "23-", "24-", "25-", "26-"]


def encode_text(input_text):
    encoded_text = text
    for i in range(len(alphabet)):
        encoded_text = encoded_text.replace(alphabet[i], alphabet_encrypted[i])
    return encoded_text


def decode_text(input_text):
    decoded_text = text
    for i in range(len(alphabet)):
        decoded_text = decoded_text.replace(alphabet_encrypted[i], alphabet[i])
    return decoded_text


text = "abcdefghijklmnopqrstuvwxyz"
encoded_text = encode_text(text)
decoded_text = decode_text(encoded_text)

print(text)
print(encoded_text)
print(decoded_text)
