#national forest service data
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

nf = pd.read_csv('/Users/theloniuspunk/Desktop/Grows/grows.csv')

file = '/Users/theloniuspunk/Desktop/Grows/NFS_MJ.xlsx'
data = pd.ExcelFile(file)
sheets = data.sheet_names
joined = []
for sheet in sheets:
    each_year = pd.read_excel(data, sheet_name=sheet)
    year = sheet.split('Y')
    each_year['year'] = '20' + year[1]
    joined.append(each_year)

grows = pd.concat(joined).reset_index()
grows.rename(columns={
    'REGION': 'region',
    'FOREST': 'forest_number',
    'FOREST NAME': 'name',
    'MJ PLANTS (EA)': 'number_plants',
    'PROCESSED MJ (LBS)': 'pounds_processed',
    'Year': 'year'
}, inplace=True)

#new grows with relevant columns
grows = grows[['name', 'number_plants', 'pounds_processed', 'year']]

# rename columns
nf.rename(columns={
    'REGION': 'region',
    'FOREST': 'forest_number',
    'FOREST NAME': 'name',
    'MJ PLANTS (EA)': 'number_plants',
    'PROCESSED MJ (LBS)': 'pounds_processed',
    'Year': 'year'
}, inplace=True)


# dictionary with names of states according to names of national forests
parks = {"RIO GRANDE N F": "colorado", "NEZ PERCE-CLEARWATER": "idaho", "KISATCHIE N F": "louisiana",
         "LINCOLN N F": "new mexico", "SUPERIOR N F": "minnesota", "OLYMPIC N F": 'washington',
         "MIDEWIN TALLGRASS PRA": "illinois", "CUSTER GALLATIN": "montana",
         "NFS IN MISSISSIPPI": "mississippi", "WHITE MOUNTAIN N F": "new hampshire/maine",
         "SALMON-CHALLIS N F": "idaho", "NEBRASKA N F": "nebraska", "BITTERROOT N F": "montana/idaho",
         "MT BAKER-SNOQUALMIE": "washington", "FLATHEAD N F": "montana", "BLACK HILLS N F": "south dakota/wyoming",
         "CIBOLA N F": "new mexico", "TONGASS NF": "alaska", "SAN JUAN N F": "colorado",
         "GIFFORD PINCHOT N F": "washington", "GREEN MOUNTAIN N F": "vermont", "CORONADO N F": "arizona",
         "ALLEGHENY N F": "pennsylvania", "PAYETTE N F": "idaho", "HIAWATHA N F": "michigan", "ROUTT N F": "colorado",
         "COLVILLE N F": "washington", "CARSON N F": "new mexico", "SHAWNEE N F": "illinois",
         "NFS IN FLORIDA": "florida",
         "MONONGAHELA N F": "west virginia", "GILA N F": "new mexico", "FRANCIS MARION&SUMTER": "south carolina",
         "OZARK ST FRANCIS N F": "arkansas", "IDAHO PANHANDLE N F": "idaho",
         "CLEARWATER N F": "idaho", "CHIPPEWA N F": "minnesota", "DESCHUTES N F": "oregon",
         "MARK TWAIN N F": "missouri",
         "OUACHITA N F": "arkansas", "SANTA FE N F": "new mexico", "HURON MANISTEE N F": "michigan",
         "KAIBAB N F": "arizona", "OTTAWA N F": "michigan", "GUNNISON-GM-UNC N F": "colorado", "WAYNE  N F": "ohio",
         "LOLO N F": "montana", "FREMONT N F": "oregon", "HOOSIER N F": "indiana", "UMPQUA N F": "oregon",
         "ARAPAHO-ROOSEVELT N F": "colorado", "WHITE RIVER N F": "colorado", "WILLAMETTE N F": "oregon",
         "OCHOCO N F": "oregon", "MALHEUR N F": "oregon", "NFS IN ALABAMA": "alabama", "GW & JEFFERSON N F": "virginia",
         "MT HOOD N F": "oregon", "PRESCOTT N F": "arizona", "UINTA-WASATCH-CACHE": "utah", "SIUSLAW N F": "oregon",
         "COCONINO N F": "arizona", "MANTI LASAL N F": "colorado/utah", "OKANOGAN N F": "washington",
         "CHATTAHOOCHEE-OCONEE": "georgia", "NFS IN TEXAS": "texas", "SAWTOOTH N F": "idaho",
         "NFS IN NORTH CAROLINA": "north carolina", "COLUMBIA RIVER GORGE": "oregon", "FISHLAKE N F": "utah",
         "BOISE N F": "idaho", "CHEQUAMEGON-NICOLET": "wisconsin", "MODOC N F": "california",
         "ROGUE RIVER-SISKIYOU": "california/oregon", "UMATILLA N F": "oregon",
         "HUMBOLDT-TOIYABE N F": "california/nevada", "WALLOWA WHITMAN N F": "oregon/idaho",
         "PIKE-SAN ISABEL N F": "colorado", "ELDORADO N F": "california",
         "DIXIE N F": "utah", "INYO N F": "california", "WENATCHEE N F": "washington", "TONTO NF": "arizona",
         "TAHOE N F": "california", "CHEROKEE N F": "tennessee", "LASSEN N F": "california",
         "DANIEL BOONE N F": "kentucky", "PLUMAS N F": "california", "CLEVELAND N F": "california",
         "SIX RIVERS N F": "california", "KLAMATH N F": "california", "STANISLAUS N F": "california",
         "SIERRA N F": "california", "ANGELES N F": "california", "SAN BERNARDINO N F": "california",
         "SAN BERNARDINO N F": "california", "LOS PADRES N F": "california", "MENDOCINO N F": "california",
         "SEQUOIA N F": "california", "SHASTA TRINITY N F": "california", "LAKE TAHOE BASIN M U": "california",
         "APACHE-SITGREAVES N F": "arizona/new mexico", "LAND BETWEEN THE LAKE": "kentucky", "CHUGACH NF": "alaska",
         "KOOTENAI N F": "montana", "ASHLEY N F": "utah/wyoming", "WINEMA N F": "oregon",
         "BEAVERHEAD-DEERLODGE": "montana", "CARIBOU-TARGHEE N F": "idaho", }

# mapping the key value pairs to make a new column state
grows['state'] = grows['name'].map(parks)

# checking for nan values in new state column
nan.value_counts()

# identify where nan values are
grows[grows.state.isnull()]

# setting other quantitative variables with nan to 0
nf.fillna(0, inplace=True)
grows.fillna(0, inplace=True)

# aggregating plants and pounds_processed based on estimates on plant yield
nf['pounds_est'] = nf.apply(lambda row: (row.number_plants * 1.1) + row.pounds_processed, axis=1)
grows['pounds_est'] = grows.apply(lambda row: (row.number_plants * 1.1) + row.pounds_processed, axis=1)

# changing pounds_est column to integer value
nf['pounds_est'] = nf.pounds_est.astype(int)
grows['pounds_est'] = grows.pounds_est.astype(int)

# split rows where there are two states and create new rows where the states are now separate
split_state = nf.state.str.split("/").apply(pd.Series, 1).stack()
split_state.index = split_state.index.droplevel(-1)
split_state.name = 'state'
del nf['state']
nf = nf.join(split_state)

split_s = grows.state.str.split("/").apply(pd.Series, 1).stack()
split_s.index = split_s.index.droplevel(-1)
split_s.name = 'state'
del grows['state']
grows = grows.join(split_s)

# cleaning up names in dataset
nf['name'] = nf['name'].str.lower()
nf['name'] = nf['name'].apply(lambda x: x.split(" "))
nf['name'] = nf['name'].apply(lambda x: " ".join(x[0:-2]) if x[-1] == 'f' and x[-2] == 'n' else (
"".join(x[0:-1]) if x[-1] == 'nf' else " ".join(x)))

grows['name'] = grows['name'].str.lower()
grows['name'] = grows['name'].apply(lambda x: x.split(" "))
grows['name'] = grows['name'].apply(lambda x: " ".join(x[0:-2]) if x[-1] == 'f' and x[-2] == 'n' else (
"".join(x[0:-1]) if x[-1] == 'nf' else " ".join(x)))

# exploring the data and looking for stories -- looking to see if there are any trends in eradication numbers for states where marijuana was legalized
legal_states = ['california', 'oregon', 'washington', 'colorado', 'nevada']
legal = grows[grows.state.isin(legal_states)]
legal_years = legal.pivot_table(index='year', columns='state', values='number_plants', aggfunc='sum')

cali = legal_years.loc[:, 'california']
oregon = legal_years.loc[:, 'oregon']
was = legal_years.loc[:, 'washington']
colo = legal_years.loc[:, 'colorado']

plt.plot(cali)
plt.show()

plt.plot(oregon)
plt.show()

plt.plot(was)
plt.show()

plt.plot(colo)
plt.show()

legal.groupby('state').pounds_est.sum().sort_values(ascending=False)

print(grows.dtypes)
grows['year'] = grows['year'].astype(int)
cali = grows[(grows.state == 'california') & (grows.year >= 2015)]
cali = cali.groupby(['name', 'year']).pounds_est.sum().reset_index()

ca = grows[grows['state']=='california']
# cali = ca.groupby('year').pounds_est.sum()
plt.plot(cali)
plt.show()

ore = grows[grows['state']=='oregon']
ore = ore.groupby('year').pounds_est.sum()
plt.plot(ore)
plt.show()

colo = grows[grows['state'] == 'colorado']
col = colo.groupby('year').pounds_est.sum()

plt.plot(col)
plt.show()

was = grows[grows['state']=='washington']
was = was.groupby('year').pounds_est.sum()
plt.plot(was)
plt.show()

cali = cali.groupby('year').pounds_est.sum().reset_index()

cali[cali.year==2017]

ten = grows[grows.state == 'kentucky']
ten.groupby('year').number_plants.sum().sort_values(ascending=False)

totals = grows.groupby('year').number_plants.sum()
plt.rcParams['figure.figsize'] = (20, 10)
plt.plot(totals)
plt.rcParams['figure.figsize'] = (20, 10)
plt.show()

illeg = grows[(grows.state != 'maine') & (grows.state != 'vermont') & (grows.state != 'california') & (grows.state != 'washington') & (grows.state != 'oregon') & (grows.state != 'nevada') & (grows.state != 'colorado')]
illeg = illeg.groupby('year').number_plants.sum()
plt.plot(illeg)
plt.show()

leg = grows[(grows.state == 'colorado') | (grows.state == 'washington') | (grows.state == 'oregon')].groupby('year').number_plants.sum()
plt.plot(leg)
plt.show()
legit = grows[(grows.state == 'colorado') | (grows.state == 'washington') | (grows.state == 'oregon')]
legit


#adding in new data from the national forest service
totals.loc[2018] = 700000

totals.sort_values(ascending=True)
ca = grows[grows.state == 'california'].groupby('year').number_plants.sum().sort_values(ascending=False)
ca.loc[2018] = 600000
ca.sort_values(ascending=True)
legal_years

was = grows[grows.state == 'colorado'].groupby('year').number_plants.sum()
was

grows[grows.name == 'shasta trinity'].groupby('year').number_plants.sum().sort_values(ascending=False)

print('mean', (grows[grows.state == 'california'].number_plants.sum() / 17))

grows.state.nunique()

grows.groupby('name').number_plants.sum().sort_values(ascending=False)

# making csv for line chart showing grows in California over time
ca = grows[grows.state == 'california'].groupby('year').number_plants.sum().sort_values(ascending=False)

# adding forest service estimations for 2018 -- unofficial data they have collected
ca.loc[2018] = 700000
ca = ca.reset_index()
ca['year'] = ca.year.astype(int)
ca.dtypes
ca.sort_values('year', ascending=True)
ca.to_csv('/Users/theloniuspunk/Desktop/Grows/total_ca_line.csv', index=False)

#merging national park land data derived from FOIA request with national forest service data
import pandas as pd
nps = pd.read_csv('/Users/theloniuspunk/Desktop/Grows/national_park_land.csv')
nps = pd.melt(nps, id_vars =['Name', 'State'], var_name = 'year', value_name = 'plants')
nps.columns = nps.columns.str.lower()
nps.name = nps.name.str.lower()
nps.rename(columns = {
    'plants':'plants_eradicated'
}, inplace=True)
nps

merged = pd.concat([grows, nps], axis=0)
public = merged[['name', 'number_plants', 'plants_eradicated', 'state', 'year']]
public.fillna(0, inplace=True)
public['plants'] = public.number_plants + public.plants_eradicated

#making csv for horizontal bar chart viz
total = public.groupby('state').plants.sum().sort_values(ascending=False).reset_index()
total['plants'] = total.plants.astype(int)
total.to_csv('/Users/theloniuspunk/Desktop/Grows/total_public_states.csv', index = False)


# DEA data on eradication efforts
file = '/Users/theloniuspunk/Desktop/Grows/dea_erad.xlsx'
data = pd.ExcelFile(file)
sheets = data.sheet_names
sheets
joined = []
for sheet in sheets:
    each_year = pd.read_excel(data, sheet_name=sheet)
    stripped = each_year.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
    stripped.fillna(0, inplace=True)
    stripped.iloc[:, 1:] = stripped.iloc[:, 1:].astype(int)
    joined.append(stripped)

dea = pd.concat(joined)
pd.set_option('display.max_rows', 500)

sheet
one = pd.read_excel(data, sheet_name='2001')
one = one.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
one.fillna(0, inplace=True)
one.iloc[:, 1:] = one.iloc[:, 1:].astype(int)
two = pd.read_excel(data, sheet_name='2002')
print(dea.columns)
total = dea.groupby('year')['outdoor cultivated plants eradicated'].sum()
plt.plot(total)
plt.show()

states = dea.groupby(['State', 'year'])['outdoor cultivated plants eradicated'].sum().reset_index()
cali = states[states['State'] == 'California'].groupby('year')['outdoor cultivated plants eradicated'].sum()
plt.plot(kent)
plt.show()

# getting the total numbers of outdoor grows eradicated as part of the DEA program, which estimates that 80% of their outdoor eradication was on public lands
dea[dea['State'] == 'California'].groupby('year')['outdoor plots eradicated'].sum() * .8


#organizing the UNODC data to use in the third article around the rise of far-right nationalists and the war on drugs
import pandas as pd
import matplotlib.pyplot as plt
#getting the data for opium and coca cultivation as well as drug consumption
opium = pd.read_csv("/Users/theloniuspunk/Desktop/Grows/opium_poppy_cult.csv")
opium = pd.melt(opium)
opium.rename(columns = {
    'variable':'year',
    'value':'hectares'
},inplace=True)
opium.to_csv('/Users/theloniuspunk/Desktop/Grows/poppy_cult.csv')
opium.set_index('year', inplace=True)
plt.plot(opium)
plt.show()

coca = pd.read_csv("/Users/theloniuspunk/Desktop/Grows/coca_cult_hect.csv")
coca = pd.melt(coca)
coca.rename(columns = {
    'variable':'year',
    'value':'hectares'
},inplace=True)
coca.to_csv('/Users/theloniuspunk/Desktop/Grows/coca_cult.csv')
coca.set_index('year', inplace=True)
plt.plot(coca)
plt.show()

use = pd.read_csv("/Users/theloniuspunk/Desktop/Grows/drug_use_intl.csv")
use.to_csv('/Users/theloniuspunk/Desktop/Grows/drug_use.csv')
use.set_index('year', inplace=True)
plt.plot(use)
plt.show()


#permits granted to marijuana operators in california
import pandas as pd
perm = pd.read_csv("/Users/theloniuspunk/Desktop/Grows/permits_orig.csv")
perm = perm[['Legal Business Name','Premises County','Type of License', 'License Status']]
perm.rename(columns={
    'Legal Business Name':'business',
    'Premises County':'county',
    'Type of License':'type',
    'License Status':'status'
}, inplace=True)
perm.groupby('county')['type'].value_counts()

def size(row):
    if row.type == 'Small Outdoor' or row.type == 'Small Mixed-Light Tier 1' or row.type == 'Specialty Indoor' or row.type == 'Small Mixed-Light Tier 2' or row.type == 'Specialty Outdoor' or row.type == 'Small Indoor' or row.type == 'Specialty Mixed-Light Tier 1' or row.type == 'Specialty Mixed-Light Tier 2':
        val = 'small'
    elif row.type =='Specialty Cottage Mixed-Light Tier 1' or row.type == 'Specialty Cottage Indoor' or row.type == 'Specialty Cottage Outdoor' or row.type == 'Specialty Cottage Mixed-Light Tier 2':
        val = 'cottage'
    elif row.type == 'Medium Indoor' or row.type == 'Medium Outdoor' or row.type == 'Medium Mixed-Light Tier 1' or row.type == 'Medium Mixed-Light Tier 2':
        val ='medium'
    else:
        val = row.type
    return val

#data exploration
perm['size'] = perm.apply(size, axis=1)
perm.groupby('county')['size'].value_counts()

perm = perm.dropna()
# print(perm.business.value_counts().sort_values(ascending=False))

#big holders of permits in santa barbara
#big holders of permits in santa barbara
iron = perm[perm.business =='Iron Angel II, LLC']
central = perm[perm.business == 'Central Coast Ag Farming, LLC']
organic = perm[perm.business == 'Organic Green Farms']
eight = perm[perm.business == '805 Agricultural Holdings']
alliance = perm[perm.business == 'Alliance Farms']
slo = perm[perm.business == 'SLO Cultivation, Inc. (dba Cresco California)']
ag = perm[perm.business == 'Ag Roots LLC']
thc = perm[perm.business == 'THC Farms']
heirloom = perm[perm.business == 'Lakeview Organics']
lake = perm[perm.business == 'Lakeview Organics']
canna = perm[perm.business == 'Canna Rios LLC']
power = perm[perm.business == 'Power Farms LLC']



#just getting permits that are active, i.e. still valid
big = perm[perm.status == 'Active']
permits = big.county.value_counts(ascending=False).reset_index().rename(columns = {
    'index':'county',
    'county':'permits',
})

def clean(row):
    county = row.county.split()
    del county[-1]
    new = " ".join(county)
    return new

permits['county'] = permits.apply(clean, axis=1)

#totals for counties
permits.to_csv("/Users/theloniuspunk/Desktop/Grows/permits.csv", index=False)

permits.head(10).to_csv("/Users/theloniuspunk/Desktop/Grows/top_ten_permits.csv", index=False)

permits.head(10)

permits.head()

bigd = perm[(perm.county == 'Santa Barbara County') | (perm.county == 'Humboldt County') | (perm.county == 'Mendocino County') | (perm.county == 'Monterey County') | (perm.county == 'Trinity County')]

bigd['business'].value_counts().head(15)

#humboldt
honey = perm[perm.business == 'Honeydew Farms LLC']

#monterey
flr = perm[perm.business == 'FLRish Farms Cultivation 2, LLC']

#humboldt
inno = perm[perm.business == 'Innovation West DBA Panther Gap Farms']

data = bigd['business'].value_counts().head(15).reset_index()
data.rename(columns={
    'index':'company'
}, inplace=True)
data.to_csv('/Users/theloniuspunk/Desktop/Grows/top_holders.csv', index=False)