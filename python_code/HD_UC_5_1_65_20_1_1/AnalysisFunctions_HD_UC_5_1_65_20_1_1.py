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

    'number_cycle': 40000,     # cycle

}


#point to check 
#notation C=corner Number=brick_course M=middle_sail Co=corner
# CNunM = [x,y,z]
points= [
    [3.42290139198,-3.60698533058,2.38945031166], #C02M    #03
    [1.78201496601,-4.64230775833,2.38945031166], #C02Co   #09

    [1.59312653542,-4.15023660660,3.26704072952], #C16M    #15
    [3.08599567413,-3.25196099281,3.21519088745], #C16Co   #21

    [2.68701505661,-2.83152318001,3.89852499962], #C30M    #39
    [1.39890122414,-3.64426231384,3.89852499962], #C30Co   #45

    [-3.33665704727,-1.28082263470,4.20265197754], ##C36M   #51
    [-3.09521245956,-1.78702175617,4.20265197754], ##C36Co  #57

    [1.13556337357,-2.95824360847,4.51612234116], #C45M    #51
    [2.24061489105,-2.24061489105,4.51612234116], #C45Co   #57

    [-2.44974374771,-0.940368533134,4.85288906097], ##C54M   #63
    [-2.27247738838,-1.31201541424,4.85288906097]   ##C54Co  #69  

    [1.65318417549,-1.65318417549,4.99700260162],  #C59M   #63
    [0.837848305702,-2.18266963959,4.99700260162], #C59Co   #69

    [0.536903858185,-1.39868247509,5.30956602097], #C78M    #75
    [1.01570653915,-1.01570653915,5.32660770416],  #C78M    #81

    [0.883883476257,-0.883883476257,5.37341356277], #C78M    #87
    [0.447959929705,-1.16697549820,5.37341356277], #C78Co   #93
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
    elif c_stage_name =='dome_herringbone_5_1_65_20_1_1_18_35.wrl':
        coord_point(points[4])
        coord_point(points[5])
    elif c_stage_name =='dome_herringbone_5_1_65_20_1_1_36_36_0.wrl':
        coord_point(points[6])
        coord_point(points[7])
    elif c_stage_name =='dome_herringbone_5_1_65_20_1_1_36_53.wrl':
        coord_point(points[8])
        coord_point(points[9]) 
    elif c_stage_name =='dome_herringbone_5_1_65_20_1_1_54_54_0.wrl':
        coord_point(points[10])
        coord_point(points[11]) 
    elif c_stage_name =='dome_herringbone_5_1_65_20_1_1_54_78.wrl':
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




