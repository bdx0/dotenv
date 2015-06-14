#!/bin/bash -

BASE_DIR=$(dirname $(readlink -f $0))

export GOPATH=$BASE_DIR:$GOPATH

go build main
