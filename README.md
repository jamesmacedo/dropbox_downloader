# Dropbox Downloader

A Python-based tool for downloading files from Dropbox. This script allows you to list folders, authenticate with your Dropbox account, and download files to a local directory.

---

Disclaimer:

This code was based in the following GIST: [GOTO](https://gist.github.com/hannesdatta/10422a6fbb584f245c83361245335741)

Huge thanks to [hannesdatta](https://github.com/hannesdatta)

## Requirements

- Python 3.x
- Dropbox Python SDK
- Token for Dropbox API

## Installation

1. Install the required library:

   ```bash
   pip install dropbox
   ```

2. Clone or download this repository.

3. Ensure you have a valid Dropbox API token.

## Usage

Run the script using the following command:

```bash
python downloader.py --root "/Your Folder" --download "id:your-folder-id"
```

### Arguments

| Argument        | Description                                                                 | Required          |
|-----------------|-----------------------------------------------------------------------------|-------------------|
| `--token`       | Your Dropbox API token. If omitted, the script reads the token from `token.txt`. | No                |
| `--root`        | The root Dropbox folder to target.                                         | Yes               |
| `--list`        | List all folders in the specified root directory.                         | No (flag option)  |
| `--download`    | The ID of the folder to download.                                          | Yes (if downloading) |
| `--to`          | Target local folder for downloads. Defaults to the folder name in Dropbox. | No                |

## Example Commands

### List folders

```bash
python downloader.py --root "/Your Folder" --list
```

### Download a folder

```bash
python downloader.py --root "/Your Folder" --download "id:rL8lR-oSFTIAAABBBBV56w"
```

### Download to a specific local directory

```bash
python downloader.py --root "/Your Folder" --download "id:rL8lR-oSFTIAAABBBBV56w" --to "/path/to/local/folder"
```

## File Structure

Ensure the following files are present:

- `downloader.py`: The main script.
- `helpers.py`: Contains helper functions, including `find_folder_id`.
- `get_dropbox.py`: Handles interactions with Dropbox, such as `get_folders` and `get_files`.
- `token.txt`: Optional file to store your Dropbox API token (omit if providing via `--token` argument).

## Authentication

The script authenticates with Dropbox using your API token. You can pass the token via the `--token` argument or save it in a `token.txt` file in the same directory as the script.

## Dependencies

- `dropbox`

Install via pip:

```bash
pip install dropbox
```

## Notes

- Ensure your Dropbox API token has the necessary permissions to access the folders and files.
- Use the `--list` argument to explore folder IDs before downloading.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

Happy downloading!
