def gen_parzyste(n):
    for i in range(n):
        if i % 2 == 0:
            yield i
            
            
gen = gen_parzyste(100)

print(next(gen))  # 0
print(next(gen))
print(next(gen))