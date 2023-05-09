from project_tools.utils import *


def test_monthly_weekday_counts():
	Berkeley_Embarcadero_2010_2019, label = monthly_weekday_counts("BK", "EM", 2010, 2019)
	assert len(Berkeley_Embarcadero_2010_2019) == 120, "Check correct number of elements in the list"
	assert type(label[0]) == str, "Check label type"


def test_annual_arrival_count():
    output = annual_arrival_trips(year = ['2022'], station = ['EM','MT', 'PL', 'CC'])
    assert isinstance(output, pd.DataFrame)