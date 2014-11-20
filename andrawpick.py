import os
import re
import shutil
import argparse

SIZES = ['mdpi', 'hdpi', 'xhdpi', 'xxhdpi', 'xxxhdpi']

def filter_files(res_folder, regex, sizes):
    files = {}
    for size in sizes:
        walk_path = os.path.join(res_folder, 'drawable-' + size)
        try:
            for file_found in os.listdir(walk_path):
                if regex.match(file_found):
                    if size not in files or not files[size]:
                        files[size] = []
                    files[size].append(file_found)
        except OSError:
            continue
    return files

def process_request(src_folder, dest_folder, regex_def='.*', sizes=SIZES):
    filter_re = re.compile(regex_def, re.IGNORECASE)
    res_files = filter_files(src_folder, filter_re, sizes)
    if not res_files:
        print ('No file found matching {}'.format(regex_def))
        exit(0)
    for size in sizes:
        if size not in res_files:
            continue
        for res_file in res_files[size]:
            folder_size = 'drawable-' + size
            src_file = os.path.join(src_folder, folder_size, res_file)
            dest_file = os.path.join(dest_folder, folder_size, res_file)
            try:
                print('\nCOPYING {} IN {}'.format(src_file, dest_file))
                shutil.copy2(src_file, dest_file)
                print('SUCCESS!')
            except IOError:
                print('FAILURE!')

def main():
    parser = argparse.ArgumentParser(description='A simple script to pick Android drawables from a folder and put them into your project.')
    parser.add_argument('src', default='./', help='Source res folder path.')
    parser.add_argument('-d', '--dest', default='./', help='Destination res folder path.')
    parser.add_argument('-f', '--file', default='.*', help='File name regex.')
    parser.add_argument('-s', '--sizes', type=str, nargs='+', help='Sizes you want (mdpi, hdpi etc..)')
    args = parser.parse_args()

    if not args.sizes:
        args.sizes = SIZES

    process_request(args.src, args.dest, args.file, args.sizes)

if __name__ == '__main__':
    main()