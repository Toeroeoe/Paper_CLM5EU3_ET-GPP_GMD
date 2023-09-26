


# Settings

name                        = 'CLOSE'

sources_grids               = ['GLASS-EU3', 'CLM5-EU3', 'CLM5-EU3-pft', 'ERA5L-EU3', 'GLEAM-EU3']

sources_static              = ['CLM5-EU3-surf']

sources_insitu              = ['ICOS-WARMWINTER2020']

variables                   = ['GPP', 'ET']

year_start                  = 1995
year_end                    = 2018

dst_time_str                = '8D'
method_time_interp          = 'mean'

path_stations               = '/p/scratch/cjibg31/jibg3105/Data/CLM5EU3/code_clm5eu3/Projects/CLM5EU3_Ecosystem_Processes/user_in/csv/'
file_stations               = 'stations.csv'

file_format                 = 'parquet'


# Execute
from Analyses import Grids_vs_InSitu
from Analyses import Grid_vs_Grid

Grids_vs_InSitu.run(name = name, sources_grids = sources_grids, sources_static = sources_static,
    sources_insitu = sources_insitu, variables = variables, file_format = file_format,
    path_stations = path_stations, file_stations = file_stations,
    year_start = year_start, year_end = year_end, dst_time_str = dst_time_str,
    method_time_interp = method_time_interp)


#Grid_vs_Grid.run()