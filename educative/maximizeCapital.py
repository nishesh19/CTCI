from heapq import heappush,heappop
class Capital:
  def __init__(self,index,value):
    self.index = index
    self.value = value
  
  def __lt__(self,other):
    return self.value < other.value

def find_maximum_capital(capital, profits, numberOfProjects, initialCapital):
  # TODO: Write your code here
  min_capital = []
  max_profit = []
  curr_capital = initialCapital
  
  for i in range(len(capital)):
    heappush(min_capital,Capital(i,capital[i]))

  while (numberOfProjects > 0):
    while (min_capital) and curr_capital >= min_capital[0].value:
      heappush(max_profit,-profits[heappop(min_capital).index])
    
    curr_capital += -heappop(max_profit)
    numberOfProjects -= 1
    
  return curr_capital


def main():

  print("Maximum capital: " +
        str(find_maximum_capital([0, 1, 2], [1, 2, 3], 2, 1)))
  print("Maximum capital: " +
        str(find_maximum_capital([0, 1, 2, 3], [1, 2, 3, 5], 3, 0)))


main()
