t = 41777096
d = 249136211271011

# distance traveled is (t - x) * x
# want this to be bigger than d => x^2 - tx + d < 0

using Polynomials
using Formatting
p = Polynomial([d, -t, 1])
r = roots(p)
println(r)

# valid range [a, b]
a = ceil(r[1])
b = floor(r[2])
len = b - a + 1

println(format(len))

