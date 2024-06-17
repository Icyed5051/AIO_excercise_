def no_repeat(name):
    result = []
    for word in name:
        if(word not in result):
            result.append(word)
    return result


def create_dictionary(file_path):
    file = open(file_path,"r")
    file = file.read().lower()
    text = file.split()
    no_repeat_text = no_repeat(text)
    word_count = {word: 0 for word in no_repeat_text}
    for word in text:
        if(word in word_count):
            word_count[word] += 1
    return word_count

print(create_dictionary("P1_data.txt"))