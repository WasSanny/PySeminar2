Arbuz = int(input("Enter arbuz: "))
VesMin = VesMax = int(input("Ves Arbuz: "))
for i in range (1, Arbuz):
  temp = int(input("Ves Arbuz: "))
  if temp > VesMax:
    VesMax=temp
  elif temp < VesMin:
    VesMin=temp
print(f"Для тещи {VesMin}, Для себя {VesMax}")