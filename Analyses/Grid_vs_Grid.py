

def run():

    from my_.data_process.apply_nc import src_var_apply_nc
    from my_.files.netcdf import open_netcdf, netcdf_variables_to_array
    from my_.resources.sources import query_grids, query_static
    from my_.plot.custom import double_EU3_mesh_div_cbar, single_EU3_mesh_cat_cbar
    from my_.figures.save import save_png
    from my_.files.netcdf import netcdf_variable_to_array
    from my_.math.mapping import relative_difference
    from my_.gridded.aggregate import apply

    from my_.math.arithmetic import difference
    
    from user_in.options_plots import EU3_maps


    case_name                   = 'test1'

    sources                     = ['CLM5-EU3', 'CLM5-EU3-pft']

    grid                        = 'EU3'

    variables                   = ['GPP', 'ET']

    stats                       = ['mean', 'var']

    print('\nLoad grid lat and lon variables...')

    file_grid               = query_grids(grid, 'file')
    path_grid               = query_grids(grid, 'path')
    grid_lat                = query_grids(grid, 'var_lat')
    grid_lon                = query_grids(grid, 'var_lon')

    source_sel_4d           = 'CLM5-EU3-surf'
    var_name_sel_4d         = 'PCT_NAT_PFT'
    axis_sel_shrink         = 1
    axis_sel                = 0
    method_sel              = 'argmax'
    method_agg_4d           = 'mean'

    path_sel_4d             = query_static(source_sel_4d, 'path')
    file_sel_4d             = query_static(source_sel_4d, 'file')
    data_sel_4d             = open_netcdf(f'{path_sel_4d}/{file_sel_4d}')
    array_sel_4d            = netcdf_variable_to_array(data_sel_4d, var_name_sel_4d) 

    data_geo                = open_netcdf(f'{path_grid}/{file_grid}')
    [lat, lon]              = netcdf_variables_to_array(data_geo, variables = [grid_lat, grid_lon])

    print(f'\nPlot the delecting variable information {source_sel_4d} {var_name_sel_4d}...')

    CLM5_pft                = list(query_static('CLM5-EU3-surf', 'abbr_PFT').values())

    import numpy as np
    
    array_sel_4d_1          = netcdf_variable_to_array(data_sel_4d, 'PCT_NATVEG')
    array_sel_4d_2          = netcdf_variable_to_array(data_sel_4d, 'PCT_CROP')
    array_sel_4d_top        = netcdf_variable_to_array(data_sel_4d, 'PCT_CFT')

    array_sel_4d_F1         = array_sel_4d * array_sel_4d_1
    array_sel_4d_F2         = array_sel_4d_top * array_sel_4d_2

    array_sel_4d            = np.vstack([array_sel_4d_F1, array_sel_4d_F2])

    array_sel_4d_shrank     = apply(array_sel_4d, axis_sel, method_sel)

    plot_sel_map            = single_EU3_mesh_cat_cbar(array_sel_4d_shrank, lat, lon,
                                                        **EU3_maps['base'], **EU3_maps['lines'],
                                                        **EU3_maps['sel_map'], cbar_tick_labels = CLM5_pft)

    save_png(plot_sel_map, f'plotsel_test2')

    for stat in stats:

        src_var_apply_nc(name = case_name, sources = sources, variables = variables, 
                    array_sel_4d = array_sel_4d, method_sel = method_sel, axis_sel = axis_sel, 
                    axis_sel_shrink = axis_sel_shrink, method_agg_4d = method_agg_4d,
                    method_agg_time = stat)

        diff_arrays         = []
        
        str_file            = f'out/nc/{case_name}_*_{stat}.nc'

        data_stat           = open_netcdf(str_file)

        for var in variables:
            
            names_variables     = [f'{src}_{var}_{stat}' for src in sources]

            arrays              = netcdf_variables_to_array(data_stat, names_variables)

            diff                = relative_difference(arrays[1], arrays[0], percent = True)

            diff_arrays.append(diff)

        fig1                    = double_EU3_mesh_div_cbar(diff_arrays, lat, lon, 
                                                            title = f"Relative difference: Dominant PFT relating to Cell {EU3_maps[f'long_name_{stat}']}",
                                                            **EU3_maps['base'], **EU3_maps['lines'],
                                                            **EU3_maps['diff_maps'], **EU3_maps[f'v_{stat}'],
                                                            subtitles = variables)

        save_png(fig1, f'test2_rel_{stat}_2')









    







        

