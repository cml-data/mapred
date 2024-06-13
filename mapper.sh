#!/usr/bin/bash

while read -r line;
  do
    for word in `echo $line | tr -d -c '[:alpha:][:blank:]'`;
      do
        printf '%s\t%s\n' $word 1
      done
  done
