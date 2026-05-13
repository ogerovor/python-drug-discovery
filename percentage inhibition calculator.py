pos_ctrl= float(input("What is the reference for 100% inhibition?"))
neg_ctrl= float(input("What is the reference for 0% inhibition?"))
sample= float(input("What is the absorbance of the sample?"))
pct_inh = ((pos_ctrl-sample)/(pos_ctrl-neg_ctrl))* 100
print(f"Percentage inhibition of sample: {round(pct_inh, 1)}% inhibition")
