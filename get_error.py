real_value = float(input("enter real value(이론값): ")) #참값
test_value = float(input("enter test value: ")) #실험값

err = abs(real_value - test_value) / real_value

print(f"err = {err}")
