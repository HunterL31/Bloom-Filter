import hashlib
import math
import uuid
from bitarray import bitarray

class BloomFilter(object):
    def __init__(self, itemcount, fpprob):
        self.fp_prob = fpprob
        self.size = self.get_size(itemcount, fpprob)
        self.bit_array = bitarray(self.size)
        self.bit_array.setall(0)

    @classmethod
    def get_size(self, n, p):
        m = -(n * math.log(p))/(math.log(2)**2)
        return int(m)