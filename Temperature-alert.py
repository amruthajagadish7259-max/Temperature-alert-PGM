# temperature_alert.py

temp_c = float(input("Enter temperature in °C: "))

if temp_c < 20:
    status = "Cold"
elif 20 <= temp_c <= 30:
    status = "Normal"
else:
    status = "Hot"

print(f"Temperature: {temp_c}°C")
print(f"Status: {status}")