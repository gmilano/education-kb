#!/bin/sh
# Compile the production validator against test-only stand-ins for the Bean
# Validation container and commons-lang3, then run the cases. Pure JDK: no
# third-party dependency is downloaded or installed.
set -e
here=$(cd "$(dirname "$0")" && pwd)
out="${TMPDIR:-/tmp}/seb-proctoring-validator-build"
rm -rf "$out" && mkdir -p "$out"
javac -nowarn -d "$out" \
  $(find "$here/testsupport" "$here/src" "$here/test" -name '*.java')
java -cp "$out" ValidatorTest
