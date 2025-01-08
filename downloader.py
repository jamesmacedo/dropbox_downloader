# > pip install dropbox
import os
import dropbox
import argparse
from helpers import find_folder_id
from get_dropbox import get_folders, get_files

parser = argparse.ArgumentParser(description="Download files from Dropbox")
parser.add_argument('--token', type=str, help="Your Dropbox Token", required=True)
parser.add_argument('--root', type=str, help="Target Dropbox folder", required=True)
parser.add_argument('--download', type=str, help="Target download directory", required=False)
parser.add_argument('--to', type=str, help="Target local folder", required=False)

args = parser.parse_args()
print('Authenticating with Dropbox...')
dbx = dropbox.Dropbox(args.token)
print('...authenticated with Dropbox owned by ' + dbx.users_get_current_account().name.display_name)

folders = get_folders(dbx, args.root.lower())
found_folder = find_folder_id(folders, args.download.lower())
if(found_folder is None):
    print(f'Folder {args.download} not found')
    exit(1)

folder_id = found_folder[1]
download_dir = args.to or found_folder[0].split('/')[-1]

print('Obtaining list of files in target directory...')
get_files(dbx, folder_id, download_dir)
