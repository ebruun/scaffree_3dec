import itasca as it
import copy

it.command("python-reset-state false")

it.command("""
model restore 'Additional_State'
""")

it.block.count()

b = it.block.find(1)

#for i,b in enumerate(it.block.list()):
#    print("brick {}, volume: {:.2f}, unbal: {}, centroid: {}".format(i,b.vol(),b.force_unbal(), b.pos()))


#with open('output.txt', 'w') as f:
#    for i,b in enumerate(it.block.list()):
#        f.write(str(i) + " ")
#        f.write(str(b.vol()) + " ")
#        f.write(str(b.pos())+" ")
#        f.write(str(b.force_unbal()))
#        f.write("\n")
#        
#f.close()

#for i,b in enumerate(it.block.subcontact.list()):
#    print("brick {}, area: {:.2f}, Norm_force: {}, position: {}".format(i,b.area(),b.force_norm(), b.pos()))
    
with open('output.txt', 'w') as f:
    for i,b in enumerate(it.block.subcontact.list()):
        f.write(str(i) + " ")
        f.write(str(b.area()) + " ")
        f.write(str(b.pos())+" ")
        f.write(str(b.force_norm())+" ")
        f.write(str(b.contact()))
        f.write("\n")
f.close()


with open('outputContact.txt', 'w') as f:
    for i,b in enumerate(it.block.contact.list()):
        f.write(str(i) + " ")
        f.write(str(b.area()) + " ")
        f.write(str(b.pos())+" ")
        f.write(str(b.normal()))
        f.write("\n")
f.close()