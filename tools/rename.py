

import os

dirs = os.listdir(os.getcwd())

for i in dirs:
    if i.startswith('meituanlist_'):
        i_new = i.replace('meituanlist_', 'meituanlist_sh_')
        print i_new
        os.rename(i, i_new)
