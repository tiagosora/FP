
print("Kryptonite phase classifier")

T = float(input("Temperature (K)? "))
P = float(input("Pressure (kPa)? "))

phase = "SOLID"

if T > 400.0 and P > 50:
	phase = "LIQUID"
elif P < 0.125*T:
	phase = "GAS"

print("At {:.1f} K and {:.3f} kPa, Kryptonite is in the {} phase.".format(T, P, phase))

