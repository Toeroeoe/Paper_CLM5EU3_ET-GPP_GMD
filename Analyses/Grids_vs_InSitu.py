""" 

"""


def run(name: str, sources_grids = [], sources_static = [],
        sources_insitu = [],  variables = [], 
        file_format: str = 'parquet',
        path_stations: str = 'gridded/csv_in', file_stations: str = 'stations.csv',
        year_start: int = 1995, year_end: int = 2018, dst_time_str: str = 'D',
        method_time_interp = 'mean'):


    from glob import glob
    from itertools import product
    from matplotlib.backends.backend_pdf import PdfPages

    from my_.data_process.cells_df import src_var_cells_df, cell_static_info
    from my_.data_process.insitu_df import src_var_insitu_df
    from my_.files.csv import open_csv
    from my_.files.handy import read_resample_save
    from my_.series.aggregate import concat

    from my_.figures.save import save_png, save_pdf

    from my_.plot.custom import single_EU3_point_locations
    from my_.plot.custom import xy_landcover_moments

    from user_in.options_plots import EU3_maps, land_cover_moments
    from user_in.options_analyses import selected_landcover
    

    print('\nLocate files or create the necessary source dataframes')
    print('for all stations / cells...\n')

    src_var_cells_df(name_case = name, sources = sources_grids, variables = variables,
                        file_format = file_format, path_stations = path_stations, 
                        file_stations = file_stations, year_start = year_start, 
                        year_end = year_end)

    cell_static_info(name_case = name, sources = sources_static, 
                        path_stations = path_stations, file_stations = file_stations)


    src_var_insitu_df(name_case = name, sources = sources_insitu, variables = variables,
                        file_format = file_format, path_stations = path_stations,
                        file_stations = file_stations, year_start = year_start,
                        year_end = year_end)
    

    print('Load the files to dataframe')
    print('and resample to the chosen frequency...\n')

    file_static                 = glob(f'out/csv/Static_data_{name}_*.csv')[0]
  
    files_cells                 = [f'out/{file_format}/Extracted_{name}_{src}.{file_format}' for src in sources_grids]
    files_insitu                = [f'out/{file_format}/Insitu_{name}_{src}.{file_format}' for src in sources_insitu]

    df_cells                    = read_resample_save(case_name = name, files = files_cells, origin = 'Cells',
                                                    file_format = file_format, join = 'outer', offset_str = dst_time_str,
                                                    interp_method = method_time_interp)

    df_insitu                   = read_resample_save(case_name = name, files = files_insitu, origin = 'Insitu',
                                                    file_format = file_format, join = 'outer', offset_str = dst_time_str,
                                                    interp_method = method_time_interp)

    print('Load the insitu and cell files to a common dataframe')
    print('and load the static and station information data...\n')
    
    df_merged                   = concat([df_insitu, df_cells], join = 'outer', axis = 1)


    df_static                   = open_csv(file_static)
    df_stations                 = open_csv(f'{path_stations}/{file_stations}')
    
    names_stations              = df_stations['name']
    lats_stations               = df_stations['lat']
    lons_stations               = df_stations['lon']

    n_stations                  = len(names_stations)
    n_variables                 = len(variables)

    iterations                  = product(range(n_stations), range(n_variables))

    name_pdf                    = f'out/pdf/{name}.pdf'

    
    with PdfPages(name_pdf) as pdf:
        
        fig1                    = single_EU3_point_locations(lats_stations, lons_stations, 
                                                             **EU3_maps['base'], **EU3_maps['lines'], 
                                                             **EU3_maps['locations_map'])
        
        save_png(fig1, 'out/png/ICOS_locations')
        save_pdf(pdf, fig1)

        for vv in variables:

            fig2x               = xy_landcover_moments(df_merged, vv, sources_insitu, sources_grids, selected_landcover,
                                                    markers = land_cover_moments['markers'], colors = land_cover_moments['i_color'],
                                                    xy_init_args = land_cover_moments['init_xy'],
                                                    xy_args = land_cover_moments['xy'], marker_legend_args = land_cover_moments['marker_legend'],
                                                    color_legend_args = land_cover_moments['color_legend'])

            save_png(fig2x, f'out/png/{name}_{vv}_xy_landcover_moments')
            save_pdf(pdf, fig2x)


        exit()
        
        #plot_var_agg_PFT(name, pdf, variables, target_units, sources_insitu, sources_grids, master_df, cells_data)
        for i_station, i_var in iterations:

            station             = data_stations['name'][i_station]
            var                 = variables[i_var]        

            print('Loading cell and in-situ data for station ' + station)
            print('and variable ' + var + '...\n')

            # Continue with columns (station-variables) that exist in the data
            cols                = [col for col in master_df.columns if (station + '_' in col) & (var in col)]
            ts                  = [master_df[col] for col in cols]

            if i_var==0: plot_station_info(name, pdf, station, cells_data)
            plot_timeseries(name, pdf, timeseries=ts, labels=cols, units=target_units[i_var])
            plot_seasonal_stats(name, pdf, timeseries=ts, labels=cols, units=target_units[i_var])

    print('###########')
    print('That\'s it! Cell and in-situ data was processed and saved; Time-series were plotted. Ciao!')
    print('___________')
