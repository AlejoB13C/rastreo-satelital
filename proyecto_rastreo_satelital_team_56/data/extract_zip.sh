#!/bin/bash

xlsx_files=$(zipinfo -1 $1 | grep -E '\.xlsx$')

while IFS= read -r line < $variable;
do 
    echo $line; 
done; <<<"$xlsx_files"