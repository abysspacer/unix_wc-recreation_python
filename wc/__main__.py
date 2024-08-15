import argparse
from file_details import get_byte_count, get_line_count, get_word_count, get_char_count, get_file_wc_details
from report import print_details

# create argument parser
parser = argparse.ArgumentParser(description="Unix wc Recreation by abysspacer")

# add flags
parser.add_argument("-l", "--lines", action="store_true", help="count the lines of the input")
parser.add_argument("-w", "--words", action="store_true", help="count the words of the input")
parser.add_argument("-m", "--chars", action="store_true", help="count the characters of the input")
parser.add_argument("-c", "--bytes", action="store_true", help="count the bytes of the input")
parser.add_argument("file_path", type=str, help="path to target file")

# parse the arguments
args = parser.parse_args()

# default behavior
if not (args.lines or args.words or args.chars or args.bytes):
    args.lines = args.words = args.bytes = True

# enlist and sanitize details
details = []
if (args.lines and args.words) or (args.lines and args.chars) or (args.words and args.chars):
    line_c, word_c, char_c, byte_c = get_file_wc_details(args.file_path)
    details = [args.lines and line_c, args.words and word_c, args.chars and char_c, args.bytes and byte_c, args.file_path]
else:
    details = [args.lines and get_line_count(args.file_path), args.words and get_word_count(args.file_path), args.chars and get_char_count(args.file_path), args.bytes and get_byte_count(args.file_path), args.file_path]
details = [x for x in details if x]

# report to user
print_details(details)
