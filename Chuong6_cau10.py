# -------- Câu 10 --------
print("\n===== CHƯƠNG 6 - CÂU 10 =====")
import numpy as np
def nhap_matrix(name):
    m = int(input(f"Nhập số dòng ma trận {name}: "))
    n = int(input(f"Nhập số cột ma trận {name}: "))
    M = []
    for i in range(m):
        row = list(map(int, input(f"Nhập dòng {i+1}: ").split()))
        M.append(row)
    return np.array(M)

def hoan_vi(M):
    return M.T

A = nhap_matrix("A")
B = nhap_matrix("B")
print("Ma trận A:\n", A)
print("Ma trận B:\n", B)
print("A + B =\n", A + B)
print("Hoán vị A:\n", hoan_vi(A))
print("Hoán vị B:\n", hoan_vi(B))