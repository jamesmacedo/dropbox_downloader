# > pip install dropbox pick pp-ez
import dropbox
import argparse
import pp
import os
from pick import pick
from helpers import find_folder_id
from get_dropbox import get_folders, get_files

parser = argparse.ArgumentParser(description="Download files from Dropbox")
parser.add_argument('--token', type=str, help="Your Dropbox Token", required=False)
parser.add_argument('--interactive', type=bool, help="Your Dropbox Token", default=True, required=False)
parser.add_argument('--root', type=str, help="Target Dropbox folder", required=True)
parser.add_argument('--list', help="List folders", action='store_true', required=False)
parser.add_argument('--depth', help="Select a depth in the folder listing", type=int, required=False)
parser.add_argument('--download', type=str, help="Target download folder id", required=False)
parser.add_argument('--to', type=str, help="Target local folder", required=False)

args = parser.parse_args()


def auth(token):
    print('Authenticating with Dropbox...')
    dbx = dropbox.Dropbox(token)
    print('...authenticated with Dropbox owned by ' + dbx.users_get_current_account().name.display_name)
    return dbx


def download(folder, folder_id):
    if os.path.exists('downloads') is False:
        os.makedirs('downloads')
    download_dir = 'downloads/' + (args.to or folder[0].split('/')[-1] + '/')
    print('Files will be downloaded to ' + download_dir + '...')
    get_files(dbx, folder_id, download_dir)


def to_list(array, depth=1):
    if depth == 1:
        return array
    else:
        resultado = []
        for item in array:
            if isinstance(item, list) or isinstance(item, dict):
                resultado.append(list(item, depth - 1))
            else:
                resultado.append(item)
        return resultado


dbx = auth(args.token or open('token.txt').read().strip())
folders = get_folders(dbx, args.root.lower())


if(args.interactive is True):
    selected, idx = pick([name for name, _ in folders], "Please select one folder")
    found_folder = find_folder_id(folders, folders[idx][1])
    download(found_folder, found_folder[1])
    exit(1)

if (args.list is True):
    pp(to_list(folders, args.depth))
    exit(1)

found_folder = find_folder_id(folders, args.download)

if (found_folder is None):
    print(f'Folder {args.download} not found')
    exit(1)

download(found_folder, found_folder[1])
