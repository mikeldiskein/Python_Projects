import math
import matplotlib
import numpy

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-5, 2, 100)                     # от -5 до 2 сделать 100 точек
y1 = x**3 + 5*x**2 + 10                         # y1 - тоже много точек
y2 = 3*x**2 + 10*x
y3 = 6*x + 10

fig, ax = plt.subplots()                        # будет 1 график, на нем:
ax.plot(x, y1, color="blue", label="y(x)")      # функция y1(x), синий, надпись y(x)
ax.plot(x, y2, color="red", label="y'(x)")      # функция y2(x), красный, надпись y'(x)
ax.plot(x, y3, color="green", label="y''(x)")   # функция y3(x), зеленый, надпись y''(x)
ax.set_xlabel("x")                              # подпись у горизонтальной оси х
ax.set_ylabel("y")                              # подпись у вертикальной оси y
ax.legend()                                     # показывать условные обозначения

plt.show()                                      # показать рисунок
fig.savefig('1.png')                            # сохранить в файл 1.png


# class TreeNode:
#     def __init__(self, value=1):
#         self.value = value
#         self.left = None
#         self.right = None
#
#
# tree = TreeNode()
# tree.right = TreeNode()
# tree.right.left = TreeNode()
# tree.right.right = TreeNode()
# tree.right.right.left = TreeNode()
# tree.right.right.right = TreeNode()
# tree.right.right.left.right = TreeNode()
# tree.right.right.left.right.right = TreeNode()
#
#
# def longestZigZag(root: TreeNode) -> int:
#     res = 0
#
#     def helper(root, direction):
#         nonlocal res
#         if not root:
#             return 0
#         left = helper(root.left, 'left')
#         right = helper(root.right, 'right')
#         res = max(res, left + 1, right + 1)
#         return right + 1 if direction == 'left' else left + 1
#
#     if not root:
#         return 0
#     helper(root, 'left')
#     helper(root, 'right')
#     return res - 1
#
#
# print(longestZigZag(tree))



