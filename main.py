import time

n = 500000
target = 499999

my_list = list(range(n))
my_set = set(range(n))

start = time.perf_counter()
result_list = target in my_list
list_time = time.perf_counter() - start

start = time.perf_counter()
result_set = target in my_set
set_time = time.perf_counter() - start

print(f"List search: {list_time:.6f} сек")
print(f"Set search: {set_time:.6f} сек")

print(f"Множина швидша приблизно у {list_time / set_time:.2f} разів")