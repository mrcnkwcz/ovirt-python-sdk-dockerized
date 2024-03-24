# oVirt Python SDK Dockerized
oVirt SDK with Docker

## Build image
`docker build . --tag ovirt-sdk-python --label ovirt`

## Environment variables
- `OVIRT_URL` - URL of the oVirt engine API
- `OVIRT_USER` - The username for the oVirt engine
- `OVIRT_PASSWORD` - The password for the oVirt engine
- `OVIRT_CAFILE` - A file containing the CA certificate in PEM format
