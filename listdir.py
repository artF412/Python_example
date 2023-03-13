import os
import time

# def listdirPath():
#     path = '/Users/admin/Documents'
#     now = time.time()
#     for root, dirs, files in os.walk(path):
#         for item in files + dirs:
#         # get the full path to the item
#             item_path = os.path.join(root, item)
        
#         # get the last modified time of the item
#             last_modified = os.path.getmtime(item_path)
        
#         # calculate the number of seconds between now and the last modified time
#             time_diff = now - last_modified
        
#         # check if the time difference is less than 7 days (in seconds)
#             if time_diff < (7 * 24 * 60 * 60):
#                 days_diff = int(time_diff / (24 * 60 * 60))
#                 print(f"{item} in {item_path} was last modified {days_diff} days ago.")
    
    
# def listWalk():
    
#     filesCount = 0
#     foldersCount = 0
#     for path,lis_fol,lis_fai in os.walk('/Users/admin/Documents'):
#         foldersCount += len(lis_fol)
#         filesCount += len(lis_fai)
#     print('มีโฟลเดอร์ '+str(foldersCount)+' โฟลเดอร์')
#     print('มีไฟล์ '+str(filesCount)+' ไฟล์')
#     listdirPath()
    
# listWalk()

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

            if time_diff < (7*24*60*60):
                days_diff = int(time_diff / (24*60*60))
                print(f'{item} in {item_path} was last modified {days_diff} days.')

    print(f'Folders Count Number {folderCount}')
    print(f'Files Count Number {fileCount}')

countFolderAndFilesLisst()



            
                    
