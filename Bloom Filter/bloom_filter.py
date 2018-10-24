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

    def check3(self, item):
        digests = [0, 0, 0]
        digests[0] = int((hashlib.md5(item).hexdigest()), 16) % self.size
        digests[1] = int((hashlib.sha1(item).hexdigest()), 16) % self.size
        digests[2] = int((hashlib.sha224(item).hexdigest()), 16) % self.size
        
        if self.bit_array3[digests[0]] == False:
            return 2
        elif self.bit_array3[digests[1]] == False:
            return 2
        elif self.bit_array3[digests[2]] == False:
            return 2

        return 0

    def check5(self, item):
        digests = [0, 0, 0, 0, 0]
        digests[0] = int((hashlib.md5(item).hexdigest()), 16) % self.size
        digests[1] = int((hashlib.sha1(item).hexdigest()), 16) % self.size
        digests[2] = int((hashlib.sha224(item).hexdigest()), 16) % self.size
        digests[3] = int((hashlib.sha256(item).hexdigest()), 16) % self.size
        digests[4] = int((hashlib.sha512(item).hexdigest()), 16) % self.size
        
        if self.bit_array3[digests[0]] == False:
            return 2
        elif self.bit_array3[digests[1]] == False:
            return 2
        elif self.bit_array3[digests[2]] == False:
            return 2
        elif self.bit_array3[digests[3]] == False:
            return 2
        elif self.bit_array3[digests[4]] == False:
            return 2

        return 0

    @classmethod
    def get_size(self, n, p):
        m = -(n * math.log(p))/(math.log(2)**2)
        return int(m)