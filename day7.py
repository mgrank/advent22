class File:
  def __init__(self, name, topDir=None, size=-1):
    self.name = name
    self.contents = []
    self.size = size
    self.topDir = topDir
    self.dir = True if size==-1 else False

  def isDir(self):
    return self.dir

  def findFileByName(self, name):
    for i in self.contents:
      if i.name == name:
        return i
    return None

  def addFileIfNotExists(self, name, fsize=-1):
    newFile = currentDir.findFileByName(name)
    if not newFile:
      newFile = File(name, topDir=currentDir, size=fsize)
      currentDir.contents.append(newFile)
    return newFile

  def getSize(self):
    if self.size != -1:
      return self.size

    size = 0
    for file in self.contents:
      if not file.isDir():
        size += file.size
      else:
        size += file.getSize()
    self.size = size
    return size

root = currentDir = File('/')


def printFileTree(fromDir, level=0):
  desc = 'dir' if fromDir.isDir() else 'file'
  print(f'{"  "*level}- {fromDir.name}  ({desc}, {fromDir.getSize()})')
  for file in fromDir.contents:
    printFileTree(file, level+1)

def commandCd(dir_name):
  global currentDir
  if dir_name == '..':
    currentDir = currentDir.topDir
  elif dir_name == '/':
    currentDir = root
  else:
    newDir = currentDir.addFileIfNotExists(dir_name)
    currentDir = newDir

def addListedFile(line):
  t, name = line.split()
  if t == 'dir':
    currentDir.addFileIfNotExists(name)
  else: #file
    fsize = int(t)
    currentDir.addFileIfNotExists(name, fsize)

with open('day7test.txt') as f:
  for line in f:
    line = line.strip()
    if line[0] == '$':
      command = line[2:4]
      if command == 'cd':
        arg = line[5:]
        commandCd(arg)
    else:
      addListedFile(line)

def getSmallDirs(start_dir):
  size = 0
  if start_dir.getSize() <= 100000:
    print(start_dir.name, start_dir.getSize())
    size += start_dir.getSize()

  for d in [f for f in start_dir.contents if f.isDir()]:
    size += getSmallDirs(d)

  return size


printFileTree(root)
print(getSmallDirs(root))

TOTAL_SPACE = 70000000
NEED_SPACE  = 30000000
free_space = TOTAL_SPACE - root.getSize()

min_dir_size = root.getSize()

def walkDirTree(dir, min_size):
  for d in [f for f in dir.contents if f.isDir()]:
    if free_space + d.getSize() >= NEED_SPACE:
      min_size = min(d.getSize(), min_size)
    walkDirTree(d, min_size)
  return min_size

print(walkDirTree(root, root.getSize()))
