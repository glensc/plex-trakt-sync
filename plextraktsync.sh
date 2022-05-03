#!/bin/sh
set -eu

file=$(readlink -f "$0")
dir=$(dirname "$file")

cd "$dir"

# without arguments, run sync first, then continue with watch
if [ -z "${1:-}" ]; then
	pipenv run plextraktsync sync
	set -- watch
fi

exec pipenv run plextraktsync "$@"
