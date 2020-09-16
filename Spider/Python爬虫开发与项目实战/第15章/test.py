from pybloom_live import BloomFilter, ScalableBloomFilter

f = BloomFilter(capacity=1000, error_rate=0.001)
print([f.add(x) for x in range(10)])
print(11 in f)
print(4 in f)


sbf = ScalableBloomFilter(mode=ScalableBloomFilter.SMALL_SET_GROWTH)
count = 10000
for i in range(0, count):
    sbf.add(i)
print(10001 in sbf)
print(4 in sbf)