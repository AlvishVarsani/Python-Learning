import sys
import argparse


# print(sys.argv)
# name =sys.argv[1]
# print(f"My name is {name}")

#Instead of using argv use argparse
##When we use -- this is optional ,here we can add the parameter as required but
##without -- this mean this is requires so we cannot add the required parameter
##when we -- we need to specify python CLI.py Alvish --age 23
parser=argparse.ArgumentParser()
parser.add_argument("name",type=str,)
parser.add_argument("--age",type=int,required=True)

args=parser.parse_args()
print(f"My name is {args.name}")
print(f"Age {args.age}")