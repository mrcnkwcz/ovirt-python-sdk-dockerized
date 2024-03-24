import os
import sys
import logging

import ovirtsdk4 as sdk


logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s - %(message)s",
    stream=sys.stdout,
)
log = logging.getLogger(__name__)

# Create connection to engine server
connection = sdk.Connection(
    url=os.environ.get("OVIRT_URL"),
    username=os.environ.get("OVIRT_USER"),
    password=os.environ.get("OVIRT_PASSWORD"),
    ca_file=os.environ.get("OVIRT_CAFILE"),
)
# Test connection
if connection.test(raise_exception=False):
    log.info("Connection works")
else:
    log.error("Connection doesn't work")
# Close connection
connection.close()
