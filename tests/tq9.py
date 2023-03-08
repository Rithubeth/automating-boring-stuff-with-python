def series_sumofsquare(start,end):
 sum = 0
 for x in range(start,end+1):
  sum += x**2
 return sum
print(series_sumofsquare(1,5))
