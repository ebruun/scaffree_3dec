import itasca as it
a = 'dd'
s = '''
    model restore '1_1_State'
    model save '../3dec_output/HD_UC_5_1_65_12_1_1_Output/{}' inputdir
    '''.format(a)

it.command(s)