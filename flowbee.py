#!/usr/bin/env python2
'''
Simple CLI to send messages to a flowdock flow

os.env[FLOW_USER] or --user    = User name flow sent as
os.env[FLOW_TOKEN] or --token  = Flow API Token
--tags = Optional tags to add to message

Prints error otherwise "Success"
'''

import urllib2
import json
import os
import sys
from optparse import OptionParser

FLOW_API = 'https://api.flowdock.com/v1/messages/chat/%s'
HEADER = { 'Content-Type' : 'application/json' }
USAGE = "usage: %prog [options] message"

opts = OptionParser(USAGE)
opts.add_option('-u', '--user', dest="user", default=os.getenv('FLOW_USER'), help="User name to send as or ENV['FLOW_USER']")
opts.add_option('-t', '--token', dest="token", default=os.getenv('FLOW_TOKEN'), help="Flow API token or ENV['FLOW_TOKEN']")
opts.add_option('--tags', dest="tags", help="Optional tags to append to message")
(opt, args) = opts.parse_args()

if args:
    msg = " ".join(args)
else:
    opts.print_help()
    sys.exit(1)

''' Split tags and create the json payload '''
tags = opt.tags.split(',') if opt.tags else ""
payload = json.dumps({'content' : msg, "external_user_name" : opt.user, "tags" : tags })

''' Create Request and POST the data '''
request = urllib2.Request(FLOW_API % opt.token, payload, headers=HEADER)
try:
    f = urllib2.urlopen(request)
except urllib2.HTTPError, e:
    print "HTTP Error %s" % e.code



