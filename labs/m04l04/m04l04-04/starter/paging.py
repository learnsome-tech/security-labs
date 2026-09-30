rows=200000
def page(requested, cap=None):
    size=requested if cap is None else min(requested, cap)
    return min(rows, size)
print('one row:', page(1))
print('million rows, no cap:', page(1000000))
print('million rows, capped:', page(1000000, cap=100))
print('page size is an input with a bound:', True)
