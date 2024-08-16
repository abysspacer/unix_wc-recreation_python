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
parser.add_argument("file_path", type=str, nargs="*", help="path to target file")

# parse the arguments
args = parser.parse_args()

# default behavior
if not (args.lines or args.words or args.chars or args.bytes):
    args.lines = args.words = args.bytes = True

# enlist details
details = []

# file path provided
if args.file_path:
    
    #single-file mode
    if len(args.file_path) == 1:
        if (args.lines and args.words) or (args.lines and args.chars) or (args.words and args.chars):
            line_c, word_c, char_c, byte_c = file_details.get_wc_details(args.file_path[0])
            details = [args.lines and line_c, args.words and word_c, args.chars and char_c, args.bytes and byte_c, args.file_path[0]]
        else:
            details = [args.lines and file_details.get_line_count(args.file_path[0]), args.words and file_details.get_word_count(args.file_path[0]), args.chars and file_details.get_char_count(args.file_path[0]), args.bytes and file_details.get_byte_count(args.file_path[0]), args.file_path[0]]
    
    # multi-file mode
    else:
        total_line_count = total_word_count = total_char_count = total_byte_count = 0
        if (args.lines and args.words) or (args.lines and args.chars) or (args.words and args.chars):
            for fp in args.file_path:
                line_c, word_c, char_c, byte_c = file_details.get_wc_details(fp)
                total_line_count += line_c
                total_word_count += word_c
                total_char_count += char_c
                total_byte_count += byte_c
                details = [args.lines and line_c, args.words and word_c, args.chars and char_c, args.bytes and byte_c, fp]

                # sanitize details
                details = [x for x in details if x]

                # report to user
                print_details(details)
        else:
            #TODO: dear me, I'm sorry
            # please fix this
            # doesnt report total
            # and generally sucks
            for fp in args.file_path:
                details = [args.lines and file_details.get_line_count(fp), args.words and file_details.get_word_count(fp), args.chars and file_details.get_char_count(fp), args.bytes and file_details.get_byte_count(fp), fp]

                total_line_count += details[0] or 0
                total_word_count += details[1] or 0
                total_char_count += details[2] or 0
                total_byte_count += details[3] or 0
                # sanitize details
                details = [x for x in details if x]

                # report to user
                print_details(details) 
        
        # ready the total report
        details = [args.lines and total_line_count, args.words and total_word_count, args.chars and total_char_count, args.bytes and total_byte_count, "total"] 
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
