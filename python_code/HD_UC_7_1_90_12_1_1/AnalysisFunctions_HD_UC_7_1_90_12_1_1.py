import itasca as it
import json
from re import split
import os
#from HD_UC_7_1_90_12_1_1 import name_supports, name_list
#from input_HD_UC_7_1_90_12_1_1 import c_support_names, c_stage_names, mech_properties, points #

print("\nSTART ANALYSIS")
#print(os.getcwd())
#print(c_support_names)

#######################################################

it.command("python-reset-state false")

it.command("""
    model new
    model large-strain on
    """)
    
########################################################

c_support_names = ['dome_herringbone_7_1_90_12_1_1_0_0.wrl']

c_stage_names = [
    'dome_herringbone_7_1_90_12_1_1_1_1.wrl',
    'dome_herringbone_7_1_90_12_1_1_2_24.wrl',
    'dome_herringbone_7_1_90_12_1_1_25_49.wrl',
    'dome_herringbone_7_1_90_12_1_1_50_74.wrl',
    'dome_herringbone_7_1_90_12_1_1_75_99.wrl',
    'dome_herringbone_7_1_90_12_1_1_100_124.wrl',
    'dome_herringbone_7_1_90_12_1_1_125_154.wrl',
    ]

mech_properties = {
    'block_prop_density': 2000, #[kg/m^3]
    
    'stif_norm1': 1.5e9, # stiffness-norm [Pa/m] 
    'stif_norm2': 1.0e9,
    'stif_norm_Broken1': 1.0e9,
    'stif_norm_Broken2' : 1.0e9,

    'stif_shear1': 1.5e8,  # stiffness-shear [Pa/m] 
    'stif_shear2': 1.0e8,
    'stif_shear_Broken1': 1.0e8,
    'stif_shear_Broken2': 1.0e8,

    'fric_angl1': 25,     # friction angle[grad]
    'fric_angl2': 25,
    'fric_angl_Broken1': 25,
    'fric_angl_Broken2': 20,

    'number_cycle': 40000,     # cycle

}


#point to check 
#notation C=corner Number=brick_course M=middle_sail Co=corner
# CNunM = [x,y,z]
points= [

    [-0.2597,-6.9409,3.3781], #C02M   #03
    [2.5476,-6.4911,3.3212], #C02Co   #09
    
    [2.3163,-5.9019,4.411], #C20M   #15
    [-0.1186,-6.3391,4.411], #C20Co   #21

    [-0.1027,-5.4934,5.4284],#C42M   #27
    [2.0073,-5.1145,5.4284], #C42Co   #33

    [-4.5502,-1.7858,5.9801], #C54M   #39
    [-4.0387,-2.7536,5.9801], #C54Co   #45

    [1.6206,-4.1291,6.3229], #C62M   #39
    [-0.0839,-4.4864,6.2864], #C62Co   #45

    [-3.1464,-1.4434,6.9044], #C81Co   #51
    [-3.1982,-1.3247,6.9044], #C81Co   #57

    [-0.0626,-3.3479,6.9601], #C82M   #51
    [1.2596,-3.041,6.9872], #C82Co   #57

    [0.7848,-1.8946,7.4464], #C101Co  #63
    [-0.0395,-2.1111,7.4294], #C101M  #69

    [-0.0245,-1.312,7.6114], #C119M  #71
    [0.5022,-1.2123,7.6114] #C119Co  #11

]


########################################################

def path_input(file_name, cwd_path):
    model = os.path.join(cwd_path, file_name)

def model_geometries(file_name, cwd_path):
    
    model = os.path.join(cwd_path, file_name)
    
    model_action = '''
    block hide on
    block generate from-vrml filename '{}'
    '''.format(model)
    it.command(model_action)

def coord_point(point):
    x_point = point[0] 
    y_point = point[1]
    z_point = point[2]
    cmd_text = '''
    block history velocity-x position {0} {1} {2}
    block history velocity-y position {0} {1} {2}
    block history velocity-z position {0} {1} {2}
    block history displacement-x position {0} {1} {2}
    block history displacement-y position {0} {1} {2}
    block history displacement-z position {0} {1} {2}
    '''.format(x_point, y_point, z_point)
    it.command(cmd_text) 

def split_string(string, delimiters):
    pattern = r'|'.join(delimiters)
    return split(pattern, string)

def names_c_construction(name):
    temp_name_block_group = split_string(name, ['dome_herringbone_7_1_90_12_1_1_','.wrl'])
    name_block_group = 'C' + temp_name_block_group[1]
    name_state = temp_name_block_group[1] + '_State'
    temp_name_list = [name_block_group, name_state]
    return(temp_name_list)

def group_block(g_name):
    g_name_action = '''
    block group '{}'
    block hide off
    '''.format(g_name)
    it.command(g_name_action)

def save_c_state(c_state_name):
    #!heck the path
    state_action = '''
    model save '../../3dec_output/HD_UC_7_1_90_12_1_1_Output/{}' inputdir 
    '''.format(c_state_name)
    it.command(state_action) 

def density_prop(den_value):
    density_action = '''
    block property density {}
    '''.format(den_value)
    it.command(density_action)


def mech_prop1(stif_n1,stif_s1,fric_a1,stif_n_Brok1,stif_s_Brok1,fric_a_Brok1):
    mech_prop_action = '''
    block contact generate-subcontacts
    block contact prop stiffness-norm={} stiffness-shear={} friction={} range group 'Free' not
    block contact material-table default prop stiffness-norm={} stiffness-shear={} friction={}
    '''.format(stif_n1,stif_s1,fric_a1,stif_n_Brok1,stif_s_Brok1,fric_a_Brok1)
    it.command(mech_prop_action)
    
def mech_prop2(stif_n2,stif_s2,fric_a2,stif_n_Brok2,stif_s_Brok2,fric_a_Brok2):
    mech_prop_action  = '''
    block contact generate-subcontacts
    block contact group 'Free'
    block contact prop stiffness-norm={} stiffness-shear={} friction={} range group 'Free'
    block contact material-table default prop stiffness-norm={} stiffness-shear={} friction={}
    '''.format(stif_n2,stif_s2,fric_a2,stif_n_Brok2,stif_s_Brok2,fric_a_Brok2)
    it.command(mech_prop_action)
    
def gravity():
    gravity_action = '''
    block mechanical damping global
    model gravity 0 0 -9.81
    '''
    it.command(gravity_action)
    
def cycle(cyc):
    cycle_action = '''
    model cycle  {}
    '''.format(cyc)
    it.command(cycle_action)
  
##########################################################
##########################################################

cwd_path = os.getcwd()
path_input('input_HD_UC_7_1_90_12_1_1', cwd_path)
block_prop_density = mech_properties['block_prop_density']

# stiffness-norm [Pa/m] 
stif_norm1 = mech_properties['stif_norm1']
stif_norm2 = mech_properties['stif_norm2']
stif_norm_Broken1 = mech_properties['stif_norm_Broken1']
stif_norm_Broken2 = mech_properties['stif_norm_Broken2']

# stiffness-shear [Pa/m] 
stif_shear1 = mech_properties['stif_shear1']
stif_shear2 = mech_properties['stif_shear2']
stif_shear_Broken1 = mech_properties['stif_shear_Broken1']
stif_shear_Broken2 = mech_properties['stif_shear_Broken2']

# friction angles[grad]
fric_angl1 = mech_properties['fric_angl1']
fric_angl2 = mech_properties['fric_angl2']
fric_angl_Broken1 = mech_properties['fric_angl_Broken1']
fric_angl_Broken2 = mech_properties['fric_angl_Broken2']

# cycle
number_cycle = mech_properties['number_cycle']
print(number_cycle)
##########################################################
##########################################################

model_geometries(c_support_names[0],cwd_path)

it.command("""
    block group 'fix'
    block fix range group 'fix'
    block hide off
    """)

it.command("""
    plot create 'HD_Under construction'
    plot item create block
    model history mechanical unbalanced-maximum ;1
    model history mechanical time-total ;2
    plot create 'Unbalanced Force'
    plot item create chart-history history '1' vs '2'
    plot 'Unbalanced Force' export bitmap filename 'Unbalanced Force'
    """)
    
for c_stage_name in c_stage_names:

    print("running...{}".format(c_stage_name))

    if c_stage_name == 'dome_herringbone_7_1_90_12_1_1_54_80.wrl':
        it.command("model restore '../../3dec_output/HD_UC_7_1_90_12_1_1_Output/27_53_E_State'") ##check the path
    elif c_stage_name == 'dome_herringbone_7_1_90_12_1_1_81_119.wrl':
        it.command("model restore '../../3dec_output/HD_UC_7_1_90_12_1_1_Output/54_80_E_State'")
    model_geometries(c_stage_name,cwd_path)
    if c_stage_name =='dome_herringbone_7_1_90_12_1_1_2_26.wrl':
        coord_point(points[0])
        coord_point(points[1])
        coord_point(points[2])
        coord_point(points[3])
    elif c_stage_name =='dome_herringbone_7_1_90_12_1_1_27_53.wrl':
        coord_point(points[4])
        coord_point(points[5])         
    elif c_stage_name =='dome_herringbone_7_1_90_12_1_1_54_54_0.wrl':
        coord_point(points[6])
        coord_point(points[7])
    elif c_stage_name =='dome_herringbone_7_1_90_12_1_1_54_80.wrl':
        coord_point(points[8])
        coord_point(points[9])      
    elif c_stage_name =='dome_herringbone_7_1_90_12_1_1_81_81_0.wrl':
        coord_point(points[10])
        coord_point(points[11]) 
    elif c_stage_name =='dome_herringbone_7_1_90_12_1_1_81_119.wrl':
        coord_point(points[12])
        coord_point(points[13]) 
        coord_point(points[14])
        coord_point(points[15])
        coord_point(points[16])
        coord_point(points[17])  
 
    name_c_stages = names_c_construction(c_stage_name)
    print(name_c_stages)
    group_block(name_c_stages[0])
    save_c_state(name_c_stages[1])
    density_prop(block_prop_density)
    
    if c_stage_name == 'dome_herringbone_7_1_90_12_1_1_1_1.wrl':
        mech_prop2(stif_norm2,stif_shear2,fric_angl2,stif_norm_Broken2,stif_shear_Broken2,fric_angl_Broken2)
    else:
        mech_prop1(stif_norm1,stif_shear1,fric_angl1,stif_norm_Broken1,stif_shear_Broken1,fric_angl_Broken1)
    
    gravity()
    cycle(number_cycle)
    save_c_state(name_c_stages[1].split("_State")[0]+'_E_State')
    
it.command("""
    model solve ratio-average 1e-9
    model save '../../3dec_output/HD_UC_7_1_90_12_1_1_Output/Complete_dome'
    """)




