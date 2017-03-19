def dosomething(x):
    if x == 5:
        print('Fifth')
    else:
        print('Hell')

    if x == 7:
        print('Seventh')
    else:
        print('Heaven')


import dis
dis.dis(dosomething)

# How hard is to test (and understand) this function?
# https://en.wikipedia.org/wiki/Cyclomatic_complexity
complexity = 1
for i in dis.get_instructions(dosomething):
    complexity += int('JUMP_IF' in i.opname or 'FOR_ITER' == i.opname)

print(complexity)

# 7 is usually considered a threshold over which we should split the function
if complexity > 7:
    print('You should refactor!')
