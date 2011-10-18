#!/usr/bin/env python
#       rmdup.py
#       removes duplicate files from a directory.
#       version 0.4

#       Usage
#       rmdup.py duplicate-dest dir1 dir2[dir3...]
#
#       will place a duplicate found in dir1,dir2,dir3 into duplicate-dest. Will only
#       leave one copy in the other directories.
#       eg a duplicate file in dir1 and dir2, dir1 has priority and the dup will be moved out from dir2
#
#       eg rmdup.py duplicates/ myPrimaryLibrary/ aFolderOfMusicToMergeWithMyLibrary/

# Copyright(c) 2007, 2011 Samuel G. D. Williams. <http://www.oriontransfer.co.nz>
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files(the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

wet = True

import sys, os, md5

def sumfile(file, whole = False):
	fsize = os.stat(file)[6]
	fobj = open(file)
	m = md5.new()
	m.update(`fsize`)
	if whole:
		while True:
			d = fobj.read(8096 * 16)
			if not d:
				break
			m.update(d)
	else:
		for i in range(2):
			d = fobj.read(8096 * 2)
			if not d:
				break
			m.update(d)
	return m.hexdigest()

def check(path):
	global unique, duplicates
	sum = sumfile(path)
	if unique.has_key(sum):
		duplicates.append((path, sum))
	else:
		unique[sum] =[path, '']

roots = sys.argv[2:]
to = sys.argv[1]

unique = {}
duplicates =[]

for dir in roots:
	print "Scanning", dir, "..." 
	for top, dirs, files in os.walk(dir):
		if len(files):
			print 'Checking', top
		for f in files:
			check(os.path.join(top, f))

print 'Verifying', len(duplicates), 'duplicates'

for k in duplicates:
	if unique[k[1]][1] == '':
		unique[k[1]][1] = sumfile(unique[k[1]][0], True)
		if wet:
			if sumfile(k[0], True) == unique[k[1]][1]:
				print 'Moving', k[0], 'duplicate of:', unique[k[1]][0]
				dst_dir = os.path.join(to, k[0][0 : k[0].rfind('/')])
				
				try:
					if not os.path.isdir(dst_dir):
						os.makedirs(dst_dir)
				except:
					print "Could not create directory:", dst_dir
				
				dst_path = os.path.join(to,k[0])
				
				try:
					os.rename(k[0], dst_path)
				except:
					print 'Error trying to move:', k[0], 'to:', dst_path
		else:
			print 'Found:', k[0], 'duplicate of:', unique[k[1]][0]
	else:
		print 'Similar match:', k[0] , 'of:', unique[k[1][0]]
