#!/bin/sh
set -eu

file=$(readlink -f "$0")
dir=$(dirname "$file")

cd "$dir"
exec pipenv run plextraktsync "$@"
