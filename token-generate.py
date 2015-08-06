import hmac
from hashlib import md5
hmac.new("evilbillionaire:006da874-4268-4a07-940f-58e06ee36aa2",
         "ad5540553b02489586ae7ebbbd2562a8", md5).hexdigest()
