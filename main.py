
def count_batteries_by_health(present_capacities):
  rated_capacity=115
  c=0
  c1=0
  c2=0
  for i in present_capacities:
    soh=100*present_capacities(i)/rated_capacity
    if soh>=80 and soh<=100:
      c++
    if soh<80 and soh>=62:
      c1++
    if soh<62:
      c2++
  return {
    "healthy": c,
    "exchange": c1,
    "failed": c2
  }


def test_bucketing_by_health():
  print("Counting batteries by SoH...\n")
  present_capacities = [113, 116, 80, 95, 92, 70]
  counts = count_batteries_by_health(present_capacities)
  assert(counts["healthy"] == 2)
  assert(counts["exchange"] == 3)
  assert(counts["failed"] == 1)
  print("Done counting :)")


if __name__ == '__main__':
  test_bucketing_by_health()
