import matplotlib.pyplot as plt
import pandas as pd

data = pd.DataFrame({"x" : [1,2,3,4,5,6,2,7],"y":[3,2,4,4,7,8,2,90]})

plot_me = data.plot(x='x', y='y', kind='line')

plt.show()
