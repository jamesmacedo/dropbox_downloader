def find_folder_id(folders: [], folder: str):
    return {item[1]: item for item in folders}.get(folder, None)
