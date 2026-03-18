#!/bin/bash

awk '$2 > 80 {print $0}' student.txt
awk '$2 < 70 {print $0}' student.txt
awk 'NR == 1 {print $0}' student.txt
