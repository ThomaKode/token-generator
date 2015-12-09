import hmac
import math

from hashlib import md5
#---pre: encode values

a = hmac.new("evilbillionaire:006da874-4268-4a07-940f-58e06ee36aa2",
         "ad5540553b02489586ae7ebbbd2562a8", md5).hexdigest()

b = hashlib.md5()
b.update(b"This is the string to be encrypted")
b.update(b"concatenated to this string")
b.digest()

#--post: Print result to file
f = open('workspace', 'r+b') #Create a file object 'f' for reading and writing
#in binary mode
print f(a)
