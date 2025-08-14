import itertools
print(list(itertools.chain([1,2],[3,4])))      # nối các iterable: 1,2,3,4
print(list(itertools.compress('ABCDE', [1,0,1,0,1]))) # lọc theo mask: A C E
print(list(itertools.dropwhile(lambda x: x<3, [1,2,3,4])))  # bỏ đến khi x>=3: 3,4
itertools.takewhile(lambda x: x<3, [1,2,3,4])  # lấy đến khi x>=3: 1,2
itertools.filterfalse(lambda x: x%2, range(5))  # lọc ngược điều kiện: 0,2,4
itertools.islice(range(10), 2,8,2)