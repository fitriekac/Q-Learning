
# coding: utf-8

# In[38]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# In[39]:


# read data txt untuk dijadikan sebagai list
data = np.genfromtxt("tabel.txt", dtype= float)


# In[40]:


data


# In[41]:


#inisiasi
gamma = 0.9
alpha = 1
epsilon_init = 1
iterasi= 100
reward= 0
eps = epsilon_init


# In[42]:


#untuk plot ke tabel

fig, ax = plt.subplots()

# hide axes

ax.axis('off')
ax.axis('tight')

df = pd.DataFrame(data, columns=list('ABCDEFGHIJKLMNO'))

ax.table(cellText=df.values, colLabels=df.columns, loc='center')
#fig.tight_layout()

plt.show()


# In[43]:


state = []
q_table = np.zeros((15,15,4))
for i in range (1,iterasi):
    state = [14,0]
    while ((state[0] != 0) or (state[1] != 14)):
        possible_aksi = []
        action = -1
        if (state[0] > 0):
            possible_aksi.append(0)
        if (state[1] < 14 ):
            possible_aksi.append(1)
        if (state[0] < 14):
            possible_aksi.append(2)
        if (state[1] > 0):
            possible_aksi.append(3)
            
        if np.random.uniform(0,0.5) < eps:
            action = np.random.choice(possible_aksi)
        else:
            temp = q_table[state[0]][state[1]]
            possible_q = []
            for i in range(len(temp)):
                if i in possible_aksi:
                    possible_q.append(temp[i])
            action = np.argmax(possible_q)
            
        nilai_lama = q_table[state[0]][state[1]][action]
        state_lama = np.copy(state)
        
        if (action ==0):
            state[0] = state[0]-1
        elif (action==1):
            state[1]= state[1] +1
        elif (action==2):
            state[0] = state[0]+1
        elif (action==3):
            state[1]= state[1]-1
            
        selanjutnya = np.max(q_table[state[0]][state[1]])
        reward_action = data[state[0]][state[1]]
        
        #update nilai q_table
        q_table[state_lama[0]][state_lama[1]][action] = (1 - alpha) * nilai_lama + alpha * (reward_action + gamma * selanjutnya)
    eps = epsilon_init * np.exp(-0.001*i)


# In[44]:


#untuk lihat hasil
state = [14,0]
print("Dari state: {},{}".format(state[0],state[1]))
reward = 0
while ((state[0] != 0) or (state[1] != 14)):
    aksi = np.argmax(q_table[state[0]][state[1]])
    old_value = q_table[state[0]][state[1]][action]

    if (aksi ==0):
        state[0] = state[0]-1
    elif (aksi==1):
        state[1]= state[1] +1
    elif (aksi==2):
        state[0] = state[0]+1
    elif (aksi==3):
        state[1]= state[1]-1
    
    print("Ke state: {},{}".format(state[0],state[1]))
    reward = reward + data[state[0]][state[1]]
print("Reward: {}".format(reward))
nilai = reward.T


# In[8]:




