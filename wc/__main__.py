import argparse
from file_details import get_byte_count
from report import print_details

# create argument parser
parser = argparse.ArgumentParser(description="Unix wc Recreation by abysspacer")

# add flags
parser.add_argument("-c", "--bytes", action="store_true", help="count the bytes of the input")
parser.add_argument("file_path", type=str, help="path to target file")

# parse the arguments
args = parser.parse_args()

# report to user
if args.bytes:
    print_details([get_byte_count(args.file_path), args.file_path])
