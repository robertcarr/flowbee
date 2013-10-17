FLOWBEE
=======

Uber simple CLI to post messages with optional tags to a flowdock flow.

USAGE
=======

with ENV variables
export FLOW_USER=user to post as
export FLOW_TOKEN=API Token for specific flow

./flowbee.py "message"

OR

./flowbee.py --user <user> --token <apitoken> "message"

```
Usage: flowbee.py [options] message

Options:
  -h, --help            show this help message and exit
  -u USER, --user=USER  User name to send as or ENV['FLOW_USER']
  -t TOKEN, --token=TOKEN
                        Flow API token or ENV['FLOW_TOKEN']
  --tags=TAGS           Optional tags to append to message
```
