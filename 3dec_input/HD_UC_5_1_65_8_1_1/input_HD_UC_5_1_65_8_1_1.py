c_support_names = ['dome_herringbone_5_1_65_8_1_1_0_0.wrl']

c_stage_names = [
    'dome_herringbone_5_1_65_8_1_1_1_1.wrl',
    'dome_herringbone_5_1_65_8_1_1_2_17.wrl',
    'dome_herringbone_5_1_65_8_1_1_18_35.wrl',
    'dome_herringbone_5_1_65_8_1_1_36_36_0.wrl',
    'dome_herringbone_5_1_65_8_1_1_36_36_1.wrl',
    'dome_herringbone_5_1_65_8_1_1_36_36_2.wrl',
    'dome_herringbone_5_1_65_8_1_1_36_36_3.wrl',
    'dome_herringbone_5_1_65_8_1_1_36_36_4.wrl',
    'dome_herringbone_5_1_65_8_1_1_36_36_5.wrl',
    'dome_herringbone_5_1_65_8_1_1_36_36_6.wrl',
    'dome_herringbone_5_1_65_8_1_1_36_36_7.wrl',
    'dome_herringbone_5_1_65_8_1_1_36_36_8.wrl',
    'dome_herringbone_5_1_65_8_1_1_36_36_9.wrl',
    'dome_herringbone_5_1_65_8_1_1_36_36_10.wrl',
    'dome_herringbone_5_1_65_8_1_1_36_36_11.wrl',
    'dome_herringbone_5_1_65_8_1_1_36_36_12.wrl',
    'dome_herringbone_5_1_65_8_1_1_36_36_13.wrl',
    'dome_herringbone_5_1_65_8_1_1_36_36_14.wrl',
    'dome_herringbone_5_1_65_8_1_1_36_36_15.wrl',
    'dome_herringbone_5_1_65_8_1_1_36_36_16.wrl',
    'dome_herringbone_5_1_65_8_1_1_36_36_17.wrl',
    'dome_herringbone_5_1_65_8_1_1_36_36_18.wrl',
    'dome_herringbone_5_1_65_8_1_1_36_36_19.wrl',
    'dome_herringbone_5_1_65_8_1_1_36_36_20.wrl',
    'dome_herringbone_5_1_65_8_1_1_36_36_21.wrl',
    'dome_herringbone_5_1_65_8_1_1_36_36_22.wrl',
    'dome_herringbone_5_1_65_8_1_1_36_36_23.wrl',
    'dome_herringbone_5_1_65_8_1_1_36_53.wrl',
    'dome_herringbone_5_1_65_8_1_1_54_54_0.wrl',
    'dome_herringbone_5_1_65_8_1_1_54_54_1.wrl',
    'dome_herringbone_5_1_65_8_1_1_54_54_2.wrl',
    'dome_herringbone_5_1_65_8_1_1_54_54_3.wrl',
    'dome_herringbone_5_1_65_8_1_1_54_54_4.wrl',
    'dome_herringbone_5_1_65_8_1_1_54_54_5.wrl',
    'dome_herringbone_5_1_65_8_1_1_54_54_6.wrl',
    'dome_herringbone_5_1_65_8_1_1_54_54_7.wrl',
    'dome_herringbone_5_1_65_8_1_1_54_54_8.wrl',
    'dome_herringbone_5_1_65_8_1_1_54_54_9.wrl',
    'dome_herringbone_5_1_65_8_1_1_54_54_10.wrl',
    'dome_herringbone_5_1_65_8_1_1_54_54_11.wrl',
    'dome_herringbone_5_1_65_8_1_1_54_54_12.wrl',
    'dome_herringbone_5_1_65_8_1_1_54_54_13.wrl',
    'dome_herringbone_5_1_65_8_1_1_54_54_14.wrl',
    'dome_herringbone_5_1_65_8_1_1_54_54_15.wrl',
    'dome_herringbone_5_1_65_8_1_1_54_54_16.wrl',
    'dome_herringbone_5_1_65_8_1_1_54_54_17.wrl',
    'dome_herringbone_5_1_65_8_1_1_54_54_18.wrl',
    'dome_herringbone_5_1_65_8_1_1_54_54_19.wrl',
    'dome_herringbone_5_1_65_8_1_1_54_54_20.wrl',
    'dome_herringbone_5_1_65_8_1_1_54_54_21.wrl',
    'dome_herringbone_5_1_65_8_1_1_54_54_22.wrl',
    'dome_herringbone_5_1_65_8_1_1_54_54_23.wrl',
    'dome_herringbone_5_1_65_8_1_1_54_78.wrl',
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
#C2M-Co
[-0.13016709,-4.97088,2.38948]
[1.78201496601,-4.64230775833,2.38945031166]
#C16M-Co
[1.60662,-4.18538,3.21519]
[-0.117355,-4.48161,3.21519]
#C32M-Co
[-7.08702e-16,-3.85799,3.9436]
[1.47639000416,-3.56432080269,3.94359731674]
#C45M-Co
[1.13556337357,-2.95824360847,4.51612234116]
[-0.0829470977187,-3.16762185097,4.51612234116]
#C62M-Co
[-0.0612005421647,-2.33715445151,4.99700260162]
[0.837848325297,-2.18266954102,4.99700260162]
#C72M-Co
[0.549696441814,-1.32708462441,5.32660770416]
[-0.0376012648751,-1.43593381256,5.32660770416]
#C78M-Co
[-0.0654199325169,-1.24828695256,5.37341356277]
[0.447959941495,-1.16697555790,5.37341356277]
#C36M-Co
[-3.33665704727,-1.28082263470,4.20265197754]
[-3.04737305641,-1.86743259430,4.20265197754]
#C54M-Co
[-2.44974374771,-0.940368533134,4.85288906097]
[-2.27247738838,-1.31201541424,4.85288906097]
    ]
