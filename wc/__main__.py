import argparse
import file_details
from report import print_details
import string_details
from sys import stdin

# create argument parser
parser = argparse.ArgumentParser(description="Unix wc Recreation by abysspacer")

# add flags
parser.add_argument("-l", "--lines", action="store_true", help="count the lines of the input")
parser.add_argument("-w", "--words", action="store_true", help="count the words of the input")
parser.add_argument("-m", "--chars", action="store_true", help="count the characters of the input")
parser.add_argument("-c", "--bytes", action="store_true", help="count the bytes of the input")
parser.add_argument("file_path", type=str, nargs="?", help="path to target file")

# parse the arguments
args = parser.parse_args()

# default behavior
if not (args.lines or args.words or args.chars or args.bytes):
    args.lines = args.words = args.bytes = True

# enlist details
details = []

# file path provided
if args.file_path:
    if (args.lines and args.words) or (args.lines and args.chars) or (args.words and args.chars):
        line_c, word_c, char_c, byte_c = file_details.get_wc_details(args.file_path)
        details = [args.lines and line_c, args.words and word_c, args.chars and char_c, args.bytes and byte_c, args.file_path]
    else:
        details = [args.lines and file_details.get_line_count(args.file_path), args.words and file_details.get_word_count(args.file_path), args.chars and file_details.get_char_count(args.file_path), args.bytes and file_details.get_byte_count(args.file_path), args.file_path]

# file path not provided

# i dont think combinig the functionailty will improve the performance
# so this is what we got
else:
    data = stdin.read()
    details = [args.lines and string_details.get_line_count(data), args.words and string_details.get_word_count(data), args.chars and string_details.get_char_count(data), args.bytes and string_details.get_byte_count(data), args.file_path]

# sanitize details
details = [x for x in details if x]

# report to user
print_details(details)
