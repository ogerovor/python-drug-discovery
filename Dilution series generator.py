stock_conc= float(input("What is the concentration of stock?"))
dilution_factor = float(input("What is the dilution factor?"))
conc_1 = stock_conc
conc_2 = conc_1/dilution_factor
conc_3 = conc_2/dilution_factor
conc_4 = conc_3/dilution_factor
conc_5 = conc_4/dilution_factor
conc_6 = conc_5/dilution_factor
print(f"Concentration 1: {round(conc_1, 2)} nM")
print(f"Concentration 2: {round(conc_2, 2)} nM")
print(f"Concentration 3: {round(conc_3, 2)} nM")
print(f"Concentration 4: {round(conc_4, 2)} nM")
print(f"Concentration 5: {round(conc_5, 2)} nM")
print(f"Concentration 6: {round(conc_6, 2)} nM")
