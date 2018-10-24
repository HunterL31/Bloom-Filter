import sys
from bloom_filter import BloomFilter
import hashlib
import math
import uuid
from bitarray import bitarray
import time

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

p = .05    #Desired false positive probablility
n = 0       #Will be the number of entries in the dictionary file

#Open all desired files
dictfile = open(dictionary, "r")
for line in dictfile:
    n = n + 1
dictfile.close()
dictfile = open(dictionary, "r")
inpfile = open(input, "r")
out3file = open(output3, "w")
out5file = open(output5, "w")

bloomf = BloomFilter(n, p)
print("Bloom Filter size: {}".format(bloomf.size))
print("False Positive Probability: {}".format(bloomf.fp_prob))
print("Using Hash Functions: MD5, SHA1, SHA224, SHA256, SHA512")

for line in dictfile:
    bloomf.add(line)
