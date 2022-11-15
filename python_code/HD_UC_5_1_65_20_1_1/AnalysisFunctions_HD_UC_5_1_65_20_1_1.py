import itasca as it
import json
from re import split
import os
#from HD_UC_5_1_65_20_1_1 import name_supports, name_list
#from input_HD_UC_5_1_65_20_1_1 import c_support_names, c_stage_names, mech_properties, points #

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

c_support_names = ['dome_herringbone_5_1_65_20_1_1_0_0.wrl']

c_stage_names = [
    'dome_herringbone_5_1_65_20_1_1_1_1.wrl',
    'dome_herringbone_5_1_65_20_1_1_2_17.wrl',
    'dome_herringbone_5_1_65_20_1_1_18_35.wrl',
    'dome_herringbone_5_1_65_20_1_1_36_36_0.wrl',
    'dome_herringbone_5_1_65_20_1_1_36_36_1.wrl',
    'dome_herringbone_5_1_65_20_1_1_36_36_2.wrl',
    'dome_herringbone_5_1_65_20_1_1_36_36_3.wrl',
    'dome_herringbone_5_1_65_20_1_1_36_36_4.wrl',
    'dome_herringbone_5_1_65_20_1_1_36_36_5.wrl',
    'dome_herringbone_5_1_65_20_1_1_36_36_6.wrl',
    'dome_herringbone_5_1_65_20_1_1_36_36_7.wrl',
    'dome_herringbone_5_1_65_20_1_1_36_36_8.wrl',
    'dome_herringbone_5_1_65_20_1_1_36_36_9.wrl',
    'dome_herringbone_5_1_65_20_1_1_36_36_10.wrl',
    'dome_herringbone_5_1_65_20_1_1_36_36_11.wrl',
    'dome_herringbone_5_1_65_20_1_1_36_36_12.wrl',
    'dome_herringbone_5_1_65_20_1_1_36_36_13.wrl',
    'dome_herringbone_5_1_65_20_1_1_36_36_14.wrl',
    'dome_herringbone_5_1_65_20_1_1_36_36_15.wrl',
    'dome_herringbone_5_1_65_20_1_1_36_36_16.wrl',
    'dome_herringbone_5_1_65_20_1_1_36_36_17.wrl',
    'dome_herringbone_5_1_65_20_1_1_36_36_18.wrl',
    'dome_herringbone_5_1_65_20_1_1_36_36_19.wrl',
    'dome_herringbone_5_1_65_20_1_1_36_53.wrl',
    'dome_herringbone_5_1_65_20_1_1_54_54_0.wrl',
    'dome_herringbone_5_1_65_20_1_1_54_54_1.wrl',
    'dome_herringbone_5_1_65_20_1_1_54_54_2.wrl',
    'dome_herringbone_5_1_65_20_1_1_54_54_3.wrl',
    'dome_herringbone_5_1_65_20_1_1_54_54_4.wrl',
    'dome_herringbone_5_1_65_20_1_1_54_54_5.wrl',
    'dome_herringbone_5_1_65_20_1_1_54_54_6.wrl',
    'dome_herringbone_5_1_65_20_1_1_54_54_7.wrl',
    'dome_herringbone_5_1_65_20_1_1_54_54_8.wrl',
    'dome_herringbone_5_1_65_20_1_1_54_54_9.wrl',
    'dome_herringbone_5_1_65_20_1_1_54_54_10.wrl',
    'dome_herringbone_5_1_65_20_1_1_54_54_11.wrl',
    'dome_herringbone_5_1_65_20_1_1_54_54_12.wrl',
    'dome_herringbone_5_1_65_20_1_1_54_54_13.wrl',
    'dome_herringbone_5_1_65_20_1_1_54_54_14.wrl',
    'dome_herringbone_5_1_65_20_1_1_54_54_15.wrl',
    'dome_herringbone_5_1_65_20_1_1_54_54_16.wrl',
    'dome_herringbone_5_1_65_20_1_1_54_54_17.wrl',
    'dome_herringbone_5_1_65_20_1_1_54_54_18.wrl',
    'dome_herringbone_5_1_65_20_1_1_54_54_19.wrl',
    'dome_herringbone_5_1_65_20_1_1_54_78.wrl',
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

    'number_cycle': 5,     # cycle

}


#point to check 
#notation C=corner Number=brick_course M=middle_sail Co=corner
# CNunM = [x,y,z]
points= [

    [-0.13016,-4.9708,2.3894], #C02M    #03
    [ 0.64905,-4.9330,2.3894], #C02Co   #09

    [ 0.62576,-4.7531,2.7298], #C08M    #15
    [-0.12549,-4.7924,2.7298], #C08Co   #21

    [-0.12021,-4.5908,3.0570], #C14M    #27
    [ 0.59943,-4.5531,3.0570], #C14Co   #33

    [ 0.57019,-4.3310,3.3694], #C20M   #39 #6
    [-0.11435,-4.3669,3.3694], #C20Co  #45

    [-0.10793,-4.1218,3.6654], #C26M   #27
    [ 0.53818,-4.0879,3.6654], #C26Co  #33

    [ 0.50356,-3.8249,3.9435], #C32M   #39
    [-0.10099,-3.8566,3.9435], #C32Co  #45

    [-0.09482,-3.6213,4.1608], #C35M   #51
    [ 0.47284,-3.5916,4.1608], #C35Co  #57 #13

    [-3.39911,-1.1044,4.2026], #C36M  #63 #
    [-3.22587,-1.5386,4.2026], #C36Co #69 #15 #

    [ 0.42717,-3.2447,4.4413], #C43M  #63 #16
    [-0.08567,-3.2716,4.4413], #C43Co #69

    [-0.07736,-2.9545,4.6584], #C48M   #75
    [ 0.38577,-2.9302,4.6584], #C48Co  #81 #19

    [ 0.34250,-2.6015,4.8528], #C54M   #87 # 20#
    [-0.06868,-2.6231,4.8528], #C54Co  #93 #

    [-2.59172,-0.4104,4.8528], #C54M   #87 #22
    [-2.51597,-0.7452,4.8528], #C54Co  #93

    [-0.05967,-2.2789,5.0238], #C60M   #99 
    [ 0.29756,-2.2602,5.0238], #C60Co  #105

    [ 0.25118,-1.9079,5.1703], #C66M   #111
    [-0.05037,-1.9237,5.1703], #C66Co  #117

    [-0.04082,-1.5592,5.2918], #C72M  #123
    [ 0.20358,-1.5464,5.2918], #C72Co #129

    [ 0.16315,-1.239306,5.37], #C78M  #135
    [ -2.e-16,-1.25,5.3734]    #C78Co #141 #31
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
    temp_name_block_group = split_string(name, ['dome_herringbone_5_1_65_20_1_1_','.wrl'])
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
    model save '../../3dec_output/HD_UC_5_1_65_20_1_1_Output/{}' inputdir 
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
    block contact group 'boundary'
    block contact prop stiffness-norm={} stiffness-shear={} friction={} range group 'boundary'
    block contact material-table default prop stiffness-norm={} stiffness-shear={} friction={}
    '''.format(stif_n1,stif_s1,fric_a1,stif_n_Brok1,stif_s_Brok1,fric_a_Brok1)
    it.command(mech_prop_action)
    
def mech_prop2(stif_n2,stif_s2,fric_a2,stif_n_Brok2,stif_s_Brok2,fric_a_Brok2):
    mech_prop_action  = '''
    block contact generate-subcontacts
    block contact group 'boundary'
    block contact prop stiffness-norm={} stiffness-shear={} friction={} range group 'boundary'
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
path_input('input_HD_UC_5_1_65_20_1_1', cwd_path)
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

    if c_stage_name == 'dome_herringbone_5_1_65_20_1_1_36_53.wrl':
        it.command("model restore '../../3dec_output/HD_UC_5_1_65_20_1_1_Output/18_35_E_State'") ##check the path
    elif c_stage_name == 'dome_herringbone_5_1_65_20_1_1_54_78.wrl':
        it.command("model restore '../../3dec_output/HD_UC_5_1_65_20_1_1_Output/36_53_E_State'")
    model_geometries(c_stage_name,cwd_path)
    if c_stage_name =='dome_herringbone_5_1_65_20_1_1_2_17.wrl':
        coord_point(points[0])
        coord_point(points[1])
        coord_point(points[2])
        coord_point(points[3])
        coord_point(points[4])
        coord_point(points[5])
    elif c_stage_name =='dome_herringbone_5_1_65_20_1_1_18_35.wrl':
        coord_point(points[6])
        coord_point(points[7])
        coord_point(points[8])
        coord_point(points[9])        
        coord_point(points[10])
        coord_point(points[11])        
        coord_point(points[12])
        coord_point(points[13])              
    elif c_stage_name =='dome_herringbone_5_1_65_20_1_1_36_36_0.wrl':
        coord_point(points[14])
        coord_point(points[15])
    elif c_stage_name =='dome_herringbone_5_1_65_20_1_1_36_53.wrl':
        coord_point(points[16])
        coord_point(points[17])
        coord_point(points[18])
        coord_point(points[19])       
    elif c_stage_name =='dome_herringbone_5_1_65_20_1_1_54_54_0.wrl':
        coord_point(points[20])
        coord_point(points[21]) 
    elif c_stage_name =='dome_herringbone_5_1_65_20_1_1_54_78.wrl':
        coord_point(points[22])
        coord_point(points[23]) 
        coord_point(points[24])
        coord_point(points[25])
        coord_point(points[26])
        coord_point(points[27])  
        coord_point(points[28])
        coord_point(points[29])
        coord_point(points[30])
        coord_point(points[31]) 

    name_c_stages = names_c_construction(c_stage_name)
    print(name_c_stages)
    group_block(name_c_stages[0])
    save_c_state(name_c_stages[1])
    density_prop(block_prop_density)
    
    if c_stage_name == 'dome_herringbone_5_1_65_20_1_1_1_1.wrl':
        mech_prop2(stif_norm2,stif_shear2,fric_angl2,stif_norm_Broken2,stif_shear_Broken2,fric_angl_Broken2)
    else:
        mech_prop1(stif_norm1,stif_shear1,fric_angl1,stif_norm_Broken1,stif_shear_Broken1,fric_angl_Broken1)
    
    gravity()
    cycle(number_cycle)
    save_c_state(name_c_stages[1].split("_State")[0]+'_E_State')
    
it.command("""
    model solve ratio-average 1e-9
    model save '../../3dec_output/HD_UC_5_1_65_20_1_1_Output/Complete_dome'
    """)




