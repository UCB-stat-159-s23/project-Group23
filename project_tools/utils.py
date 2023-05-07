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

def annual_arrival_trips(year, station):
    
    '''
    This function generates a list that contains the annual arrival ridership of the given stations. 
    
    Parameters
    ----------
    year: (list of str)
        A list of the years (years after 2018)
    station: (list of str)
        A list of stations that are under interest
    
    Returns
    ----------
    Output: pandas dataframe
        dataframe of the arrival riderships given the station and years
    '''
    
    output = pd.DataFrame(columns = station)
    
    for j in range(len(year)):
        file_dir = 'Data/ridership_' + year[j] + '/'
        file_name = []
        
        for i in range(12):
            if i < 9:
                string = 'Ridership_'+year[j]+'0'+str(i+1)
            else:
                string = 'Ridership_'+year[j]+str(i+1)
            file_name.append(string)
        
            string = file_dir + file_name[i] + ".xlsx"
            temp = pd.read_excel(string, skiprows = 1)
            temp = temp.set_index('Unnamed: 0')
            output.loc[file_name[i][-6:]] = temp.loc['Entries'][station]
    
    return output


