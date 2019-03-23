# sandbox script to try out atom with python and plotting
# Written (and snippets barrowed) by Jeremy D. Rogers <jdrogers5@wisc.edu>
# To make atom more useful with python, install some community packages:
# hydrogen
# hydrogen-launcher
# atom-ide-ui
# ide-python
# platformio-ide-terminal (super useful to have cli that shares the environment, start with: jupyter console --existing )
# script
#
# most of this taken from various howtos and guides:
# https://realpython.com/python-matplotlib-guide/
# https://towardsdatascience.com/the-art-of-effective-visualization-of-multi-dimensional-data-6c7202990c57

#
# use hydrogen setting inline or docked as default (requires restart)

# %% first example from
# the double precent after the # makes this a cell for cell exexution using alt+shift+enter)
# line at a time exceution with shift enter
# note that plotting works best with cell execution, otherwise modfications to existing figure overwrite
#
import matplotlib.pyplot as plt
import numpy as np
np.random.seed(444)


fig, _ = plt.subplots()


rng = np.arange(50)
rnd = np.random.randint(0, 10, size=(3, rng.size))
yrs = 1950 + rng

fig, ax = plt.subplots(figsize=(5, 3))
ax.stackplot(yrs, rng + rnd, labels=['Eastasia', 'Eurasia', 'Oceania'])
ax.set_title('Combined debt growth over time')
ax.legend(loc='upper left')
ax.set_ylabel('Total debt')
ax.set_xlim(xmin=yrs[0], xmax=yrs[-1])
fig.tight_layout()
fig.show()
fig.savefig('test2.svg')


# %% second example

x = np.random.randint(low=1, high=11, size=50)
y = x + np.random.randint(1, 5, size=x.size)
data = np.column_stack((x, y))

fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(10, 6))

ax1.scatter(x=x, y=y, marker='o', c='r', edgecolor='b')
ax1.set_title('Scatter: $x$ versus $y$')
ax1.set_xlabel('$x$')
ax1.set_ylabel('$y$')

ax2.hist(data, bins=np.arange(data.min(), data.max()), label=('x', 'y'))
ax2.legend(loc=(0.65, 0.8))
ax2.set_title('Frequencies of $x$ and $y$')
ax2.yaxis.tick_right()



# %% third example using seaborn taken from screenshots in:
# https://jstaf.github.io/2018/03/25/atom-ide.html

# import pandas as pd
import seaborn as sns
tips = sns.load_dataset('tips')
sns.lmplot(data=tips, x='total_bill', y='tip', hue='sex')
