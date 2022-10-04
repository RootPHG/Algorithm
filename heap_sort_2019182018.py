import unsorted
import time
from random import shuffle

words = [
  'mog', 'jim', 'km', 'lining', 'mingle', 'ell', 'folk', 'melon', 'ln', 'link', 
  'knife', 'fennel', 'loon', 'john', 'ff', 'felloe', 'liking', 'lino', 'om', 'keg', 
  'joke', 'no', 'hog', 'jell', 'fino', 'elfin', 'gin', 'lone', 'oh', 'gong', 
  'ogee', 'oi', 'jig', 'filling', 'g', 'ge', 'mn', 'femme', 'fen', 'kj', 
  'gene', 'online', 'mg', 'goggle', 'emf', 'loll', 'meek', 'l', 'gem', 'filing', 
  'infill', 'hello', 'ink', 'monk', 'kg', 'ghillie', 'elf', 'gm', 'leo', 'genie', 
  'hoe', 'he', 'eke', 'moll', 'gnomon', 'fm', 'lei', 'million', 'going', 'feminine', 
  'infilling', 'liege', 'mo', 'o', 'goon', 'hg', 'legging', 'holm', 'enjoin', 'e', 
  'mini', 'logging', 'kin', 'hen', 'logo', 'flee', 'inf', 'fog', 'knee', 'limn', 
  'jingo', 'lf', 'log', 'non', 'lj', 'goo', 'hmg', 'joe', 'knell', 'minim', 
  'menfolk', 'feel', 'mlle', 'ken', 'home', 'if', 'linen', 'ne', 'lo', 'knoll', 
  'mime', 'ooh', 'nomen', 'hill', 'kohl', 'efl', 'offline', 'lee', 'king', 'legion', 
  'one', 'hike', 'genome', 'neigh', 'lifelong', 'him', 'gigolo', 'fo', 'fe', 'ego', 
  'mom', 'hi', 'fine', 'ni', 'ongoing', 'ho', 'noh', 'jog', 'lion', 'loin', 
  'fill', 'm', 'nee', 'join', 'noggin', 'neon', 'none', 'hm', 'gi', 'hook', 
  'ion', 'in', 'gen', 'mono', 'feign', 'look', 'hinge', 'moonie', 'nil', 'ginkgo', 
  'kilo', 'fief', 'ikon', 'moon', 'long', 'hf', 'lifeline', 'lingo', 'mink', 'nigh', 
  'k', 'killing', 'hoi', 'mongol', 'nikkei', 'ime', 'hoof', 'me', 'floe', 'omen', 
  'jiff', 'mike', 'foe', 'ingoing', 'leg', 'kiln', 'fin', 'noel', 'niff', 'minion', 
  'gnome', 'ill', 'ogle', 'info', 'igloo', 'fife', 'milk', 'loo', 'en', 'high', 
  'onion', 'lemon', 'li', 'life', 'flog', 'jink', 'joggle', 'ofghijklmno', 'ofghijklmni', 'ofghijklmok'
]


def main(list):
  count = len(list)
  last_parent_index = count // 2 - 1
  for n in range(last_parent_index, -1, -1):
    heapify(list, n, count)

  last_sort_index = count - 1
  while last_sort_index > 0:
    list[0], list[last_sort_index] = list[last_sort_index], list[0]
    heapify(list, 0, last_sort_index)
    last_sort_index -= 1

  # vis.heapsort(list, 0, 0)

def heapify(arr, root, size):
  lc = root * 2 + 1
  if lc >= size: return
  child = lc
  rc = root * 2 + 2
  if rc < size:
    if arr[rc] > arr[lc]:
      child = rc

  if arr[root] < arr[child]:
    arr[root], arr[child] = arr[child], arr[root]
    heapify(arr, child, size)

if __name__ == '__main__':
  list = unsorted.numbers[:13]


  started = time.time()
  main(words)
  elapsed = time.time() - started
  print('Elapsed: %.4fs' % elapsed)
  print(words)


