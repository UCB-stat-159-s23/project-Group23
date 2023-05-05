import numpy as np
import pandas as pd
import calendar
import os



def monthly_weekday_counts(entry_station, exit_station, start_year, end_year):
	
	 """
	 This function generates a list that contains monthly ridership of specified entry/exit stations and start/end years timeframe. 
	 
    Parameters
    ----------
    entry_station : str
        This defines the entry_station in its two characters reference name. Ex. "EM" for Embarcadero
	exit_station : str
        This defines the exit_station in its two characters reference name. Ex. "EM" for Embarcadero
	start_year : int
        This defines the start year of the timeframe, starting from January.
	end_year : int
        This defines the end year of the timeframe, ending in December.
	
	Returns
	----------
	monthly_weekday_counts : list[double]
        This returns the monthly weekday counts.
	monthly_weekday_plot_label : list[str]
        This returns a label for the corresponding index's month in the count list. format: {year}-{two_digits_format_month}
    """
	
	
	
    monthly_weekday_counts = []
    monthly_weekday_plot_label = []

    for year in np.arange(start_year, end_year+1, 1):
        dir_path = f'Data/ridership_{year}/'
        if year <= 2017:
            for month in np.arange(1, 13, 1):
                two_digits_format_month = '{:02d}'.format(month)
                file_name = f'Ridership_{calendar.month_name[month]}{year}.xlsx'
                file_path = os.path.join(dir_path, file_name)
                monthly_weekday_counts.append(pd.read_excel(file_path, header=1, index_col=0).loc[exit_station, entry_station])
                monthly_weekday_plot_label.append(f'{year}-{two_digits_format_month}')
        else:
            for month in np.arange(1, 13, 1):
                two_digits_format_month = '{:02d}'.format(month)
                file_name = f'Ridership_{year}{two_digits_format_month}.xlsx'
                file_path = os.path.join(dir_path, file_name)
                monthly_weekday_counts.append(pd.read_excel(file_path, header=1, index_col=0).loc[exit_station, entry_station])
                monthly_weekday_plot_label.append(f'{year}-{two_digits_format_month}')
                
    return monthly_weekday_counts, monthly_weekday_plot_label