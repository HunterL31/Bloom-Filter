import hashlib
import math
import uuid
from bitarray import bitarray

class BloomFilter(object):
    def __init__(self, itemcount, fpprob):
        self.fp_prob = fpprob
        self.size = self.get_size(itemcount, fpprob)
        self.bit_array3 = bitarray(self.size)
        self.bit_array3.setall(0)
        self.bit_array5 = bitarray(self.size)
        self.bit_array5.setall(0)

    def add(self, item):
        #Add an item to the filter
        digest = hashlib.md5(item).hexdigest()
        self.bit_array3[int(digest, 16) % self.size] = True
        self.bit_array5[int(digest, 16) % self.size] = True
        digest = hashlib.sha1(item).hexdigest()
        self.bit_array3[int(digest, 16) % self.size] = True
        self.bit_array5[int(digest, 16) % self.size] = True
        digest = hashlib.sha224(item).hexdigest()
        self.bit_array3[int(digest, 16) % self.size] = True
        self.bit_array5[int(digest, 16) % self.size] = True
        digest = hashlib.sha256(item).hexdigest()
        self.bit_array5[int(digest, 16) % self.size] = True
        digest = hashlib.sha512(item).hexdigest()
        self.bit_array5[int(digest, 16) % self.size] = True

    def check(self, item):
        print("hi")
        #Check for item presence in filter
        #Hash either 3 or 5 times
        #Get set of positions and check if each one is a 0
        #If you find a 0, password is good
        #Else password is bad

    @classmethod
    def get_size(self, n, p):
        m = -(n * math.log(p))/(math.log(2)**2)
        return int(m)