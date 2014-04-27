#! /usr/bin/env bash
k=(8 12 16 20 24)

for val in ${k[@]}
do
    echo "K=$val" > conf.py
    echo "K=$val"
    python hashing.py
    python radius.py
done
