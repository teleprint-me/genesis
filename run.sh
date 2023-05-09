#!/usr/bin/env bash

make
source .env
export OPENAI_API_KEY
./genesis
