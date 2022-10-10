



words = [
  'jingo', 'lf', 'log', 'non', 'lj', 'goo', 'hmg', 'joe', 'knell', 'minim',
  '2019182018', '박효근',
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
]

def mergeSort(start=0, end = None):
    if end == None: end = len(words) - 1
    if start >= end: return # 재귀호출의 종료조건
    mid = (start + end) // 2 # mid is included in left part
    mergeSort(start, mid) #왼쪽
    mergeSort(mid + 1, end)#오른쪽
    merge(start, mid, end)

def merge(start, mid, end): # mid is in left, end = inclusive in right
    # 공간복잡도 = O(n)
    merged = []
    l, r = start, mid + 1
    while l < mid + 1 and r <= end:
        if words[l] <= words[r]:
            merged += [ words[l] ]
            # merged.append(words[i])
            l += 1
        else:
            merged += [ words[r] ]
            r += 1
    if l <= mid: #왼쪽에 선수가 남아있다면
        merged += words[l:mid+1] # 어디에 +1 을 해야하는지
    elif r <= end: #오른쪽에 선수가 남아있다면
        merged += words[r:end+1]


    words[start:end+1] = merged #

print(words)
mergeSort()
print(words)

