def go_back_n_arq(n, m, Sf, Sn, E1, E2, E3):
    ws = (2 ** m) - 1
    for _ in range(n):
        if E1 == 1:  # Timeout event
            Sf = Sn
        elif E2 > 0:  # Frames from Upper layer event
            nfr = min(E2, ws - (Sn - Sf))
            Sn += nfr
            E2 -= nfr
        elif E3 > 0:  # ACK from bottom layer event
            Sf = E3
    print("Sf:", Sf, " Sn:", Sn)

n = int(input("Enter number of test cases:"))
inputs = []
for i in range(n):
    inputs.append([n])
    inputs[i].extend(list(map(int, input().split())))
print()

for tc in inputs:
    go_back_n_arq(*tc)
