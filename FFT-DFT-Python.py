import matplotlib.pyplot as plt
import math


def DFT_matrix(N):
    w0 = 2 * math.pi / N
    res = []
    for k in range(N):
        a_k = []
        for n in range(N):
            a_k.append(
                complex(
                    round(math.cos(-1 * k * w0 * n), 3),
                    round(math.sin(-1 * k * w0 * n), 3)
                )
            )

        res.append(a_k)

    return res


def DFT(x, N):
    matrix = DFT_matrix(N)
    res = [[0 + 0j] for i in range(N)]
    for i in range(N):
        for k in range(N):
            res_keeper = res[i][0] + matrix[i][k] * x[k][0]
            res[i][0] = round(res_keeper.real, 3) + round(res_keeper.imag, 3) * 1j
    return res


def FFT(x, N):
    if len(x) == 2:
        return DFT(x, N)

    x_even = x[::2]
    x_odd = x[1::2]

    a_k = FFT(x_even, N // 2)
    b_k = FFT(x_odd, N // 2)

    a_k_two_times = a_k * 2
    b_k_two_times = b_k * 2

    W = []
    for i in range(N):
        W.append([complex(
            round(math.cos(-1 * i * 2 * math.pi / N), 3),
            round(math.sin(-1 * i * 2 * math.pi / N), 3)
        )])

    res = []
    for k in range(N):
        res_keeper = a_k_two_times[k][0] + W[k][0] * b_k_two_times[k][0]
        res.append([round(res_keeper.real, 3) + round(res_keeper.imag, 3) * 1j])

    return res


print("<--------------------------------------------->")
print("      |--->   Sajjad Rahmani   <---|")

# x : list of x[n] values in a period (number of values most be a power of 2)
x = [2, -1, 3, -3, -4, 5, -6, 1]
# change x from list form to matrix form
x = [[i] for i in x]

# N : period
N = len(x)

print("<--------------------------------------------->")

if not ((N & (N - 1) == 0) and (N != 0)):
    print("Number of values most be a power of 2!")
    exit(0)

# <------------------------------------------------------------>

res_DFT = DFT(x, N)
print(f"Result using DFT (without applying 1/{N}) : \n")
for row in res_DFT:
    for i in row:
        print(i)

print("\n<--------------------------------------------->")

res_FFT = FFT(x, N)
print(f"Result using FFT (without applying 1/{N}) : \n")
for row in res_FFT:
    for i in row:
        print(i)
print("\n<--------------------------------------------->")

# calculate real & imaginary part
res_FFT_real = [i[0].real for i in res_FFT]
res_FFT_imag = [i[0].imag for i in res_FFT]

print("Real Part : ", res_FFT_real)
print("Imaginary Part : ", res_FFT_imag)

fig, ax = plt.subplots(2, 1, sharex=True)
ax[0].stem(res_FFT_real, use_line_collection=True, label='Real Part')
ax[1].stem(res_FFT_imag, use_line_collection=True, label='Imaginary Part')
for axx in ax:
    axx.legend()
plt.show()

print("<--------------------------------------------->")

# calculate magnitude and phase
res_FFT_magnitude = [math.sqrt((res_FFT_real[i] ** 2) + (res_FFT_imag[i] ** 2)) for i in range(N)]
res_FFT_phase = [math.atan(res_FFT_imag[i] / res_FFT_real[i]) for i in range(N)]

print("Magnitude : ", res_FFT_magnitude)
print("Phase : ", res_FFT_phase)

fig, ax = plt.subplots(2, 1, sharex=True)
ax[0].stem(res_FFT_magnitude, use_line_collection=True, label='Magnitude')
ax[1].stem(res_FFT_phase, use_line_collection=True, label='Phase')
for axx in ax:
    axx.legend()
plt.show()

print("<--------------------------------------------->")
