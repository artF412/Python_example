import os
import time

def countFolderAndFilesLisst ():

    path = '/Users/admin/Documents'
    now = time.time()
    fileCount = 0
    folderCount = 0

    for root , fol , fil in os.walk(path):

        # Sum folders and files count number
        folderCount += len(fol)
        fileCount += len(fil)

        for item in fol+fil:
            
            # List folders and files less than 7 days.
            item_path = os.path.join(root, item)
            last_modified = os.path.getmtime(item_path)
            time_diff = now - last_modified

            # check if the time difference is less than 7 day
            if time_diff < (7*24*60*60):
                days_diff = int(time_diff / (24*60*60))
                print(f'{item} in {item_path} was last modified {days_diff} days.')

    print(f'Folders Count Number : {folderCount} Folders')
    print(f'Files Count Number : {fileCount} Files')

countFolderAndFilesLisst()