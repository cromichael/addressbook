#!/bin/bash
# This will remove the container after running
docker run --rm address_book -cf config.yaml -qs $1