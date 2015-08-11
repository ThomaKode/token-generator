import hashlib
from hmac import sha
x = hashlib.md5()
x.update("Encrypt this text")
x.update(" With the preferred algorithm")
x.digest()

x.digest_size

x.block_size
