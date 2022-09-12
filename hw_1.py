import time
start = time.time()

# from unsorted import numbers
from sorted import numbers

to_find = [
  5378654,1096519,2575130,7912393,8847484,1391621,9669847,2030367,
  2092897,8173176,4044334,8784312,7199523,3190798,3866636,5267739,
  9129410,7259936,8794047,9995645,1711458,5108271,4725368,5774026,
  5473012,8171462,5506896,3067434,4342111,9756710,5734943,3328182,
  8715714,4567529,5386518,8999073, 832952,8824648, 667046, 502084,
  2740509,1076401,4921322, 993662,3281009,9404866,9163322,7445817,
  4822940,2305758,5042564,9648271,7074265,5195662,6386087,1040530,
  9890093,5589876,6782305,4579948,9277859,1076959, 898569,6820658,
  6932561,4147591,5844909,9733787,7653226,1889274,4784433,5959323,
  6061374,6422378,4594699,9529062,5251684,4065461,6072650,    289
]

for num in to_find:
  found = False
  for i in range(0, len(numbers)):
    if numbers[i] == num:
      found = True
      print("%d at #%d" % (num, i))
      break
  if not found: print("%d Not found" % num)

print("time : ", time.time() - start)