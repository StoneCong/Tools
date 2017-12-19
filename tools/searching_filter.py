#!/usr/bin/python

import os
import sys

def search_file(file, pattern, exclude):

  count = 0
  lines = []
  result = []

  with open(file) as f:
    for line in f:
      count += 1
      lines.append((count, line.rstrip()))

  for num, line in lines:
    if pattern not in line:
      continue
    if len(exclude) and (exclude in line):
      continue
    result.append(file + ":" + str(num) + " " + line)

  return result

def main():

  if len(sys.argv) < 3:
    print "search_filter.py 'dir_path' 'pattern' 'exclude'"
    return

  pattern = sys.argv[2]
  exclude = "" if len(sys.argv) == 3 else sys.argv[3]

  for root, _, files in os.walk(sys.argv[1]):
    for file in files:
      path = root + '/' + file
      for line in search_file(path, pattern, exclude):
        print line

if __name__ == "__main__":
  main()
