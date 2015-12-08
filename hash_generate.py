import hashlib
from hmac import md5
x = hashlib.new('stripe-master84')
x.update("Encryt this text with the preffered algorithm")
x.hexdigest()
