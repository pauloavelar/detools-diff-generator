import detools
import os

exclusions = ['.DS_Store', '.gitkeep']
files = [f for f in os.listdir('files') if f not in exclusions]

def get_filename(f):
  return os.path.splitext(f)[0]

def from_files(name):
  return f'files/{name}'

if len(files) < 2:
  print('Not enough files')
  exit

files.sort()

for i in range(0, len(files)):
  old = files[i]

  for j in range(i + 1, len(files)):
    new = files[j]

    diff = f'out/diff_{get_filename(old)}_{get_filename(new)}.ptm'

    print(f'Generating "{diff}"...')
    detools.create_patch_filenames(from_files(old), from_files(new), diff, compression='heatshrink')
