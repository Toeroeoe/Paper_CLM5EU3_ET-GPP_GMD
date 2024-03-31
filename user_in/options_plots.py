

EU3_maps = {
            
            'base': {
                'rotnpole_lat': 39.25,
                'rotnpole_lon': -162.0,
                'semmj_axis': 6370000, 
                'semmn_axis': 6370000, 
                'lon_extents': [351, 58], 
                'lat_extents': [26, 65.5],
            },

            'lines': {
                'xticks': [-20, 0, 20, 40],
                'yticks': [20, 40, 60],
                'lw_grid': 0.95,
                'lw_coast': 0.95,
                'ls_grid': '--',
                'color_grid': 'grey',
                'fs_label': 12,
            },

            'locations_map': {
                'size_marker': 50,
                'marker': 'x',
                'color_marker': 'firebrick',
                'alpha': 0.9,
                'zorder': 5,
            },

            'lc_markers': {
                    'ENF': 'o', 
                    'DBF': '^', 
                    'GRA': 's', 
                    'CRO': 'P'},

            'diff_maps': {
                'cmap': 'coolwarm_r',
                'cmap_n': 1000,
                'extend': 'both',
                'clabel': '%',
                'fs_title': 12,
                'fs_subtitle': 10,
                'fs_cbar_label': 10,
            },

            'sel_map': {
                'cmap': 'cet_glasbey_hv',
                'extend': 'neither',
                'clabel': '',
                'title': 'Dominant PFT',
                'fs_title': 12,
                'fs_cbar_label': 20,
            },

            'v_mean': {
                'v0': -20,
                'v1': 20,
            },

            'v_var': {
                'v0': -50,
                'v1': 50,
            },

            'marker_legend': {
                    'marker_color': 'gray',
                    'marker_size': 10,
                    'anchor': (0.5, 0.5), 
                    'markerfirst': True, 
                    'fs_labels': 10,
                    'labelcolor': 'k',
                    'handletextpad': 0.2,
                    'columnspacing': 0.9, 
                    'loc': 'center',
                    'handlelength': 1.2, },
            
            'long_name_var' : 'Variance',
            'long_name_mean': 'Mean',

            'long_name_ET' : 'Evapotranspiraton',
            'long_name_GPP': 'Gross Primary Production',
            
}

sources_colors = {

        'i_color': {
        'ICOS-WARMWINTER2020': 0,
        'CLM5-EU3': 1,
        'CLM5-EU3-pft': 2,
        'GLASS-EU3': 3,
        'ERA5L-EU3': 10,
        'GLEAM-EU3': 6,
        'COSMOREA6-EU3': 9,
        }
}

landcover_colors = {

    'i_color': {
        'ENF': 0,
        'DBF': 1,
        'GRA': 2,
        'CRO': 3,
        }

}


land_cover_moments = {
    
    'markers' : {
        'ENF': 'o', 
        'DBF': '^', 
        'GRA': 's', 
        'CRO': 'P',
    },

    'i_color': {
        'ICOS-WARMWINTER2020': 0,
        'CLM5-EU3': 1,
        'CLM5-EU3-pft': 2,
        'GLASS-EU3': 3,
        'ERA5L-EU3': 4,
        'GLEAM-EU3': 6,
    },

    'init_xy': {
        'axhv_color': 'k',
        'axhv_ls': '--',
        'axhv_lw': 1,
        'axhv_dashes': (4, 4),
        'diag_color': 'k',
        'diag_ls': '--',
        'diag_lw': 0.7,
        'fs_title': 14,
        'y_title': 1.05,
        'fs_label': 12,
        'fs_ticks': 10,
        'ax_tag_x': 0.5,
        'ax_tag_y': 0.95,
    },

    'xy': {
        'sizes_marker': 60,
        'alpha': 0.75,
    },

    'marker_legend': {
        'marker_color': 'gray',
        'marker_size': 10,
        'anchor': (0.5, 0.5), 
        'markerfirst': True, 
        'fs_labels': 10,
        'labelcolor': 'k',
        'handletextpad': 0.2,
        'columnspacing': 0.9, 
        'loc': 'center',
        'handlelength': 1.2,
    },

    'color_legend': {
        'anchor': (0.5, 0.5), 
        'markerfirst': True, 
        'fs_labels': 10,
        'handletextpad': 0.35,
        'columnspacing': 0.9, 
        'loc': 'center',
        'handlelength': 1.0,
    },
}

rmse_landcover = {

    'init_bar': {
        'axhv_color': 'k',
        'axhv_ls': '--',
        'axhv_lw': 1,
        'axhv_dashes': (4, 4),
        'fs_title': 14,
        'y_title': 1.05,
        'fs_label': 12,
        'fs_ticks': 10,
        'ax_tag_x': 0.5,
        'ax_tag_y': 0.93,
    },

    'bars': {
        'alpha': 0.7,
    },

    'color_legend': {
        'anchor': (0.5, 0.5), 
        'markerfirst': True, 
        'fs_labels': 10,
        'handletextpad': 0.35,
        'columnspacing': 0.9, 
        'loc': 'center',
        'handlelength': 1.0,
        'nrows': 1 
    },
}


doy_dist = {

    'init_doy': {
        #'axhv_color': 'dimgray',
        'axhv_ls': '--',
        'axhv_lw': 1,
        'axhv_dashes': (4, 4),
        'fs_title': 14,
        'y_title': 1.05,
        'fs_label': 10,
        'fs_ticks': 10,
        'ax_tag_x': 0.15,
        'ax_tag_y': 0.93,
        'xlabel': 'Day of year'
    },

    'init_dist': {
        #'axhv_color': 'k',
        'axhv_ls': '--',
        'axhv_lw': 1,
        'axhv_dashes': (4, 4),
        'fs_title': 14,
        'y_title': 1.05,
        'fs_label': 10,
        'fs_ticks': 10,
        'ax_tag_x': 0.15,
        'ax_tag_y': 0.93,
        'ylabel': 'Probability density'
    },

    'doy': {
        'alpha': 0.8,
        'lw': 2.6,
    },

    'doy_fill_args': {
        'alpha': 0.2,
    },

    'dist': {
        'alpha': 0.8,
        'lw': 3,
    },

    'color_legend': {
        'anchor': (0.5, 0.5), 
        'markerfirst': True, 
        'fs_labels': 10,
        'handletextpad': 0.35,
        'columnspacing': 0.9, 
        'loc': 'center',
        'handlelength': 1.0,
        'nrows': 1 
    },
}

pie_landcover = {
    'color_legend': {
        'anchor': (0.5, 0.5), 
        'markerfirst': True, 
        'fs_labels': 10,
        'handletextpad': 0.35,
        'columnspacing': 0.9, 
        'loc': 'center',
        'handlelength': 1.0,
        'nrows': 1 ,
    },
}

station_ts = {
    
    'fig': {
        'fx': 6.7,
        'fy': 3.5,
    },

    'init': {
        'y_title': 1.0,
    },

    'plot': {
        'style': '-',
        'lw': 1.5,
        'alpha': 0.75,
        'markersize': 3,
        'marker': 'o'
    }
    }