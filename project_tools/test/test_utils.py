from project_tools.utils import *


def test_monthly_weekday_counts():
	Berkeley_Embarcadero_2010_2019, label = monthly_weekday_counts("BK", "EM", 2010, 2019)
	assert len(Berkeley_Embarcadero_2010_2019) == 120, "Check correct number of elements in the list"
	assert type(label[0]) == str, "Check label type"


def test_annual_arrival_count():
    output = annual_arrival_trips(year = ['2022'], station = ['EM','MT', 'PL', 'CC'])
    assert isinstance(output, pd.DataFrame)


def test_calc_stn_perc_diffs():
    SF_2019 = annual_arrival_trips(year=['2019'], station=['BK'])
    SF_2021 = annual_arrival_trips(year=['2021'], station=['BK'])
    output = calc_stn_perc_diffs(SF_2019, SF_2021)
    assert isinstance(output, pd.core.series.Series)

def test_add_markers_to_map():
    percent_diffs = [-0.65, -0.84]
    m = folium.Map(location=[45.5152, -122.6784], tiles="cartodbpositron", zoom_start=10)
    mapping_df = pd.DataFrame({
        'lon': [-122.7053, -122.6731],
        'lat': [45.5190, 45.5227],
        'name': ['International Rose Garden: '+str(round(percent_diffs[0]))+'%',
                'Voodoo Doughnuts: '+str(round(percent_diffs[1]))+'%'],
        'value': percent_diffs}, dtype=str)
    output = add_markers_to_map(mapping_df, 6, 'teal', m)
    assert isinstance(output, folium.folium.Map)

def test_get_month_and_year():
    output1 = get_month_and_year("Ridership_202105.xlsx");
    output2 = get_month_and_year("Ridership_March2016.xlsx");
    assert (2021,5) == output1
    assert (2016,3) == output2

def test_load_data():
    output1 = load_data(2016);
    output2 = load_data(2017);
    assert isinstance(output1, pd.DataFrame)
    assert isinstance(output2, pd.DataFrame)
