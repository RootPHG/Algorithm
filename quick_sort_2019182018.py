

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

def insertionSort(start, end):
    for i in range(start + 1, end + 1)
        v = array[i] # i위치의 v 값이 주인공
        j = i - 1 # v 와 비교를 시작할 위치
        while start <= j and j?? > v:
            array[??] = array[??] # 오른쪽으로 밀어준다
            j -= 1

        (j + 1) = 

def quickSort(start, end): #end = inclusive
    if ???: return # 재귀호출의 종료조건
    if ?????: # size of this array <= 10
        insertionSort(start, end)
    pi = partition(start, end)
    quickSort(start, pi - 1)
    quickSort(pi + 1, end)

from random import randint

def partition(start, end): #end = inclusive
    ri = randint(start, end)
    array[start], array[ri] = array[start]
    pv = array[start]

    p, q = start, end + 1
    while True:
        #find p
        while True:
            p += 1
            if p > end or array[p] > pv: break

        while True:
            q -= 1
            if ?? or ???: break

        if p >= q: #더이상 바꿀게 없다

        # swap @p and @q
        ????

    # swap @start and @q
    return q


array = words
quickSort(0, len(array) - 1)
print(array)

