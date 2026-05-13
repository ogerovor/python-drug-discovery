weight_kg= float(input("What is patient's weight in Kilogram?"))
height_m = float(input("What is patient's weight in metres?"))
cl_standard = float(input("What is the standard drug clearance rate(L/hr)?"))
ref_weight = float(input("What is the reference body weight in Kilogram?"))
BMI= weight_kg/(height_m**2)
cl_patient = cl_standard*(weight_kg/ref_weight)**0.75
print(f"BMI:{round(BMI,1)}kg/m2")
print(f"Drug clearance: {round(cl_patient, 2)}L/hr")
