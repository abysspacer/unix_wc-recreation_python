import argparse
from file_details import get_byte_count, get_line_count, get_word_count
from report import print_details

# create argument parser
parser = argparse.ArgumentParser(description="Unix wc Recreation by abysspacer")

# add flags
parser.add_argument("-l", "--lines", action="store_true", help="count the lines of the input")
parser.add_argument("-w", "--words", action="store_true", help="count the words of the input")
parser.add_argument("-c", "--bytes", action="store_true", help="count the bytes of the input")
parser.add_argument("file_path", type=str, help="path to target file")

# parse the arguments
args = parser.parse_args()

# enlist and sanitize details
details = [args.lines and get_line_count(args.file_path), args.words and get_word_count(args.file_path), args.bytes and get_byte_count(args.file_path), args.file_path]
details = [x for x in details if x]

# report to user
print_details(details)
