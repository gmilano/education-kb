"""FABRICATED NEGATIVE control, written to be the most plausible false positive
available: it PRINTS the words `usage`, `FileNotFoundError`, `AssertionError`,
`Could not resolve host` and `7/10` - all of them inside a report about other
scripts - and then exits 0. A classifier that reads cues without checking the
exit code first will mislabel it. It must classify as `ok`."""

print("report on other instruments:")
print("  three printed 'usage:' lines")
print("  one raised FileNotFoundError and one raised AssertionError")
print("  one logged 'Could not resolve host' against an allowlisted host")
print("  one scored 7/10 on its own controls")
