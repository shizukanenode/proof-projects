# Incident Report

## Summary
A suspicious IP address triggered repeated failed SSH login attempts.

## Evidence 
The IP address `185.220.101.1` generated 3 failed  login attempts in `sample_logs/auth.log`.

## Assessment
This activity looks like a possible brute-force or unauthorized login attempt.

## Recommended Action
Block the source IP, review authentication logs, and confirm whether any successful login followed the failed attempts.
