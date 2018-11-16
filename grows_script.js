import pandas as pd
df = pd.read_csv("/Users/digital/Documents/Illegal marijuana grows/m_grows.csv")
df['FOREST NAME'].value_counts()

plants = df.dropna(subset=['MJ PLANTS (EA)'])
names = plants['FOREST NAME'].unique()
plants = plants.set_index('FOREST NAME')
pd.set_option('display.max_rows', 500)

legal = df
legal.drop(legal.columns[[0, 1, 4]], axis=1, inplace=True)
legal = legal.dropna(subset=['MJ PLANTS (EA)'])

forests = legal

# def legal_states():
#     legal = []
#     for x in names: 
#         name = x 
        
        
#all the parks together with states
values = []
for x in names:
    name = x
    number = plants.loc[name, 'MJ PLANTS (EA)'].sum()
    newlist = (x, number)
    values.append(newlist)
values 
new = pd.DataFrame(values, columns=['Forest', 'plants'])

new.groupby('plants').max()['Forest']


parks = {"RIO GRANDE N F":"colorado", "NEZ PERCE-CLEARWATER":"idaho", "KISATCHIE N F":"louisiana", "LINCOLN N F":"new mexico", "SUPERIOR N F":"minnesota", "OLYMPIC N F":'washington', "MIDEWIN TALLGRASS PRA":"illinois", "CUSTER GALLATIN":"montana", "NFS IN MISSISSIPPI":"mississippi", "WHITE MOUNTAIN N F":"new hampshire/maine",
        "SALMON-CHALLIS N F":"idaho", "NEBRASKA N F":"nebraska", "BITTERROOT N F":"montana/idaho", "MT BAKER-SNOQUALMIE":"washington", "FLATHEAD N F":"montana", "BLACK HILLS N F":"south dakota/wyoming", "CIBOLA N F": "new mexico", "TONGASS NF": "alaska", "SAN JUAN N F":"colorado", "GIFFORD PINCHOT N F":"washington", "GREEN MOUNTAIN N F":"vermont", "CORONADO N F":"arizona",
         "ALLEGHENY N F": "pennsylvania", "PAYETTE N F": "idaho", "HIAWATHA N F": "michigan", "ROUTT N F": "colorado", "COLVILLE N F":"washington", "CARSON N F":"new mexico", "SHAWNEE N F":"illinois", "NFS IN FLORIDA": "florida", "MONONGAHELA N F":"west virginia", "GILA N F":"new mexico", "FRANCIS MARION&SUMTER":"south carolina", "OZARK ST FRANCIS N F":"arkansas", "IDAHO PANHANDLE N F":"idaho",
         "CLEARWATER N F":"idaho", "CHIPPEWA N F":"minnesota", "DESCHUTES N F":"oregon", "MARK TWAIN N F":"missouri", "OUACHITA N F":"arkansas", "SANTA FE N F":"new mexico", "HURON MANISTEE N F":"michigan", "KAIBAB N F": "arizona", "OTTAWA N F":"michigan", "GUNNISON-GM-UNC N F":"colorado", "WAYNE  N F":"ohio", "LOLO N F":"montana", "FREMONT N F":"oregon", "HOOSIER N F":"indiana", "UMPQUA N F":"oregon",
         "ARAPAHO-ROOSEVELT N F":"colorado", "WHITE RIVER N F":"colorado", "WILLAMETTE N F":"oregon", "OCHOCO N F":"oregon", "MALHEUR N F":"oregon", "NFS IN ALABAMA":"alabama", "GW & JEFFERSON N F":"virginia", "MT HOOD N F":"oregon", "PRESCOTT N F":"arizona", "UINTA-WASATCH-CACHE":"utah", "SIUSLAW N F":"oregon", "COCONINO N F":"arizona", "MANTI LASAL N F":"colorado/utah", "OKANOGAN N F":"washington", "CHATTAHOOCHEE-OCONEE":"georgia",
         "NFS IN TEXAS":"texas", "SAWTOOTH N F":"idaho", "NFS IN NORTH CAROLINA":"north carolina", "COLUMBIA RIVER GORGE":"oregon", "FISHLAKE N F":"utah", "BOISE N F":"idaho", "CHEQUAMEGON-NICOLET":"wisconsin", "MODOC N F":"california", "ROGUE RIVER-SISKIYOU":"california/oregon", "UMATILLA N F":"oregon", "HUMBOLDT-TOIYABE N F":"california/nevada", "WALLOWA WHITMAN N F":"oregon/idaho", "PIKE-SAN ISABEL N F":"colorado", "ELDORADO N F":"california",
         "DIXIE N F":"utah", "INYO N F":"california", "WENATCHEE N F":"washington", "TONTO NF":"arizona", "TAHOE N F":"california", "CHEROKEE N F":"tennessee", "LASSEN N F":"california", "DANIEL BOONE N F":"kentucky", "PLUMAS N F":"california", "CLEVELAND N F":"california", "SIX RIVERS N F":"california", "KLAMATH N F":"california", "STANISLAUS N F":"california", "SIERRA N F":"california", "ANGELES N F":"california", "SAN BERNARDINO N F":"california",
         "SAN BERNARDINO N F":"california", "LOS PADRES N F":"california", "MENDOCINO N F":"california", "SEQUOIA N F":"california", "SHASTA TRINITY N F":"california", "LAKE TAHOE BASIN M U":"california", "APACHE-SITGREAVES N F":"arizona/new mexico", "LAND BETWEEN THE LAKE":"kentucky", "CHUGACH NF":"alaska", "KOOTENAI N F":"montana"}
parks["SALMON-CHALLIS N F"]


new['state'] = new['Forest'].map(parks)
new = new.set_index("state")
new = new.reset_index()


s = new.state.str.split("/").apply(pd.Series, 1).stack()
s.index = s.index.droplevel(-1)
s.name = 'state'
del new['state']

joined = new.join(s)

a = joined.groupby('state')['plants'].sum().sort_values(ascending=False).to_dict()

df1 = pd.DataFrame(list(a.items()), columns=['state', 'plants'])
# df1.to_csv("/Users/digital/Documents/Illegal marijuana grows/plants.csv", index=None)

legal['state'] = legal['FOREST NAME'].map(parks)
legal = legal[(legal['state'] == 'california') | (legal['state'] == 'oregon') | (legal['state'] == 'colorado')]
ca = legal[legal['state'] == 'california']

def cali(var):
    names = var['FOREST NAME'].unique()
    values =[]
    var = var.set_index("FOREST NAME")
    for x in names:
        number = var.loc[x, 'MJ PLANTS (EA)'].sum()
        new = (x, number)
        values.append(new)
    return pd.DataFrame(values, columns=['Forest', 'plants'])

totals_ca = cali(ca)
totals_ca.sort_values(by=['plants'], ascending=False)

forests.columns = ['Name', 'plants', 'years', 'state']
forests

import pandas as pd
df = pd.read_csv("/Users/digital/Documents/Illegal marijuana grows/m_grows.csv")
df['FOREST NAME'].value_counts()

plants = df.dropna(subset=['MJ PLANTS (EA)'])
names = plants['FOREST NAME'].unique()
plants = plants.set_index('FOREST NAME')
pd.set_option('display.max_rows', 500)

legal = df
legal.drop(legal.columns[[0, 1, 4]], axis=1, inplace=True)
legal = legal.dropna(subset=['MJ PLANTS (EA)'])

forests = legal

# def legal_states():
#     legal = []
#     for x in names: 
#         name = x 
        
        
#all the parks together with states
values = []
for x in names:
    name = x
    number = plants.loc[name, 'MJ PLANTS (EA)'].sum()
    newlist = (x, number)
    values.append(newlist)
values 
new = pd.DataFrame(values, columns=['Forest', 'plants'])

new.groupby('plants').max()['Forest']


parks = {"RIO GRANDE N F":"colorado", "NEZ PERCE-CLEARWATER":"idaho", "KISATCHIE N F":"louisiana", "LINCOLN N F":"new mexico", "SUPERIOR N F":"minnesota", "OLYMPIC N F":'washington', "MIDEWIN TALLGRASS PRA":"illinois", "CUSTER GALLATIN":"montana", "NFS IN MISSISSIPPI":"mississippi", "WHITE MOUNTAIN N F":"new hampshire/maine",
        "SALMON-CHALLIS N F":"idaho", "NEBRASKA N F":"nebraska", "BITTERROOT N F":"montana/idaho", "MT BAKER-SNOQUALMIE":"washington", "FLATHEAD N F":"montana", "BLACK HILLS N F":"south dakota/wyoming", "CIBOLA N F": "new mexico", "TONGASS NF": "alaska", "SAN JUAN N F":"colorado", "GIFFORD PINCHOT N F":"washington", "GREEN MOUNTAIN N F":"vermont", "CORONADO N F":"arizona",
         "ALLEGHENY N F": "pennsylvania", "PAYETTE N F": "idaho", "HIAWATHA N F": "michigan", "ROUTT N F": "colorado", "COLVILLE N F":"washington", "CARSON N F":"new mexico", "SHAWNEE N F":"illinois", "NFS IN FLORIDA": "florida", "MONONGAHELA N F":"west virginia", "GILA N F":"new mexico", "FRANCIS MARION&SUMTER":"south carolina", "OZARK ST FRANCIS N F":"arkansas", "IDAHO PANHANDLE N F":"idaho",
         "CLEARWATER N F":"idaho", "CHIPPEWA N F":"minnesota", "DESCHUTES N F":"oregon", "MARK TWAIN N F":"missouri", "OUACHITA N F":"arkansas", "SANTA FE N F":"new mexico", "HURON MANISTEE N F":"michigan", "KAIBAB N F": "arizona", "OTTAWA N F":"michigan", "GUNNISON-GM-UNC N F":"colorado", "WAYNE  N F":"ohio", "LOLO N F":"montana", "FREMONT N F":"oregon", "HOOSIER N F":"indiana", "UMPQUA N F":"oregon",
         "ARAPAHO-ROOSEVELT N F":"colorado", "WHITE RIVER N F":"colorado", "WILLAMETTE N F":"oregon", "OCHOCO N F":"oregon", "MALHEUR N F":"oregon", "NFS IN ALABAMA":"alabama", "GW & JEFFERSON N F":"virginia", "MT HOOD N F":"oregon", "PRESCOTT N F":"arizona", "UINTA-WASATCH-CACHE":"utah", "SIUSLAW N F":"oregon", "COCONINO N F":"arizona", "MANTI LASAL N F":"colorado/utah", "OKANOGAN N F":"washington", "CHATTAHOOCHEE-OCONEE":"georgia",
         "NFS IN TEXAS":"texas", "SAWTOOTH N F":"idaho", "NFS IN NORTH CAROLINA":"north carolina", "COLUMBIA RIVER GORGE":"oregon", "FISHLAKE N F":"utah", "BOISE N F":"idaho", "CHEQUAMEGON-NICOLET":"wisconsin", "MODOC N F":"california", "ROGUE RIVER-SISKIYOU":"california/oregon", "UMATILLA N F":"oregon", "HUMBOLDT-TOIYABE N F":"california/nevada", "WALLOWA WHITMAN N F":"oregon/idaho", "PIKE-SAN ISABEL N F":"colorado", "ELDORADO N F":"california",
         "DIXIE N F":"utah", "INYO N F":"california", "WENATCHEE N F":"washington", "TONTO NF":"arizona", "TAHOE N F":"california", "CHEROKEE N F":"tennessee", "LASSEN N F":"california", "DANIEL BOONE N F":"kentucky", "PLUMAS N F":"california", "CLEVELAND N F":"california", "SIX RIVERS N F":"california", "KLAMATH N F":"california", "STANISLAUS N F":"california", "SIERRA N F":"california", "ANGELES N F":"california", "SAN BERNARDINO N F":"california",
         "SAN BERNARDINO N F":"california", "LOS PADRES N F":"california", "MENDOCINO N F":"california", "SEQUOIA N F":"california", "SHASTA TRINITY N F":"california", "LAKE TAHOE BASIN M U":"california", "APACHE-SITGREAVES N F":"arizona/new mexico", "LAND BETWEEN THE LAKE":"kentucky", "CHUGACH NF":"alaska", "KOOTENAI N F":"montana"}
parks["SALMON-CHALLIS N F"]


new['state'] = new['Forest'].map(parks)
new = new.set_index("state")
new = new.reset_index()


s = new.state.str.split("/").apply(pd.Series, 1).stack()
s.index = s.index.droplevel(-1)
s.name = 'state'
del new['state']

joined = new.join(s)

a = joined.groupby('state')['plants'].sum().sort_values(ascending=False).to_dict()

df1 = pd.DataFrame(list(a.items()), columns=['state', 'plants'])
# df1.to_csv("/Users/digital/Documents/Illegal marijuana grows/plants.csv", index=None)

legal['state'] = legal['FOREST NAME'].map(parks)
legal = legal[(legal['state'] == 'california') | (legal['state'] == 'oregon') | (legal['state'] == 'colorado')]
ca = legal[legal['state'] == 'california']

def cali(var):
    names = var['FOREST NAME'].unique()
    values =[]
    var = var.set_index("FOREST NAME")
    for x in names:
        number = var.loc[x, 'MJ PLANTS (EA)'].sum()
        new = (x, number)
        values.append(new)
    return pd.DataFrame(values, columns=['Forest', 'plants'])

totals_ca = cali(ca)
totals_ca.sort_values(by=['plants'], ascending=False)

forests.columns = ['Name', 'plants', 'years', 'state']
forests


