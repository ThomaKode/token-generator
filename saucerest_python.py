import httplib
import base64
try:
    import json
except ImportError:
    import simplejson as json

config = {"username": "evilbillionaire",
          "access-key": "006da874-4268-4a07-940f-58e06ee36aa2"}

base64string = base64.encodestring('%s:%s' % (config['username'], config['access-key']))[:-1]

def set_test_status(jobid, passed=True):
    body_content = json.dumps({"passed": passed})
    connection = httplib.HTTPConnection("saucelabs.com")
    connection.request('PUT', '/rest/v1/%s/jobs/%s' % (config['username'], jobid),
                       body_content,
                       headers={"Authorization": "Basic %s" % base64string})
   result = connection.getresponse()
   return result.status == 200

set_test_status("cca9bd0238374e8d9d2068237623e5cd", passed=True)   
