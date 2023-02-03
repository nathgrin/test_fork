
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-b", "--build-directory", nargs=1, type=str)
parser.add_argument("-f", "--force-overwrite", action="store_true")
parser.add_argument("-i", "--input-files", nargs="*", type=str)
parser.add_argument("-n", "--number-of-versions", nargs=1, type=int)
parser.add_argument("--output")

# type of output -> 
# question files
# compile


args = parser.parse_args()

print(args)
print("TODO: Call program")
