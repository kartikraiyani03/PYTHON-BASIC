for i in range(1,21):
    # with open(f"tableof{i}.txt",'w') as f:
    f = open(f"tableof{i}.txt",'w')
    for j in range(1,11):
           f.write(f"{i} x {j} = {i*j}\n")
    