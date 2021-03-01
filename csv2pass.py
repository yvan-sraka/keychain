#! /usr/bin/env python3

import os, csv

with open("~/Desktop/pm_export.csv", newline="\n") as csvfile:
    for row in next(csv.reader(csvfile, delimiter=",", quotechar='"')):
        os.system(f'echo "{row[3]}\\n{row[3]}" | pass insert "{row[0]}/{row[2]}"')
