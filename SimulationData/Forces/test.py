import itasca as it
import copy

it.command("python-reset-state false")

it.command("""
model restore '02_State'
""")

it.block.count()

b = it.block.find(1)

for i,b in enumerate(it.block.list()):
    print("brick {}, volume: {:.2f}, unbal: {}, centroid: {}".format(i,b.vol(),b.force_unbal(), b.pos()))


with open('output.txt', 'w') as f:
    for i,b in enumerate(it.block.list()):
        f.write(str(i) + " ")
        f.write(str(b.vol()))
        f.write("\n")
        
f.close()