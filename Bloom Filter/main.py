import sys
from bloom_filter import BloomFilter
import hashlib
import math
import uuid
from bitarray import bitarray

dictionary = ''
input = ''
output3 = ''
output5 = ''

# Basic error checking on argument number and parsing of CL args
if len(sys.argv) != 8:
    print("Incorrect argument count")
else:
    for i in range(len(sys.argv)):
        if sys.argv[i] == '-d':
            dictionary = sys.argv[i + 1]
        elif sys.argv[i] == '-i':
            input = sys.argv[i + 1]
        elif sys.argv[i] == '-o':
            output3 = sys.argv[i + 1]
            output5 = sys.argv[i + 2]

dictfile = open(dictionary, "r")
inpfile = open(input, "r")
out3file = open(output3, "w")
out5file = open(output5, "w")

for line in dictfile:
    print(hash(line))
    hash_object = hashlib.md5(line.encode())
    print(hash_object.hexdigest())
    hash_object = hashlib.sha1(line.encode())
    print(hash_object.hexdigest())
    hash_object = hashlib.sha224(line.encode())
    print(hash_object.hexdigest())
    hash_object = hashlib.sha256(line.encode())
    print(hash_object.hexdigest())
    hash_object = hashlib.sha384(line.encode())
    print(hash_object.hexdigest())
    hash_object = hashlib.sha512(line.encode())
    print(hash_object.hexdigest())
    salt = uuid.uuid4().hex
    hash_object = hashlib.sha512(salt.encode() + line.encode()).hexdigest() + ":" + salt
    print(hash_object)