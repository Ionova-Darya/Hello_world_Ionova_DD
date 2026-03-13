#!/bin/bash

awk '{print $1 $5
    if ($5 > 90)
    	print "Предупреждение"
}' df -h
