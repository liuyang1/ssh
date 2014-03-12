#! /usr/bin/env bash

for i in *.png; do
    echo $i
    convert $i -colorspace Gray out/$i;
done
