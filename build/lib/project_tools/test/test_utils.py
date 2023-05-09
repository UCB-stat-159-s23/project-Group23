from project_tools.utils import *


def test_monthly_weekday_counts():
	Berkeley_Embarcadero_2010_2019, label = monthly_weekday_counts("BK", "EM", 2010, 2019)
	assert len(Berkeley_Embarcadero_2010_2019) == 120, "Check correct number of elements in the list"
	assert type(label[0]) == str, "Check label type"


def test_annual_arrival_count():
    output = annual_arrival_trips(year = ['2022'], station = ['EM','MT', 'PL', 'CC'])
    assert isinstance(output, pd.DataFrame)


def test_calc_stn_perc_diffs():
    output = calc_stn_perc_diffs(SF_pre_covid, SF_post_covid)
    assert isinstance(output, pd.DataFrame)

def test_add_markers_to_map():
    berk_map = folium.Map(location=[37.8715, -122.2730], tiles="cartodbpositron", zoom_start=15)
    berk_mapping_df = pd.DataFrame({
        'lon': [-122.2681, -122.2834],
        'lat': [37.8701, 37.8740],
        'name': ['Downtown Berkeley: '+str(round(berk_percent_diffs[0]))+'%',
                'North Berkeley: '+str(round(berk_percent_diffs[1]))+'%'],
        'value': berk_percent_diffs}, dtype=str)
    output = add_markers_to_map(berk_mapping_df, 6, 'teal', berk_map)
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
    