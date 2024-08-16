def get_byte_count(file_path):
    from os import path
    return path.getsize(file_path)

def get_line_count(file_path):
    count = 0
    with open(file_path, "r") as fh:
        for line in fh:
            count += 1
    return count

def get_word_count(file_path):
    with open(file_path, "r") as fh:
        return len(fh.read().split())
#TODO: edit this piece of shit
def get_char_count(file_path):
    with open(file_path, "r") as fh:
        return len(fh.read()) + get_line_count(file_path)

def get_wc_details(file_path):
    """
    combines get_byte_count, get_line_count, get_word_count, get_char_count for performance purposes
    """
    with open(file_path, "r") as fh:
        byte_count = get_byte_count(file_path)
        line_count = 0
        word_count = 0
        char_count = 0
        for line in fh:
            line_count += 1
            word_count += len(line.strip().split())
            char_count += len(line)
        char_count += line_count
        return (line_count, word_count, char_count, byte_count)
