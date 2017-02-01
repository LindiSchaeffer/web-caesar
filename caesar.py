def alphabet_position(letter):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    ch = letter.lower()
    pos = alphabet.index(ch)
    return(pos)


def rotate_character(char, rot):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    rotated = ''
    if char.isalpha() != True:
        return char
    else:
        rotated_index = alphabet_position(char) + rot
        if rotated_index < 26:
            rotated += alphabet[rotated_index]
        else:
            rotated += alphabet[rotated_index % 26]

        if char.isupper():
            return rotated.upper()
        else:
            return rotated


def encrypt(text, rot):
    encrypted = []
    for char in text:
        new_char = rotate_character(char, rot)
        encrypted.append(new_char)

    return ''.join(encrypted)
