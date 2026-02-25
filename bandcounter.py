#counter program

import numpy as np
from matplotlib.path import Path
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

#list of all voids
ra = np.array([12.2,23.183,18.6,10.467,8.667,11.2,3.833,17.65,6.083,13.416,18.083,16.833,2.433,8.967,9.367,23.8,4.916,23.583,23.683,13.1,5.016,11.267,14.533,6.816,21.233,6.516,1.333,20.116,10.983,16.733,12.566,0.616,20,6.25,9.567,12.067,12.333,15.467,3.416,4.233,11.4,21.55,7.367,14.067,0.4,12.8,10.983,10.616,8.25,14.583,3.283,0.45,20.067,15.6,20.55,6.033,23.116,11.016,14.816,10.183,9.816,1.167,14.4,15.75,9.583,14.567,8.75,15.55,22.8,11.667,9.283,7.867,10.833,12.433,6.55,0.867,8.183,22.683,15.633,13.333,0.533,14.333,2.35,17.433,9.85,15.45,5.66,3.6,14.85,11.433,19.2,12.85,1.467,9.167,11.7,5.716,11.083,12.15,10.4,5.667])
dec = np.array([-39,-12.4,30.4,25.3,31.2,-21.1,6.2,-55.6,-6.2,69.6,-16.2,38.3,-15,45.4,-77.9,16.6,-2.8,-12.6,-28.3,22.1,-9.1,37.3,-48.3,-40.7,76.3,-26.9,-47.9,29.2,2.8,15.1,-40.5,-19.9,-64.2,68.5,-6,40.6,-6.6,13.9,-62,-20.7,12.8,-11.2,-51.4,15,-33.9,12.9,19.6,-15.4,21.3,7.3,14.1,42,-29.3,29.9,-8.5,-32.4,-48.9,-29.4,3.3,30,-10.1,-6.1,-7.9,-70.4,17.3,-14.8,-7.1,-10.6,37.2,48.3,59.8,38.7,1.8,-79.8,-21.5,43.9,50,8.6,-12.2,-11,-12.3,-24.5,-33.5,-10.9,-24.3,-28.6,44,53.8,39.4,12,-38,20.9,-9.2,10.4,64.7,-54.2,38.1,-10,59.2,-40.4])

points = np.column_stack((ra, dec))


#boundaries of band
vertices = np.array([
    [17, -75],
    #[9, -75], #og
    [21, -75],
    #[13, -75], #og
    [13, 40],
    #[5, 40], #og
    [10, 40]
    #[2, 40] #og
])

#making shape
polygon = Path(vertices)

#test
inside = polygon.contains_points(points)


count = np.sum(inside)

print("Number inside:", count)
print("That BETTER be close to zero if you're running the og coords brochacho")



#plot
fig, ax = plt.subplots(figsize=(8, 6))

#outside
ax.scatter(ra[~inside], dec[~inside], s=10, alpha=0.4)

#inside
ax.scatter(ra[inside], dec[inside], s=20)

#outline
poly = Polygon(vertices, closed=True, fill=False, linewidth=2)
ax.add_patch(poly)

ax.set_xlabel("RA (hours)")
ax.set_ylabel("Dec (deg)")
ax.set_title("Figure 7\nParallelogram Region Check")


plt.show()
