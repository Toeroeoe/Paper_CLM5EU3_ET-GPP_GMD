


# Settings

name                        = 'CLOSE-GPP' #'CLOSE-Temp-Precip-SWdn-RH' # 'CLOSE-NEE-RE' 'CLOSE'

run                         = '003'

sources_grids               = ['CLM5-EU3', 'CLM5-EU3-pft', 'GLASS-EU3']#, 'ERA5L-EU3', 'GLEAM-EU3']

sources_static              = ['CLM5-EU3-surf']

sources_insitu              = ['ICOS-WARMWINTER2020']

variables                   = ['GPP']

year_start                  = 1995
year_end                    = 2018

dst_time_str                = '8D'
method_time_interp          = 'mean'

path_stations               = '/p/scratch/cjibg31/jibg3105/projects/papers/CLM5EU3_Ecosystem_Processes/user_in/csv/'
file_stations               = 'stations.csv'

file_format                 = 'parquet'

plots                       = {
                                #'location_map',
                                #'pie_landcover',
                                'xy_landcover', 
                                'doy_dist_landcover', 
                                'doy_landcover', 
                                'single_site_model_benchmarks', 
                                'landcover_model_benchmarks', 
                                #'station_info',
                                'bar_rmse_landcover',
                                }



# Execute
from Analyses import Grids_vs_InSitu
from Analyses import Grid_vs_Grid

Grids_vs_InSitu.run(name = name, run = run, sources_grids = sources_grids, sources_static = sources_static,
    sources_insitu = sources_insitu, variables = variables, file_format = file_format,
    path_stations = path_stations, file_stations = file_stations,
    year_start = year_start, year_end = year_end, dst_time_str = dst_time_str,
    method_time_interp = method_time_interp, 
    plots = plots)


#Grid_vs_Grid.run()