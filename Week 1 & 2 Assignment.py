#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1


# In[33]:


list_1 = [16, 55 , 3, 87] # create a list


# In[34]:


i = 0 #iterate over list
while i <(len(list_1)):
    print(list_1[i])
    i += 1


# In[35]:


list_1.sort(reverse=True) # Sort list
list_1


# In[36]:


import random

list_2 = [random.randint(0, 100) for x in range (0, 5)] #random list
list_3 = list_1 + list_2 # add to prior list
print(list_3)


# In[37]:


#2


# In[70]:


import matplotlib.pyplot as plt
import pandas as pd
#import xlrd

url = 'http://content.bellevue.edu/cst/dsc/540/id/data-files/12-week/weeks-1-&-2/world-population.xlsm'

wp = pd.read_excel(url)

x = wp['Year']
y = wp['Population']

plt.plot(x, y)
plt.xlabel('Year')
plt.ylabel('Pop. in Billions')
plt.title('World Population')
plt.show()


# In[84]:


#3


# In[ ]:


#Actvity 1


# In[73]:


import random #creating random list

limit = 100

random_list = [random.randint(0, limit) for x in range (0, limit)]

random_list


# In[74]:


list_div_3 = [a for a in random_list if a % 3==0] #random list divide by 3
list_div_3


# In[75]:


len_random_list = len(random_list) #differnece between the two list
len_list_div_3 = len(list_div_3)
diff = len_random_list - len_list_div_3
diff


# In[79]:


loop = 3
diff_list = []
for i in range(0, loop):
    random_list = [random.randint(0, limit) for x in range(0, limit)]
    list_div_3 = [a for a in random_list if a % 3==0]
    
    len_random_list = len(random_list)
    len_list_div_3 = len(list_div_3)
    diff = len_random_list - len_list_div_3
    
    diff_list.append(diff)

diff_list


# In[82]:


diff_mean = sum(diff_list) / float(len(diff_list))
diff_mean


# In[85]:


#Actvity 2


# In[88]:


multiline_text = """It is a truth universally acknowledged, that a single man in possession of a good fortune, must be in want of a wife.

However little known the feelings or views of such a man may be on his first entering a neighbourhood, this truth is so well fixed in the minds of the surrounding families, that he is considered the rightful property of some one or other of their daughters.

"My dear Mr. Bennet," said his lady to him one day, "have you heard that Netherfield Park is let at last?"

Mr. Bennet replied that he had not.

"But it is," returned she; "for Mrs. Long has just been here, and she told me all about it."

Mr. Bennet made no answer.

"Do you not want to know who has taken it?" cried his wife impatiently.

"You want to tell me, and I have no objection to hearing it."

This was invitation enough.

"Why, my dear, you must know, Mrs. Long says that Netherfield is taken by a young man of large fortune from the north of England; that he came down on Monday in a chaise and four to see the place, and was so much delighted with it, that he agreed with Mr. Morris immediately; that he is to take possession before Michaelmas, and some of his servants are to be in the house by the end of next week."

"What is his name?"

"Bingley."

"Is he married or single?"

"Oh! Single, my dear, to be sure! A single man of large fortune; four or five thousand a year. What a fine thing for our girls!"

"How so? How can it affect them?"

"My dear Mr. Bennet," replied his wife, "how can you be so tiresome! You must know that I am thinking of his marrying one of them."

"Is that his design in settling here?"

"Design! Nonsense, how can you talk so! But it is very likely that he may fall in love with one of them, and therefore you must visit him as soon as he comes."

"I see no occasion for that. You and the girls may go, or you may send them by themselves, which perhaps will be still better, for as you are as handsome as any of them, Mr. Bingley may like you the best of the party."

"My dear, you flatter me. I certainly have had my share of beauty, but I do not pretend to be anything extraordinary now. When a woman has five grown-up daughters, she ought to give over thinking of her own beauty."

"In such cases, a woman has not often much beauty to think of."

"But, my dear, you must indeed go and see Mr. Bingley when he comes into the neighbourhood."

"It is more than I engage for, I assure you."

"But consider your daughters. Only think what an establishment it would be for one of them. Sir William and Lady Lucas are determined to go, merely on that account, for in general, you know, they visit no newcomers. Indeed you must go, for it will be impossible for us to visit him if you do not."

"You are over-scrupulous, surely. I dare say Mr. Bingley will be very glad to see you; and I will send a few lines by you to assure him of my hearty consent to his marrying whichever he chooses of the girls; though I must throw in a good word for my little Lizzy."

"I desire you will do no such thing. Lizzy is not a bit better than the others; and I am sure she is not half so handsome as Jane, nor half so good-humoured as Lydia. But you are always giving her the preference."

"They have none of them much to recommend them," replied he; "they are all silly and ignorant like other girls; but Lizzy has something more of quickness than her sisters."

"Mr. Bennet, how can you abuse your own children in such a way? You take delight in vexing me. You have no compassion for my poor nerves."

"You mistake me, my dear. I have a high respect for your nerves. They are my old friends. I have heard you mention them with consideration these last twenty years at least."

"Ah, you do not know what I suffer."

"But I hope you will get over it, and live to see many young men of four thousand a year come into the neighbourhood."

"It will be no use to us, if twenty such should come, since you will not visit them."

"Depend upon it, my dear, that when there are twenty, I will visit them all."

Mr. Bennet was so odd a mixture of quick parts, sarcastic humour, reserve, and caprice, that the experience of three-and-twenty years had been insufficient to make his wife understand his character. Her mind was less difficult to develop. She was a woman of mean understanding, little information, and uncertain temper. When she was discontented, she fancied herself nervous. The business of her life was to get her daughters married; its solace was visiting and news. """


# In[90]:


print(type(multiline_text))
len(multiline_text)


# In[93]:


multiline_text = multiline_text.replace('\n', "") #remove space in between lines
multiline_text


# In[95]:


new_mlt = "" #remove symbol and punct
for char in multiline_text:
    if char == " ":
        new_mlt += char
    elif char.isalnum():
        new_mlt += char
    else:
        new_mlt += " "
new_mlt


# In[96]:


list_words = new_mlt.split() #see all individual words
list_words


# In[98]:


u_words_l = list(set(list_words)) # the unique words
len(u_words)


# In[99]:


u_words_d = dict.fromkeys(list_words)
len(list(u_words_d.keys()))


# In[102]:


for word in list_words: #unique word counter
    if u_words_d[word] is None:
        u_words_d[word] = 1
    else:
        u_words_d[word] += 1
u_words_d


# In[103]:


top_word = sorted(u_words_d.items(), key=lambda key_val_tuple: key_val_tuple[1], reverse = True)
top_word[:25]


# In[104]:


# Activity 3


# In[105]:


from itertools import permutations, dropwhile


# In[107]:


get_ipython().run_line_magic('pinfo', 'permutations')


# In[108]:


get_ipython().run_line_magic('pinfo', 'dropwhile')


# In[109]:


permutations(range(3))


# In[110]:


for number_tuple in permutations(range(3)):
    print(number_tuple)
    assert isinstance(number_tuple, tuple)


# In[111]:


for number_tuple in permutations(range(3)):
    print(list(dropwhile(lambda x: x <= 0, number_tuple)))


# In[112]:


import math
def convert_to_number(number_stack):
    final_number = 0
    for i in range(0, len(number_stack)):
        final_number += (number_stack.pop() * (math.pow(10, i)))
    return final_number


# In[113]:


for number_tuple in permutations(range(3)):
    number_stack = list(dropwhile(lambda x: x <= 0, number_tuple))
    print(convert_to_number(number_stack))


# In[114]:


# Activity 4


# In[115]:


from itertools import zip_longest


# In[116]:


def dict_from_csv(header, line):
    zipped_line = zip_longest(header, line, fillvalue=None)
    ret_dict = {kv[0]: kv[1] for kv in zipped-line}
    return ret_dict


# In[119]:


# did not understand how to get the csv file properly from github to open.


# In[ ]:




