import math
N = 1000000000
PRECISION = 50

estimation = 0.0
for n in range(N + 1):
    estimation += (-1)**n / (2*n + 1)
estimation *= 4

truth = math.pi
actual_error = estimation - truth
alternating_error = 1 / (2*N + 3)
lagrange_error = 1 / (2*N + 2)

print(f"Estimation = {estimation:.{PRECISION}f}")
print(f"True Value = {truth:.{PRECISION}f}")
print(f"Act. Error = {actual_error:.{PRECISION}f}")
print(f"Alt. Error = {alternating_error:.{PRECISION}f}")
print(f"Lag. Error = {lagrange_error:.{PRECISION}f}")