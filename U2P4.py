c = [1, 6, 11, 6]

r3 = [c[0] , c[2]]

r2 = [c[1], c[3]]
val = (r2[0]*r3[1]) - (r2[1]*r3[0])
val /= r2[0]
r1 = [val, 0]
r0 = [c[3]]

first_col = [r3[0], r2[0], r1[0], r0[0]]
print(f"First column of R = {first_col}")
flag = False
for i in first_col:
    if i < 0:
        flag = True
        break
print("UNSTABLE" if flag else "STABLE")