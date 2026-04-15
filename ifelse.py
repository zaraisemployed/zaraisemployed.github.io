## 15-4-2026
price= int(input("what is the price of the bananas: "))
budget= int(input("what is your budget: "))
if(price > budget):
  print("you can buy the bananas")
elif(price<budget):
  print("you cannot buy the bananas")
else:
  print("you can buy one banana")
