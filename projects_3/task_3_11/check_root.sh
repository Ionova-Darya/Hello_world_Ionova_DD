#!/bin/bash

check_root () {
	if [ $EUID -ne 0 ]; then
		echo "Предупреждение"
		exit 1
	fi
}

check_root
