import itasca as it
#import json
from re import split

#######################################################

it.command("python-reset-state false")

it.command("""
    model new
    model large-strain on
    """)
    
########################################################

def model_func(model):
    model_action = '''
    block hide on
    block generate from-vrml filename '{}'
    '''.format(model)
    it.command(model_action)

def coord_fun(point):
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

def names_func(name):
    temp_name_block_group = split_string(name, ['dome_herringbone_5_1_65_12_1_1_','.wrl'])
    name_block_group = 'C' + temp_name_block_group[1]
    name_state = temp_name_block_group[1] + '_State'
    temp_name_list = [name_block_group, name_state]
    return(temp_name_list)

def group_func(gname):
    gname_action = '''
    block group '{}'
    block hide off
    '''.format(gname)
    it.command(gname_action)

def state_func(state):
    state_action = '''
    model save '{}'
    '''.format(state)
    it.command(state_action) 

def den_prop_func(den_value):
    density_action = '''
    block property density {}
    '''.format(den_value)
    it.command(density_action)
    
def mech_prop_func1(stif_n1,stif_s1,fric_a1,stif_n_Brok1,stif_s_Brok1,fric_a_Brok1):
    mech_prop_action = '''
    block contact generate-subcontacts
    block contact group 'boundary'
    block contact prop stiffness-norm={} stiffness-shear={} friction={} range group 'boundary'
    block contact material-table default prop stiffness-norm={} stiffness-shear={} friction={}
    '''.format(stif_n1,stif_s1,fric_a1,stif_n_Brok1,stif_s_Brok1,fric_a_Brok1)
    it.command(mech_prop_action)
    
def mech_prop_func2(stif_n2,stif_s2,fric_a2,stif_n_Brok2,stif_s_Brok2,fric_a_Brok2):
    mech_prop_action  = '''
    block contact generate-subcontacts
    block contact group 'boundary'
    block contact prop stiffness-norm={} stiffness-shear={} friction={} range group 'boundary'
    block contact material-table default prop stiffness-norm={} stiffness-shear={} friction={}
    '''.format(stif_n2,stif_s2,fric_a2,stif_n_Brok2,stif_s_Brok2,fric_a_Brok2)
    it.command(mech_prop_action)
    
def grav_func():
    gravity_action = '''
    block mechanical damping global
    model gravity 0 0 -9.81
    '''
    it.command(gravity_action)
    
def cyc_func(cyc):
    cycle_action = '''
    model cycle  {}
    '''.format(cyc)
    it.command(cycle_action)
    
    
  
##########################################################

# model geometry

supports = ['dome_herringbone_5_1_65_12_1_1_0_0.wrl']

var_list = [
    'dome_herringbone_5_1_65_12_1_1_1_1.wrl',
    'dome_herringbone_5_1_65_12_1_1_2_17.wrl',
    'dome_herringbone_5_1_65_12_1_1_18_35.wrl',
    'dome_herringbone_5_1_65_12_1_1_36_36_0.wrl',
    'dome_herringbone_5_1_65_12_1_1_36_36_1.wrl',
    'dome_herringbone_5_1_65_12_1_1_36_36_2.wrl',
    'dome_herringbone_5_1_65_12_1_1_36_36_3.wrl',
    'dome_herringbone_5_1_65_12_1_1_36_36_4.wrl',
    'dome_herringbone_5_1_65_12_1_1_36_36_5.wrl',
    'dome_herringbone_5_1_65_12_1_1_36_36_6.wrl',
    'dome_herringbone_5_1_65_12_1_1_36_36_7.wrl',
    'dome_herringbone_5_1_65_12_1_1_36_36_8.wrl',
    'dome_herringbone_5_1_65_12_1_1_36_36_9.wrl',
    'dome_herringbone_5_1_65_12_1_1_36_36_10.wrl',
    'dome_herringbone_5_1_65_12_1_1_36_36_11.wrl',
    'dome_herringbone_5_1_65_12_1_1_36_36_12.wrl',
    'dome_herringbone_5_1_65_12_1_1_36_36_13.wrl',
    'dome_herringbone_5_1_65_12_1_1_36_36_14.wrl',
    'dome_herringbone_5_1_65_12_1_1_36_36_15.wrl',
    'dome_herringbone_5_1_65_12_1_1_36_36_16.wrl',
    'dome_herringbone_5_1_65_12_1_1_36_36_17.wrl',
    'dome_herringbone_5_1_65_12_1_1_36_36_18.wrl',
    'dome_herringbone_5_1_65_12_1_1_36_36_19.wrl',
    'dome_herringbone_5_1_65_12_1_1_36_36_20.wrl',
    'dome_herringbone_5_1_65_12_1_1_36_36_21.wrl',
    'dome_herringbone_5_1_65_12_1_1_36_36_22.wrl',
    'dome_herringbone_5_1_65_12_1_1_36_36_23.wrl',
    'dome_herringbone_5_1_65_12_1_1_36_53.wrl',
    'dome_herringbone_5_1_65_12_1_1_54_54_0.wrl',
    'dome_herringbone_5_1_65_12_1_1_54_54_1.wrl',
    'dome_herringbone_5_1_65_12_1_1_54_54_2.wrl',
    'dome_herringbone_5_1_65_12_1_1_54_54_3.wrl',
    'dome_herringbone_5_1_65_12_1_1_54_54_4.wrl',
    'dome_herringbone_5_1_65_12_1_1_54_54_5.wrl',
    'dome_herringbone_5_1_65_12_1_1_54_54_6.wrl',
    'dome_herringbone_5_1_65_12_1_1_54_54_7.wrl',
    'dome_herringbone_5_1_65_12_1_1_54_54_8.wrl',
    'dome_herringbone_5_1_65_12_1_1_54_54_9.wrl',
    'dome_herringbone_5_1_65_12_1_1_54_54_10.wrl',
    'dome_herringbone_5_1_65_12_1_1_54_54_11.wrl',
    'dome_herringbone_5_1_65_12_1_1_54_54_12.wrl',
    'dome_herringbone_5_1_65_12_1_1_54_54_13.wrl',
    'dome_herringbone_5_1_65_12_1_1_54_54_14.wrl',
    'dome_herringbone_5_1_65_12_1_1_54_54_15.wrl',
    'dome_herringbone_5_1_65_12_1_1_54_54_16.wrl',
    'dome_herringbone_5_1_65_12_1_1_54_54_17.wrl',
    'dome_herringbone_5_1_65_12_1_1_54_54_18.wrl',
    'dome_herringbone_5_1_65_12_1_1_54_54_19.wrl',
    'dome_herringbone_5_1_65_12_1_1_54_54_20.wrl',
    'dome_herringbone_5_1_65_12_1_1_54_54_21.wrl',
    'dome_herringbone_5_1_65_12_1_1_54_54_22.wrl',
    'dome_herringbone_5_1_65_12_1_1_54_54_23.wrl',
    'dome_herringbone_5_1_65_12_1_1_54_71.wrl',
    'dome_herringbone_5_1_65_12_1_1_72_78.wrl',
    ]

# mech prop
block_prop_density = 2000 #[kg/m^3]

# stiffness-norm [Pa/m] 
stif_norm1 = 1.5e9
stif_norm2 = 1.0e9
stif_norm_Broken1 = 1.0e9
stif_norm_Broken2 = 1.0e9
# stiffness-shear [Pa/m] 
stif_shear1 = 1.5e8
stif_shear2 = 1.0e8
stif_shear_Broken1 = 1.0e8
stif_shear_Broken2 = 1.0e8

# friction angle[grad]
fric_angl1 = 25 
fric_angl2 = 25
fric_angl_Broken1 = 25
fric_angl_Broken2 = 20
# cycle
number_cycle = 40000

#point to check 
#notation C=corner Number=brick_course M=middle_sail Co=corner
# CNunM = [x,y,z]
points_list = [
    [-0.13016, -4.97088, 2.38948], #C02M    #03
    [ 1.16082, -4.83519, 2.38948], #C02Co   #09
    
    [ 0.96932, -4.56031, 2.94957], #C10M    #15
    [-0.12204, -4.66059, 2.94957], #C10Co   #21
    
    [-0.11331, -4.32751, 3.41991], #C19M    #27
    [ 1.00124, -4.17048, 3.46994], #C19Co   #33
    
    [ 0.90069, -3.75139, 3.94952], #C30M    #39
    [-0.10099, -3.85667, 3.94351], #C30Co   #45
    
    [-3.09521, -1.78702, 4.20265], ##C36M   #51
    [-3.54341, -0.04665, 4.20265], ##C36Co  #57
    
    [-0.08834, -3.37386, 4.36409], #C40M    #51
    [ 0.78788, -3.28176, 4.36409], #C40Co   #57
    
    [ 0.66451, -2.76791, 4.72571], #C50M    #63
    [-0.07451, -2.84559, 4.72571], #C50Co   #69
    
    [ 2.48001, -0.66451, 4.88304], ##C54M   #75
    [-2.55300, -0.26837, 4.88304], ##C54Co  #81
    
    [ 0.39271, -1.63576, 5.25415], #C70M    #75
    [-0.04403, -1.68167, 5.25415], #C70Co   #81
    
    [-0.03272, -1.24957, 5.37341], #C78M    #87
    [ 0.29180, -1.21546, 5.37341], #C78Co   #93
    ]

##########################################################

model_func(supports[0])
name_list = names_func(supports[0])

#group_func(name_list[0])
#
#state_func(name_list[1])

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

# 'check before lunch'
for var in var_list:
    if var == 'dome_herringbone_5_1_65_12_1_1_36_53.wrl':
        it.command("model restore '18_35_E_State'")
    elif var == 'dome_herringbone_5_1_65_12_1_1_54_71.wrl':
        it.command("model restore '36_53_E_State'")
    model_func(var)
    if var =='dome_herringbone_5_1_65_12_1_1_2_17.wrl':
        coord_fun(points_list[0])
        coord_fun(points_list[1])
        coord_fun(points_list[2])
        coord_fun(points_list[3])
    elif var =='dome_herringbone_5_1_65_12_1_1_18_35.wrl':
        coord_fun(points_list[4])
        coord_fun(points_list[5])
        coord_fun(points_list[6])
        coord_fun(points_list[7])
    elif var =='dome_herringbone_5_1_65_12_1_1_36_36_0.wrl':
        coord_fun(points_list[8])
        coord_fun(points_list[9])
    elif var =='dome_herringbone_5_1_65_12_1_1_36_53.wrl':
        coord_fun(points_list[10])
        coord_fun(points_list[11]) 
        coord_fun(points_list[12])
        coord_fun(points_list[13]) 
    elif var =='dome_herringbone_5_1_65_12_1_1_54_54_0.wrl':
        coord_fun(points_list[14])
        coord_fun(points_list[15]) 
    elif var =='dome_herringbone_5_1_65_12_1_1_54_71.wrl':
        coord_fun(points_list[16])
        coord_fun(points_list[17]) 
    elif var =='dome_herringbone_5_1_65_12_1_1_72_78.wrl':
        coord_fun(points_list[18])
        coord_fun(points_list[19])
    name_list = names_func(var)
    group_func(name_list[0])
    state_func(name_list[1])
    den_prop_func(block_prop_density)
    if var == 'dome_herringbone_5_1_65_12_1_1_1_1.wrl':
        mech_prop_func2(stif_norm2,stif_shear2,fric_angl2,stif_norm_Broken2,stif_shear_Broken2,fric_angl_Broken2)
    else:
        mech_prop_func1(stif_norm1,stif_shear1,fric_angl1,stif_norm_Broken1,stif_shear_Broken1,fric_angl_Broken1)
    grav_func()
    cyc_func(number_cycle)
    state_func(name_list[1].split("_State")[0]+'_E_State')





