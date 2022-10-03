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


def heapify(li, idx, n):
    l = idx * 2
    r = idx * 2 + 1
    s_idx = idx
    if (l <= n and li[s_idx] > li[l]):
        s_idx = 1
    if (r <= n and li[s_idx] > li[r]):
        s_idx = r
    if s_idx != idx:
        li[idx], li[s_idx] = li[s_idx], li[idx]
        return heapify(li, s_idx, n)

def heap_sort(v):
    n = len(v)
    v = [0]+v

    for i in range(n, 0, -1):
        heapify(v, i, n)

    for i in range(n, 0, -1):
        print(v[1])
        v[i], v[1] = v[1], v[i]
        heapify(v, 1, i-1)


heap_sort(words)

