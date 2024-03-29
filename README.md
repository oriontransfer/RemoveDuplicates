RemoveDuplicates
================

This script was developed to find and remove duplicate music files from large music libraries that had been copied multiple times on to different computers. The libraries had since been updated independently. This tool allows the duplicate files to be removed quickly, even on libraries spanning 100s of gigabytes.

	rmdup.py $duplicates_path $dir1 $dir2 [$dir3...]

This command will place a duplicate found in (`$dir1`, `$dir2`, `$dir3`) into `$duplicates_path`. It will only leave one copy in the original set of directories, with the left most directory having top priority, e.g. in the case that files `$dir1/f1.ogg` and `$dir2/f2.ogg` are the same, `f2.ogg` will be moved to `$duplicates_path/$dir2/f2.ogg`.

Example
-------

	$ ./rmdup.py dups test_a test_b test_c
	Scanning test_a ...
	Checking test_a
	Scanning test_b ...
	Checking test_b
	Scanning test_c ...
	Checking test_c
	Verifying 3 duplicates
	Moving test_b/README.md duplicate of: test_a/README.md
	Duplicate test_b/README.md renamed to dups/test_b/README.md
	Moving test_b/rmdup.py duplicate of: test_a/rmdup.py
	Duplicate test_b/rmdup.py renamed to dups/test_b/rmdup.py
	Moving test_c/process_benchmark_data.rb duplicate of: test_b/process_benchmark_data.rb
	Duplicate test_c/process_benchmark_data.rb renamed to dups/test_c/process_benchmark_data.rb

License
-------

Copyright (c) 2007, 2011 Samuel G. D. Williams. <http://www.oriontransfer.co.nz>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.