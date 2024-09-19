#!/usr/bin/env python
# coding: utf-8

# In[46]:


import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import lfilter

# def weeklytotal(trading_volume,n):
#     sum=0;
#     j=1;
#     weektotal=np.array([])
#     for i in range (0,n):
#         sum+=trading_volume[i];
#         if (i)%7 == 0:
#             weektotal[j]=sum
#             sum=0
#             j=j+1
#     print(weektotal)
            
trading_volume = np.random.rand(126)
week=np.arange(0,126)
print(trading_volume)
# weeklytotal(trading_volume,126)
plt.plot(week,trading_volume)
plt.show()
# smooth_volume=lfilter(trading_volume)
# print(smooth_volume)


# In[ ]:




