#!/usr/bin/bash

current_word=''
current_count=0
word=''
IFS=$'\t'

while read -r line; do
  read -a array <<< $line
  word="${array[0]}"
  count="${array[1]}"
  if [ $word == $current_word ]; then
    ((current_count=current_count+count))
  else
    if [ "$current_word" != '' ]; then
      printf '%s\t%s\n' $current_word $current_count

    fi
    current_count=$count
    current_word=$word
  fi
done
if [ "$current_word" == "$word" ]; then
  printf '%s\t%s\n' $current_word $current_count
fi
