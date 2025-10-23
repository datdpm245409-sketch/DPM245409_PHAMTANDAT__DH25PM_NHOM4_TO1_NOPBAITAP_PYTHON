# -------- Câu 9 --------
print("\n===== CHƯƠNG 6 - CÂU 9 =====")
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

M = [3,6,7,8,11,17,2,90,2,5,4,5,8]
le = [x for x in M if x % 2 != 0]
chan = [x for x in M if x % 2 == 0]
nt = [x for x in M if is_prime(x)]
knt = [x for x in M if not is_prime(x)]

print("Số lẻ:", le, "=>", len(le))
print("Số chẵn:", chan, "=>", len(chan))
print("Số nguyên tố:", nt)
print("Không nguyên tố:", knt)