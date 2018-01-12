pd.get_dummies()，则恰将 string 转换为 integers 类型：

>> pd.get_dummies(['A', 'B', 'A'])
   A  B
0  1  0
1  0  1
2 1 0
