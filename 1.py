f = open('26.txt')
S, N = map(int, f.readline().split())
a = [int(i) for i in f]
f.close()
a = sorted(a)
s = 0
k = 0
for i in range(len(a)):
    s += a[i]
    k += 1
    if s == 8176:
        break
print(s, k)
