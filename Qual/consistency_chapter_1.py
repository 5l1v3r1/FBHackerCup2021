#!/usr/bin/env python3 -B -u
#-*- coding: utf-8 -*-

import sys
import string
import collections

def vowel(c): return c in "AEIOU"

if __name__ == "__main__":
	with open(sys.argv[1]) as f:
		idx = 0
		for line in f:
			line = line.strip()
			if not line: continue
			if idx == 0:
				idx += 1
				continue
			cnts = collections.Counter(line)
			ans = sys.maxsize
			for t in string.ascii_uppercase:
				N = 0
				for k,v in cnts.items():
					if k == t: continue
					else:
						if vowel(t) and vowel(k): N += 2*v
						elif not vowel(t) and vowel(k): N += v
						elif vowel(t) and not vowel(k): N += v
						else: N += 2*v
				ans = min(ans,N)
			print("Case #%d: %d"%(idx,ans))
			idx += 1
