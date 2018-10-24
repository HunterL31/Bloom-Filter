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

dictfile = open(dictionary, "r")
for line in dictfile:
    n = n + 1
dictfile.close()

dictfile = open(dictionary, "r")
bloomf = BloomFilter(n, p)
print("Bloom filter size: {}".format(bloomf.size))
print("False positive probability: {}".format(bloomf.fp_prob))
print("Using hash functions: MD5, SHA1, SHA224, SHA256, SHA512")

t0 = time.time()
for line in dictfile:
    bloomf.add(line)
t1 = time.time()
dictfile.close()
print("Created bloom filters in {} seconds".format(t1-t0))

print("Checking input file {}".format(input))

inpfile = open(input, "r")
out3file = open(output3, "w")
for line in inpfile:
    value = bloomf.check3(line)
    if value == 0:
        out3file.write("Bad\n")
    elif value == 1:
        out3file.write("Maybe\n")
    elif value == 2:
        out3file.write("Good\n")
out3file.close()
inpfile.close()

inpfile = open(input, "r")
out5file = open(output5, "w")
for line in inpfile:
    value = bloomf.check5(line)
    if value == 0:
        out5file.write("Bad\n")
    elif value == 1:
        out5file.write("Maybe\n")
    elif value == 2:
        out5file.write("Good\n")
out5file.close()
inpfile.close()

print("Output for k=3 stored in {}".format(output3))
print("Output for k=5 stored in {}".format(output5))