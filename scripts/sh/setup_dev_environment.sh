#!/usr/bin/env bash

pip install --user --upgrade pipx
pipx install poetry
poetry install
poetry shell
