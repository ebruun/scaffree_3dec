#;-----------------------------------------
#
#; Plot geometry
#block hide on
#block generate from-vrml filename 'dome_herringbone_5_1_65_12_1_1_54_54_22.wrl'
#block group 'C54_54_22'
#block hide off
#
#model save '54_54_22_State'
#
#; Material--Units: m, kg/m^3, N, Pa/m, m/s^2--Bricks Masonry (Dim 0.05*0.1*0.2 [m])
#block property density 2000
#
#; Interfaces properties
#block contact generate-subcontacts
#block contact prop stiffness-norm=1.5e9 stiffness-shear=1.5e8 friction=25
#block contact material-table default prop stiffness-norm=1e9 stiffness-shear=1e8 friction=15
#
#; Damping
#block mechanical damping global
#
#; Laods--Gravity [m/s^2]
#

#model gravity 0 0 -9.81
#model cycle  20000  ;20000
#
#model save '54_54_22E_State'
#
#;-----------------------------------------

import itasca as it
import json

it.command("python-reset-state false")

it.command("""
    model new
    """
    )

def analysis_func(x):
    
    model_name = x
    
    x = '''
    block hide on
    block generate from-vrml filename '{}'
    '''.format(model_name)

    print(x)
    it.command(x)


var_list = [
    'dome_herringbone_5_1_65_12_1_1_54_54_20.wrl',
    'dome_herringbone_5_1_65_12_1_1_54_54_21.wrl',
    'dome_herringbone_5_1_65_12_1_1_54_54_22.wrl',
    'dome_herringbone_5_1_65_12_1_1_54_54_23.wrl',
]

for var in var_list:
    analysis_func(var)
    
