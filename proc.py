import glob
raws = glob.glob("*.fits")
x = []
y = []


from astropy.io import fits
import matplotlib.pyplot as plt
for raw in raws:
    print "Now processing", raw
    with fits.open(raw) as f:
        for point in f[1].data:
            x.append(point[0]-point[1])
            y.append(point[3]-point[5])

print "Now plotting"
plt.scatter(x,y)
plt.show()
