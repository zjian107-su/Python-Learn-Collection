import json
from pygal.maps.world import World
from country_codes import get_country_code
from pygal.style import RotateStyle, LightColorizedStyle

filename = 'gdp_json.json'
with open(filename) as f:
    gdp_data = json.load(f)
    # print(len(gdp_data))

# print(gdp_data)

cc_gdp = {}
for gdp_dict in gdp_data:
    if gdp_dict['Year'] == 2008:
        country_name = gdp_dict['Country Name']
        gdp = int(float(gdp_dict['Value']))
        code = get_country_code(country_name)
        if code:
            cc_gdp[code] = gdp
            print(country_name + ': ' + str(cc_gdp[code]))

wm_style = LightColorizedStyle  # easy on printing
wm = World(style=wm_style)
wm.title = 'GDP in 2008, by Country'
wm.add('DGP', cc_gdp)

wm.render_to_file('gdp.svg')
