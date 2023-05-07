from project_tools.utils import *

def test_annual_arrival_count():
    
    output = annual_arrival_trips(year = ['2022'], station = ['EM','MT', 'PL', 'CC'])
    
    assert isinstance(output, pd.DataFrame)