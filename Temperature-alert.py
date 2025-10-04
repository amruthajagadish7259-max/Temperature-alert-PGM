# temperature_alert.py

temp_c = float(input("Enter temperature in °C: "))

if temp_c < 20:
    status = "Cold"
elif 20 <= temp_c <= 30:
    status = "Normal"
else:
    status = "Hot"

temp_f = (temp_c * 9/5) + 32

print(f"Temperature: {temp_c}°C")
print(f"Status: {status}")
print(f"Temperature in Fahrenheit: {temp_f}°F")