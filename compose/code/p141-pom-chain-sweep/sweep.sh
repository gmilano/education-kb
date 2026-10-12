#!/bin/sh
# p141-pom-chain-sweep — ACTION DC: apply p140's parent-POM walk to EVERY Maven coordinate
# this KB cites, not just the five on the LTI shelf.
#
# The walker itself is p140's, unchanged and re-used deliberately: a sweep that re-implements
# its instrument cannot tell a changed verdict from a changed method. Only the population is
# new. Maven Central answers 429 through this environment's proxy under load, so the walker's
# own backoff does the work and a failure is reported as a failure, never as an absence.
exec python3 -I ../p140-pom-parent-chain/pom_chain.py \
  org.imsglobal:basiclti-util:1.2.0 \
  org.verapdf:verapdf-library:1.30.3 \
  org.jasig.ssp:ssp:2.8.0 \
  org.sakaiproject:kernel:23.3 \
  uk.ac.ox.ctl:spring-security-lti13:0.3.7
