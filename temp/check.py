
dir1            = '/p/scratch/cjibg31/jibg3105/Data/CLM5EU3/code_clm5eu3/Projects/Compare_Data/parquet_out'

print(df_sel_transformed)

from my_.series.group import select_multi_column
from my_.files.parquet import open_parquet
import numpy as np
trt  = df_sel_resampled.loc['2018-12-27':'2018-12-31', 'GPP_NT_VUT_REF'].values  
print(trt)
tor = select_multi_column(df_sel_transformed, 'Variable', 'GPP')['2018-12-27':'2018-12-31'].values.flatten()
ttt = select_multi_column(df_sel_transformed, 'Variable', 'ET')['2018-12-27':'2018-12-31'].values.flatten()
print(ttt)

insitu_val = open_parquet('/p/scratch/cjibg31/jibg3105/Data/CLM5EU3/code_clm5eu3/Projects/Compare_Data/insitu_data/parquet_out/Insitu_GI-06-GPP-ET_ICOS.parquet')
tal = insitu_val[f'{name}_GPP']['2018-12-27':'2018-12-31'].values
ter = insitu_val[f'{name}_ET']['2018-12-27':'2018-12-31'].values
print(tal)
if not np.array_equal(tal, tor, equal_nan = True): print ('GPP Unequal'); exit()
if not np.array_equal(ttt, ter, equal_nan = True): print ('GPP Unequal'); exit()


for n in names_stations:

        dasdasd = select_multi_column(df_merged, ['Source', 'Variable', 'Station'], ['ICOS-WARMWINTER2020', 'ET', n])['2018-01-01':'2018-12-31'].values.flatten()

        asss    = insitu_val[f'{n}_ET_ICOS']['2018-01-01':'2018-12-31'].values

        print(np.array_equal(dasdasd, asss, equal_nan = True))


import numpy as np
var = 'ET'
insitu_val = open_parquet('/p/scratch/cjibg31/jibg3105/Data/CLM5EU3/code_clm5eu3/Projects/Compare_Data/parquet_out/GI-06-GPP-ET_insitu.parquet')
CLM5_val = open_parquet('/p/scratch/cjibg31/jibg3105/Data/CLM5EU3/code_clm5eu3/Projects/Compare_Data/parquet_out/GI-06-GPP-ET_cells.parquet')
for n in names_stations:

        dasdasd = select_multi_column(df_merged, ['Source', 'Variable', 'Station'], ['ICOS-WARMWINTER2020', var, n])['1995-01-01':'1995-12-31'].values.flatten()
        kkkk = select_multi_column(df_merged, ['Source', 'Variable', 'Station'], ['CLM5-EU3', var, n])['1995-01-01':'2018-12-31'].values.flatten()
        ttittts = CLM5_val[f'{n}_{var}_CLM5']['1995-01-01':'2018-12-31'].values
        asss    = insitu_val[f'{n}_{var}_ICOS']['1995-01-01':'1995-12-31'].values

        print(np.array_equal(dasdasd, asss, equal_nan = True))
        print(np.array_equal(kkkk, ttittts, equal_nan = True))
exit()