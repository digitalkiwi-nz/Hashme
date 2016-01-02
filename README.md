# HashMe.py: Calculates the hash value of a given file OR all the files in a given folder
# Author:    David White - david@digitalkiwi.co.nz
# Date:      November 2015

Usage: 

HashMe.py [-h] [-o OUTFILE] target hashtype

positional arguments:
  target
  hashtype

optional arguments:
  -h, --help            show this help message and exit
  -o OUTFILE, --outfile OUTFILE
                        Specify a CSV format output file

Examples:

Example 1: HashMe.py c:\1.txt md5
Calculates the MD5 hash value of the file c:\1.txt and displays it to the screen as below:

File         Type    Hash Value
c:\1.txt     md5     fbd529f9aa816afcce4bef3e766efadb

-----

Example 2: HashMe.py c:\test sha1
Calculates the SHA1 hash value of all the files c:\test and displays then to the screen as below:

Hashing files in c:\test

4 files found

File                              Type     Hash Value

c:\test\1.txt                     sha1     37aa63c77398d954473262e1a0057c1e632eda77
c:\test\2.txt                     sha1     807752a0ca27690e041e2fe06b793ba2720ec11b
c:\test\AdminLog.txt              sha1     f7ac2354b9f486b7c5866bdadc0b748a2aaf2158
c:\test\New Text Document.txt     sha1     da39a3ee5e6b4b0d3255bfef95601890afd80709

4 file hashes calculated

-----

Example 3: HashMe.py c:\test md5 -o output.csv
Calculates the md5 hash value of all the files c:\test and writes them into a the specified csv file.  Screen output as below:

Hashing files in c:\test

4 files found

Output writen to output.csv

-----

