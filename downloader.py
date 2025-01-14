# > pip install dropbox
import dropbox
import argparse
# import pp
import os
from helpers import find_folder_id
from get_dropbox import get_folders, get_files

parser = argparse.ArgumentParser(description="Download files from Dropbox")
parser.add_argument('--token', type=str, help="Your Dropbox Token", required=False)
parser.add_argument('--root', type=str, help="Target Dropbox folder", required=True)
parser.add_argument('--list', help="List folders", action='store_true', required=False)
parser.add_argument('--download', type=str, help="Target download folder id", required=False)
parser.add_argument('--to', type=str, help="Target local folder", required=False)

args = parser.parse_args()


def auth(token):
    print('Authenticating with Dropbox...')
    dbx = dropbox.Dropbox(token)
    print('...authenticated with Dropbox owned by ' + dbx.users_get_current_account().name.display_name)
    return dbx


def download(folder, folder_id):
    download_dir = args.to or folder[0].split('/')[-1] + '/'
    print('Files will be downloaded to ' + download_dir + '...')
    get_files(dbx, folder_id, download_dir)


dbx = auth(args.token or open('token.txt').read().strip())
folders = get_folders(dbx, args.root.lower())

if (args.list is True):
    print(folders)
    exit(1)

found_folder = find_folder_id(folders, args.download)

if (found_folder is None):
    print(f'Folder {args.download} not found')
    exit(1)

download(found_folder, found_folder[1])
