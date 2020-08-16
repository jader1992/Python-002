import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb

dates = pd.date_range('20200101', periods=12)
df = pd.DataFrame(np.random.randn(12,4), index=dates, columns=list('ABCD'))

# plt.plot(df.index, df['A'],)
# plt.show()
#
# plt.scatter(df.index,df['A'])
# plt.show()

sb.set_style('darkgrid')
plt.scatter(df.index, df['A'])
plt.show()