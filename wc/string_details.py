def get_byte_count(data):
    return len(data.encode("utf-8"))

def get_line_count(data):
    lines = data.split("\n")
    return len(lines) if lines[-1] != "" else len(lines) - 1

def get_word_count(data):
    count = 0
    for wrd in data.split():
        count += 1
    return count

def get_char_count(data):
    return len(data)
