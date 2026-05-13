name = input("What is compound name?")
molecular_weight= float(input(f"Molecular weight of {name}:"))
logP= float(input(f"What is {name} LogP:"))
hbd= float(input(f"How many H-bond donors does {name} have?:"))
hba = float(input(f"How many H-bond acceptors does {name} have?:"))

rule_mw = molecular_weight <= 500
rule_logp = logP <=5
rule_hbd = hbd <= 5
rule_hba = hba <= 10

print(f"{name} passes MW rule: {rule_mw}")
print(f"{name} passes logP rule: {rule_logp}")
print(f"{name} passes H-bond donor rule: {rule_hbd}")
print(f"{name} passes H-bond acceptor rule: {rule_hba}")

if rule_mw and rule_logp and rule_hba and rule_hbd:
    print(f"{name} passed Lipinski's rule of Five")
else:
    print(f"Oops!{name} does not pass Lipinski's rule of Five")



