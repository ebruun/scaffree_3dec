c_support_names = ['dome_herringbone_5_1_65_12_1_1_0_0.wrl']

c_stage_names = [
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
    'dome_herringbone_5_1_65_12_1_1_54_78.wrl',
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
    
    [-0.06120, -2.33715, 4.99700], #C59M   #75
    [ 0.54578, -2.27336, 4.99700], #C59Co   #81
    
    [ 0.39271, -1.63576, 5.25415], #C70M    #87
    [-0.04403, -1.68167, 5.25415], #C70Co   #93
    
    [-0.03272, -1.24957, 5.37341], #C78M    #99
    [ 0.29180, -1.21546, 5.37341], #C78Co   #105
    ]
