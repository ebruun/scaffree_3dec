import itasca as it
import json
from re import split
import os

print("\nSTART ANALYSIS")

########################################################

it.command("""
    model new
    model large-strain on
    """)
    
########################################################

mech_properties = {
    'block_prop_density': 2000, #[kg/m^3]
    
    'stif_norm1': 1.0e9, # stiffness-norm [Pa/m] 
    'stif_norm2': 1.0e9,
    'stif_norm_Broken1': 1.0e9,
    'stif_norm_Broken2' : 1.0e9,

    'stif_shear1': 1.5e8,  # stiffness-shear [Pa/m] 
    'stif_shear2': 1.0e8,
    'stif_shear_Broken1': 1.0e8,
    'stif_shear_Broken2': 1.0e8,

    'fric_angl1': 15,     # friction angle[grad]
    'fric_angl2': 1,
    'fric_angl_Broken1': 15,
    'fric_angl_Broken2': 1,

    'number_cycle': 40000,     # cycle

}

########################################################

def path_input(file_name, cwd_path):
    model = os.path.join(cwd_path, file_name)
    
def save_c_state(c_state_name):
    #!heck the path
    state_action = '''
    model save '../../3dec_output/HD_UC_7_1_90_8_1_1_Output/{}' inputdir 
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
    block contact group 'Free2'
    block contact prop stiffness-norm={} stiffness-shear={} friction={} range group 'Free2'
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
    
 ########################################################  
 
it.command("model restore '../../3dec_output/HD_UC_7_1_90_8_1_1_Output/Complete_dome'") ##check the path

density_prop(block_prop_density)
mech_prop2(stif_norm2,stif_shear2,fric_angl2,stif_norm_Broken2,stif_shear_Broken2,fric_angl_Broken2)
mech_prop1(stif_norm1,stif_shear1,fric_angl1,stif_norm_Broken1,stif_shear_Broken1,fric_angl_Broken1)
gravity()
cycle(number_cycle)

it.command("""
    model solve ratio-average 1e-9
    model save '../../3dec_output/HD_UC_7_1_90_8_1_1_Output/Collapse_Low friction_Complete_dome'
    """)

