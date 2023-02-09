# target = 200
# coins = [1, 2, 5, 10, 20, 50, 100, 200]
# ways = [1] + [0]*target
#
# for coin in coins:
#     for i in range(coin, target+1):
#         ways[i] += ways[i-coin]
#
# print("Ways to make change =", ways[target])


def change(sum, coins):
  if sum < 0:
    return 0
  if sum == 0:
    return 1
  possible_changes = 0
  for i in range(len(coins)):
    possible_changes += change(sum - coins[i], coins[i:])
  return possible_changes


print(change(200, [200, 100, 50, 20, 10, 5, 2, 1]))