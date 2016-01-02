# HashMe.py: Calculates the hash value of a given file OR all the files in a given folder
# Author:    David White
# Date:      November 2015

import os
import hashlib
import argparse
import csv

#  Hash the files
def hashfile(filename, hashtype):
    buffer_size = 65536
    try:
        hasher = hashlib.new(hashtype)
    except:
        print "[!] ERROR: Unsupported hash type '%s'." % hashtype
        print "[!] Acceptable values are: 'md5', 'sha1', 'sha224', 'sha256', 'sha384' and 'sha512'"
        quit()
    try:
        with open(filename, 'rb') as myfile:
            buffer = myfile.read(buffer_size)
            while len(buffer) > 0:
                hasher.update(buffer)
                buffer = myfile.read(buffer_size)
        hash_value = hasher.hexdigest()
        return filename, hashtype, hash_value
    except IOError as ioe:
        print "[!] ERROR (Hashfile IO): %s\n" % ioe
        if ioe.errno == 2:
            quit()
    except Exception as e:
        print "[!] ERROR (Hashfile): %s\n" % e

# Get hash valuse for target(s)
def get_hashes():
    target = os.path.normpath(args.target)
    hashtype = args.hashtype
    hashtype = hashtype.lower()
    result_list = []
    f_count = 0
    if os.path.isdir(target):  # if the target is a directory, do this
        try:
            print '\nHashing files in ' + target + '\n'
            for file in os.listdir(target):  # iterate through contents of directory
                if os.path.isfile(os.path.join(target, file)):  # if target is a file do this (we don't want to hash sub dirs)
                    filename = os.path.join(target, file)
                    result = hashfile(filename, hashtype)  # call the hashfile function
                    f_count += 1
                    if result is not None:
                        result_list.append(result)
        except Exception as e:
            print '[!] ERROR (Get Hashes): %s' % e

    else:  # else if the target is a single file do this
        try:
            result = hashfile(target, hashtype)
            if result is not None:
                result_list.append(result)
                f_count = 1
        except Exception as e:
            print '[!] ERROR (Get Hashes): %s' % e
    if f_count == 1:
        print ('%d file found\n' % f_count)
    else:
        print ('%d files found\n' % f_count)
    return result_list

#  Check if output file exists
def checkfile(filename):
    try:
        while os.path.exists(filename):
            #get new name
            ans = raw_input('[!] This file already exists. Press "Y" to overwrite it, or "N" to specify a new filename: ')
            ans = ans.lower()
            if ans == 'n':
                filename = raw_input('\nPlease enter the new filename: \n')
            else:
                break
        return filename
    except Exception as e:
            print '[!] ERROR (Check File): %s' % e

#  Write output to CSV file
def csv_out(result_list):
    output_file = checkfile(args.outfile)
    header = ('File', 'Type', 'Hash Value')
    try:
        with open(output_file, 'wb') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(header)
            for tup in result_list:
                writer.writerow(tup)
        print 'Output writen to %s' % output_file
    except Exception as e:
            print '[!] ERROR (CSV Out): %s' % e

#  Write output to std out
def std_out(result_list):
    #  Set up column widths
    x = 0
    y = 0
    z = 0
    count = 0
    for tup in result_list:
        if x < len(tup[0]):
            x = len(tup[0]) + 4
        if y < len(tup[1]):
            y = len(tup[1]) + 4
        if z < len(tup[2]):
            z = len(tup[2])
    print 'File'.ljust(x), 'Type'.ljust(y), 'Hash Value'.ljust(z)
    #  Print results
    for tup in result_list:
        print tup[0].ljust(x), tup[1].ljust(y), tup[2].ljust(z)
        count = count + 1
    if count == 1:
        print "\n%d file hash calculated" % count
    else:
        print "\n%d file hashes calculated" % count

def main():
    if args.outfile:
        csv_out(get_hashes())
    else:
        std_out(get_hashes())

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('target')
    parser.add_argument('hashtype')
    parser.add_argument('-o', '--outfile', help="Specify a CSV format output file")
    args = parser.parse_args()
    main()
