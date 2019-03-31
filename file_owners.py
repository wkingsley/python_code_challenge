# 5. File Owners
def group_by_owners(files):
  group = {}
  for key, value in files.items():
    if value in group:
      group[value].append(key)
    else:
      group[value]=[key]
    # group.update()
  return group

files = {
    'Input.txt': 'Randy',
    'Code.py': 'Stan',
    'Output.txt': 'Randy'
}
print(group_by_owners(files))