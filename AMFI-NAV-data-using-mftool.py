import pandas as pd
from mftool import Mftool
import warnings
warnings.filterwarnings('ignore')
from IPython.display import clear_output
mf = Mftool()

# Get scheme codes
scheme_codes = mf.get_scheme_codes()
scheme_code_list_main = [x for x in scheme_codes.keys()]

# Query scheme codes for mid, small and flexi cap
scheme_code_list = [k for k, v in scheme_codes.items() if 'mid' in v.lower()]
scheme_code_list = scheme_code_list+[k for k, v in scheme_codes.items() if 'flexi' in v.lower()]
scheme_code_list = scheme_code_list+[k for k, v in scheme_codes.items() if 'small' in v.lower()

def HistoricalNav(scheme_code_list, start_date, end_date):
    count = 0
    main_df = pd.DataFrame()
    for schemes in scheme_code_list:
        count=count+1
#         print('='*25)
#         print(schemes)
        data = mf.get_scheme_historical_nav_for_dates(schemes, start_date, end_date) # requesting NAV data from the api.
        df = pd.DataFrame(data['data']) 
        df['scheme_code'] = pd.Series([data['scheme_code'] for x in range(len(df.index))]) #adding Pandas Series(scheme_code) as a column in Pandas Dataframe.
        df['scheme_name'] = pd.Series([data['scheme_name'] for x in range(len(df.index))]) #adding Pandas Series(scheme_name) as a column in Pandas Dataframe.
        try:
            df = df.sort_values(by = 'date')
            main_df = main_df.append(df)
#             print("Data Fetched!")
        except:
            print('Data doesnt exist of selected date.')
#         print('='*25)
        print(str((count/len(scheme_code_list))*100)+'%')
        clear_output(wait=True)

    main_df = main_df[['scheme_code', 'scheme_name', 'date', 'nav']] #creating names of dataframe columns 
    main_df.reset_index(drop = True, inplace = True) 
    return main_df

def NAV_Data(start,end): 
    try:
        values_df = HistoricalNav(scheme_code_list = scheme_code_list[0:], start_date= start, end_date= end) #to get the data
        return values_df
    except KeyError:
        start=datetime.strptime(start, '%d-%m-%Y') - timedelta(1)
        return NAV_Data(start.strftime("%d-%m-%Y"),end)

start_date= "01-01-2023"
end_date = "08-04-2023"
values_df = NAV_Data(start_date,end_date)
values_df
values_df['datetime'] = pd.to_datetime(values_df['date'], format='%d-%m-%Y')
# get unique scheme names
schemes = values_df['scheme_name'].explode().unique()
# keep only latest records.. skip this cell if you want to keep all the records
final_df = pd.DataFrame()
for scheme in schemes:
    chunk_df = temp[temp['scheme_name']==scheme]
    chunk_df = chunk_df.sort_values(by='datetime')    
    final_df =final_df.append(chunk_df.iloc[-1], ignore_index=True)
final_df.drop(['datetime'],axis=1, inplace = True)
final_df.to_csv('MF_NAV_DATA.csv')