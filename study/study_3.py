from fractions import Fraction as f
from decimal import Decimal, getcontext


cycle_length = 0
biggest_d = 0
for d in range(2, 1000):
    current_length = 0
    x = 1/d
    cycle = [str(x)[j] for j in range(2, len(str(x)))]
    recurring = [cycle[0]]
    for i in range(1, len(cycle) + 1):
        if len(cycle) > 1:
            if cycle[i] == recurring[0]:
                current_length = len(recurring)
                break
            elif cycle[i] == recurring[-1]:
                if i == len(cycle) - 1:
                    current_length = 0
                    break
                elif cycle[i] == cycle[i+1]:
                    recurring = [cycle[i]]
                    current_length = len(recurring)
                    break
                elif cycle[i] != cycle[i+1]:
                    recurring.append(cycle[i])
            elif cycle[i] != recurring[-1]:
                if cycle[i] == recurring[0]:
                    current_length = len(recurring)
                    break
                elif i == len(cycle) - 1:
                    current_length = 0
                    break
                elif cycle[i] != recurring[0]:
                    flag = True
                    for k in range(1, i-1):
                        if cycle[i] == cycle[k]:
                            if cycle[i+1] == cycle[k+1]:
                                recurring = [_ for _ in cycle[k:i]]
                                current_length = len(recurring)
                                flag = False
                                break
                    if flag:
                        recurring.append(cycle[i])
                    else:
                        break
        else:
            current_length = 0
    if current_length > cycle_length:
        cycle_length = current_length
        biggest_d = d

print(cycle_length)
print(biggest_d)









