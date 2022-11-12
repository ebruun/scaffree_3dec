import itasca as it
import json

it.command("python-reset-state false")

it.command("""
model restore 'Final_State'
""")

Unbalanced_Force_Block_Dictonary = {}
print (Unbalanced_Force_Block_Dictonary)

# Empty dictionary
data_dict = {}
data_dict["model_overall"] = {}
data_dict["model_blocks"] = {}
volume_sum = 0.0

for i,b in enumerate(it.block.list()):
    volume_sum += b.vol()

    data_dict["model_blocks"][b.index()] = {
        "position":[b.pos()[0],b.pos()[1],b.pos()[2]],
        "vol":b.vol(),
        "velocity":[b.velocity()[0],b.velocity()[1],b.velocity()[2]],
        "f_unbalance":[b.force_unbal()[0],b.force_unbal()[1],b.force_unbal()[2]]
    }

data_dict["model_overall"]["total_blocks"] = it.block.count()
data_dict["model_overall"]["total_volume"] = volume_sum

print(data_dict)

f_path = '../../3dec_output/output_data.json'

with open(f_path, "w") as write_file:
    json.dump(data_dict, write_file, indent=2)
   