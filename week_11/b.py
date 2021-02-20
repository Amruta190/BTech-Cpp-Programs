import numpy as n
m1_5B9=n.array([[1,2,3],[4,5,6],[7,8,9]])
m2_5B9=n.array([[3,2,1],[6,5,4],[9,8,7]])
m3_5B9=m1_5B9+m2_5B9
print("Addition of matrices:")
print(m3_5B9)
m_5B9=m1_5B9.transpose()
print("Transpose of matrices:")
print(m_5B9)
m4_5B9=m1_5B9.dot(m2_5B9)
print("Multiplication of matrices:")
print(m4_5B9)