import os
import shutil


rootdirs = [
    '/work/cglab/projects/DORRY/W2_miss/1022/3D/MR/'
]
movedir = '/work/cglab/projects/DORRY/BIDS/RS_W2/sourcedata/'
# no 3D folder in W2_miss   '/work/cglab/projects/DORRY/W2_miss/1033/3D/MR/',


for subdir in rootdirs:
    subnum = subdir.split('/')[6]
    src_files = os.listdir(subdir)
    print('Transferring files for {}...'.format(subdir))
    # loop through each filename in root
    for i, file_name in enumerate(src_files):
        full_file_name = os.path.join(subdir, file_name)
        sub_movedir = os.path.join(movedir, subnum + '/')        
        # copy if file does **not** already exists in new location
        if ~os.path.isfile(os.path.join(sub_movedir, file_name)):
            if i == 0:
                print('Copying and Moving file...\n {0}'.format(os.path.join(sub_movedir, file_name)))
            shutil.copy(full_file_name, sub_movedir)
