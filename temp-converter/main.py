fStr = input('temperatura en grados fahrenheit ')
f = int(fStr)

c = (f - 32) * 5/9

baseStr = '{} grados fahrenheit son {} grados celsius'

print(baseStr.format(f, c))
