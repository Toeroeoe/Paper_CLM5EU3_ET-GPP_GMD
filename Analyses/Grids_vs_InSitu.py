""" 

"""


def run(name: str, run: str, sources_grids = [], sources_static = [],
        sources_insitu = [],  variables = [], 
        file_format: str = 'parquet',
        path_stations: str = 'gridded/csv_in', file_stations: str = 'stations.csv',
        year_start: int = 1995, year_end: int = 2018, dst_time_str: str = 'D',
        method_time_interp = 'mean'):

    from glob import glob
    from matplotlib.backends.backend_pdf import PdfPages

    from my_.data_process.cells_df import src_var_cells_df, cell_static_info
    from my_.data_process.insitu_df import src_var_insitu_df
    from my_.files.csv import open_csv
    from my_.files.handy import read_resample_save, create_dirs
    from my_.series.aggregate import concat

    from my_.figures.save import save_png, save_pdf

    from my_.plot.custom import map_EU3_point_locations
    from my_.plot.custom import xy_landcover_moments
    from my_.plot.custom import bar_rmse_landcover
    from my_.plot.custom import doy_dist_landcover
    from my_.plot.custom import pie_landcover
    from my_.plot.custom import doy_landcover
    from my_.plot.custom import plot_ts
    from my_.plot.tables import single_site_model_benchmarks
    from my_.plot.tables import landcover_model_benchmarks

    from user_in.options_plots import EU3_maps, land_cover_moments, rmse_landcover
    from user_in.options_plots import doy_dist, sources_colors, landcover_colors
    from user_in.options_plots import station_ts
    from user_in.options_analyses import selected_landcover
    

    print('\nLocate files or create the necessary source dataframes')
    print('for all stations / cells...\n')

    out_path                    = f'out/{name}/'

    create_dirs([f'{out_path}/png/{run}', f'{out_path}/pdf/{run}', f'{out_path}/nc/', f'{out_path}/parquet/', f'{out_path}/csv/'])

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

    file_static                 = glob(f'out/{name}/csv/Static_data_*.csv')[0]
  
    files_cells                 = [f'out/{name}/{file_format}/Extracted_{src}.{file_format}' for src in sources_grids]
    files_insitu                = [f'out/{name}/{file_format}/Insitu_{src}.{file_format}' for src in sources_insitu]

    df_cells                    = read_resample_save(case_name = name, files = files_cells, origin = 'Cells',
                                                    file_format = file_format, join = 'outer', offset_str = dst_time_str,
                                                    interp_method = method_time_interp)

    df_insitu                   = read_resample_save(case_name = name, files = files_insitu, origin = 'Insitu',
                                                    file_format = file_format, join = 'outer', offset_str = dst_time_str,
                                                    interp_method = method_time_interp)

    print('Load the insitu and cell files to a common dataframe')
    print('and load the static and station information data...\n')
    
    df_merged                   = concat([df_insitu, df_cells], join = 'outer', axis = 1, sort = False)


    df_static                   = open_csv(file_static)
    df_stations                 = open_csv(f'{path_stations}/{file_stations}')
    
    names_stations              = df_stations['name']
    lats_stations               = df_stations['lat']
    lons_stations               = df_stations['lon']

    out_pdf                     = f'{out_path}/pdf/{run}/{name}.pdf'

    
    #plots = {'location_map', 'pie_landcover', 'xy_landcover', 'bar_rmse_landcover', 'doy_landcover', 'doy_dist_landcover', 'single_site_model_benchmarks'}

    #plots = {'single_site_model_benchmarks'}

    #plots = {'single_site_model_benchmarks', 'landcover_model_benchmarks'}#, 'station_info'}

    plots = {'xy_landcover', 'doy_dist_landcover', 'doy_landcover'}

    with PdfPages(out_pdf) as pdf:

        if 'location_map' in plots:
        
            fig1                    = map_EU3_point_locations(lats_stations, lons_stations, 
                                                                 **EU3_maps['base'], **EU3_maps['lines'], 
                                                                 **EU3_maps['locations_map'])
        
            save_png(fig1, f'{out_path}/png/{run}/map_ICOS_locations')
            save_pdf(pdf, fig1)

        if 'pie_landcover' in plots:

            fig2                    = pie_landcover(df_static, selected_landcover, landcover_colors['i_color'],
                                                    color_legend_args = rmse_landcover['color_legend'])
        
            save_png(fig2, f'{out_path}/png/{run}/pie_landcover')
            save_pdf(pdf, fig2)

        for vv in variables:

            print(f'Variable specific plots: {vv}\n')

            if 'xy_landcover' in plots:

                fig3x               = xy_landcover_moments(df_merged, vv, sources_insitu, sources_grids, selected_landcover,
                                                        markers = land_cover_moments['markers'], colors = sources_colors['i_color'],
                                                        xy_init_args = land_cover_moments['init_xy'],
                                                        xy_args = land_cover_moments['xy'], marker_legend_args = land_cover_moments['marker_legend'],
                                                        color_legend_args = land_cover_moments['color_legend'])
                save_png(fig3x, f'{out_path}/png/{run}/{vv}_xy_landcover_moments')
                save_pdf(pdf, fig3x)

            if 'single_site_model_benchmarks' in plots:

                single_site_model_benchmarks(df_merged, vv, sources_insitu[0], df_static, selected_landcover)
                
            if 'landcover_model_benchmarks' in plots:

                landcover_model_benchmarks(df_merged, vv, sources_insitu[0], df_static, selected_landcover)

            if 'doy_dist_landcover' in plots:

                fig4x               = doy_dist_landcover(df_merged, vv, sources_insitu, sources_grids, selected_landcover,
                                                        colors = sources_colors['i_color'], doy_init_args = doy_dist['init_doy'],
                                                        dist_init_args = doy_dist['init_dist'], doy_args = doy_dist['doy'],
                                                        doy_fill_args = doy_dist['doy_fill_args'], dist_args = doy_dist['dist'],
                                                        color_legend_args= doy_dist['color_legend'],
                                                        do_line_bounds = False, do_fill = False)
                save_png(fig4x, f'{out_path}/png/{run}/{vv}_doy-dist_landcover')
                save_pdf(pdf, fig4x)
                
            if 'bar_rmse_landcover' in plots:
                
                fig5x               = bar_rmse_landcover(df_merged, vv, sources_insitu, sources_grids, selected_landcover,
                                                         bar_init_args = rmse_landcover['init_bar'],
                                                         bar_args =  rmse_landcover['bars'],
                                                         colors = sources_colors['i_color'],
                                                         color_legend_args = rmse_landcover['color_legend'])

                save_png(fig5x, f'{out_path}/png/{run}/{vv}_bar_rmsd_landcover')
                save_pdf(pdf, fig5x)

            if 'doy_landcover' in plots:
                
                fig6x               = doy_landcover(df_merged, vv, sources_insitu, sources_grids, selected_landcover,
                                                        colors = sources_colors['i_color'], doy_init_args = doy_dist['init_doy'],
                                                        doy_args = doy_dist['doy'], doy_fill_args = doy_dist['doy_fill_args'],
                                                        color_legend_args = doy_dist['color_legend'], do_fill = False)
                save_png(fig6x, f'{out_path}/png/{run}/{vv}_doy_landcover')
                save_pdf(pdf, fig6x)

            if 'station_info' in plots:

                for station in names_stations:

                    fig7xx          = plot_ts(df_merged, vv, station, colors = sources_colors['i_color'],
                                              color_legend_args = doy_dist['color_legend'],
                                              fig_args = station_ts['fig'], ts_init_args = station_ts['init'],
                                              plot_args = station_ts['plot'])
                
                    save_png(fig7xx, f'{out_path}/png/{run}/{station}_{vv}_ts')
                    save_pdf(pdf, fig7xx)

    print('That\'s it! Cell and in-situ data was processed and saved; Figures and plots were saved. Ciao!')
    print('___________')
