FROM python:3.10-slim

RUN apt-get update \
    && apt-get install -y --no-install-recommends gcc libxml2-dev \
    && pip install --no-cache-dir ovirt-engine-sdk-python \
    && apt-get remove -y gcc \
    && apt-get autoremove -y \
    && rm -rf /var/lib/apt/lists/*