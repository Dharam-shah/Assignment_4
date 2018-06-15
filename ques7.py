s = 'ISSISSIPPI'
l = list(s)
#coverting string into list
m_count = l.count('M')
i_count = l.count('I')
s_count = l.count('S')
p_count = l.count('P')

#creating final dictionary
dict = {'M':m_count,'I':i_count,'S':s_count,'P':p_count}
print("The created dictionary is",dict)
