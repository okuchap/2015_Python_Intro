class intDict(object):
    
    def __init__(self, numBuckets):
        self.buckets = []
        self.numBuckets = numBuckets
        for i in range(numBuckets):
            self.buckets.append([])
    
    def addEntry(self, dictKey, dictVal):
        hashBucket = self.buckets[dictKey % self.numBuckets]
        for i in range(len(hashBucket)):
            if hashBucket[i][0] == dictKey:
                hashBucket[i] = (dictKey, dictVal)
                return
        hashBucket.append((dictKey, dictVal))
    
    def getValue(self, dictKey):
        hashBucket = self.buckets[dictKey % self.numBucket]
        for e in hashBucket:
            if e[0] == dictKey:
                return e[1]
        return None
    
    def __str__(self):
        result = '{'
        for b in self.buckets:
            for e in b:
                result = result + str(e[0]) + ':' + str(e[1]) + ','
        return result[:-1] + '}'
        
    def countNonEmpty(self):
        count = 0
        for i in range(len(self.buckets)):
            if self.buckets[i] != []:
                count += 1
        return count
    
import random

D = intDict(29)

for i in range(20):
    key = random.randint(0, 10**5)
    D.addEntry(key, i)

print 'The value of the intDict is:'
print D
print len(D.buckets)
print D.countNonEmpty()

'''
print '\n', 'The buckets are:'
for hashBucket in D.buckets:
    print ' ', hashBucket
'''