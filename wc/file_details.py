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
