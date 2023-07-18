def selective_repeat_arq(n, m, Sf, Sn, E1, E2, E3):
    ws = (2 ** m) - 1
    for _ in range(n):
        if E1 == 1:  # Timeout event
            Sn = Sf
        elif E2 > 0:  # Frames from Upper layer event
            nfr = min(E2, ws - (Sn - Sf))
            Sn += nfr
            E2 -= nfr
        elif E3 != 0:  # ACK or NAK from bottom layer event
            if E3 > 0:  # Positive ACK
                Sf = E3
            else:  # Negative ACK (NAK)
                Sf = -E3
    print("Sf:", Sf, " Sn:", Sn)

n = int(input("Enter number of test cases:"))
inputs = []
for i in range(n):
    inputs.append([n])
    inputs[i].extend(list(map(int, input().split())))
print(inputs)

for test_case in inputs:
    selective_repeat_arq(*test_case)
