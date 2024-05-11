def to_list(mdict):
    my_list=[]
    m_list=[]
    k=0
    for keys ,default in mdict.items():
        my_list.append(keys)
          
        my_list.append(default)
        m_list.append(my_list)
        
    
    return m_list
    
print(to_list({ "a": 1, "b": 2 })) 