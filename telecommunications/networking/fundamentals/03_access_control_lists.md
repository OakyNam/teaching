# Access Control Lists

## Overview
Access control lists (ACLs) are ordered allow/deny rules for traffic. They are a networking version of an if/else chain: the first matching rule wins.

## What ACLs Usually Match
- Source IP or subnet
- Destination IP or subnet
- Protocol such as TCP or UDP
- Destination port
- Direction (ingress or egress)

## Programmer Mental Model
Think of ACLs like request middleware. A packet walks through the rule list until one rule decides the outcome.

## Best Practices
- Start with the smallest allow list possible.
- Put the most specific rules before broad ones.
- Document why a rule exists.
- Review rules regularly so old access paths do not linger.

## Exercises
1. Explain why rule order matters.
2. Describe one risk of a broad `allow any` rule.
3. Map an ACL to an application middleware check.

## Answer Key
1. ACLs usually stop at the first match, so order changes the result.
2. It can expose services to traffic that was never intended to reach them.
3. Both examine incoming requests and decide whether processing continues.
