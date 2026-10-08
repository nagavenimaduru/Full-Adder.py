def full_adder(a, b, carry_in):
    sum_bit = a ^ b ^ carry_in
    carry_out = (a & b) | (carry_in & (a ^ b))

    return sum_bit, carry_out


print("Full Adder")
print("----------")

a = int(input("Enter A (0 or 1): "))
b = int(input("Enter B (0 or 1): "))
carry_in = int(input("Enter Carry-In (0 or 1): "))

if a in [0, 1] and b in [0, 1] and carry_in in [0, 1]:

    sum_bit, carry_out = full_adder(a, b, carry_in)

    print("\nResults:")
    print(f"A        = {a}")
    print(f"B        = {b}")
    print(f"Carry-In = {carry_in}")
    print(f"Sum      = {sum_bit}")
    print(f"Carry-Out = {carry_out}")

else:
    print("Invalid input! Please enter only 0 or 1.")
