import os
import shutil

subdir_find = '3D/MR'
rootdir = '/work/cglab/projects/DORRY/DORRY_ALL/'
movedir = '/work/cglab/projects/DORRY/BIDS/RS/sourcedata/'

# loop through all dirs and subdirs of rootdir
for subdir, dirs, files in os.walk(rootdir):
    # str should be folder or folder combo you're looking for
    if subdir_find in subdir:
        src_files = os.listdir(subdir)
        # loop through each filename in root
        for file_name in src_files:
            full_file_name = os.path.join(subdir, file_name)
            #check that its a file not a subdir
            if os.path.isfile(full_file_name):
                subnum = os.path.split(full_file_name)
                # sub_movedir = os.path.join(movedir, subnum[0][-10:-6]+'/')
                sub_movedir = os.path.join(movedir, subnum[0].split('/')[6]+'/')
                # make directory if it doesn't exist
                if not os.path.exists(sub_movedir):
                    os.makedirs(sub_movedir)
                # copy if file does **not** already exists in new location
                if ~os.path.isfile(os.path.join(sub_movedir, file_name)):
                    shutil.copy(full_file_name, sub_movedir)