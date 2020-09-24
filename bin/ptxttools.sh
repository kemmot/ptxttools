#!/bin/bash

# rm timesheet.log

BINPATH=`dirname $0`
#python "$BINPATH/../timesheet/main.py" $@
#python3 -m "$BINPATH/../timesheet/" $@
python3 "$BINPATH/../src" "$@"
