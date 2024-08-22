import os

rootdir = '/work/cglab/projects/DORRY/DORRY_ALL/'
movedir = '/work/cglab/projects/DORRY/BIDS/RS/sourcedata/'

# get all subject number directory names
sub_dirs = [name for name in os.listdir(rootdir) if os.path.isdir(os.path.join(rootdir, name))]
os.chdir(movedir)

for sub in sub_dirs:
    os.mkdir(os.path.join(movedir, sub))
    