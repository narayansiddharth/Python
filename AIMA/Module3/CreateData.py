import pandas as pd  # this is how I usually import pandas
import sys  # only needed to determine Python version number
import matplotlib  # only needed to determine Matplotlib version number
import sys  # only needed to determine Python version number

import matplotlib  # only needed to determine Matplotlib version number
import pandas as pd  # this is how I usually import pandas

print('Python version ' + sys.version)
print('Pandas version ' + pd.__version__)
print('Matplotlib version ' + matplotlib.__version__)
# Create Data
names = ['Bob', 'Jessica', 'Mary', 'John', 'Mel']
births = [968, 155, 77, 578, 973]
print(names)
print(births)
zz = zip(names, births)
# print(list(zip(names,births)))
print(list(zz))
