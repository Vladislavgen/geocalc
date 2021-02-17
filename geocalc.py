import pandas as pd

df1 = pd.read_excel('/Users/lubava/Desktop/task geocalc/SM_CONV_Calculator_10.02.2021.xlsx', sheet_name='DATA')
df2 = pd.read_excel('/Users/lubava/Desktop/task geocalc/SM_CONV_Calculator_10.02.2021.xlsx', sheet_name='PENETRATION')
df3 = pd.read_excel('/Users/lubava/Desktop/task geocalc/SM_CONV_Calculator_10.02.2021.xlsx', sheet_name='Full_data')
print(df1.head(), df2.head(), df3.head())


def Households_5_min_PCA(Num_5_min):
    if Num_5_min < 1000:
        return '<1000'
    elif Num_5_min > 3000:
        return '>3000'
    else:
        return '1000 - 3000'


def Households_20_min_PCA(Num_20_min):
    if Num_20_min < 10000:
        return '<10000'
    elif Num_20_min > 40000:
        return '>40000'
    elif Num_20_min in range(20000, 30000):
        return '20000 - 30000'
    elif Num_20_min in range(30000, 40000):
        return '30000 - 40000'
    else:
        return '10000 - 20000'


def Pedestrian_traffic(Num_traffic):
    if Num_traffic < 3000:
        return 'low'
    elif Num_traffic > 9000:
        return 'high'
    else:
        return 'average'


def define_household(store):
    if store in small_stores:
        return Household_in_10_min
    else:
        return Household_in_20_min


# enter your Data
Num_5_min = int(input('Enter your Households number, 5 min PCA: '))
Num_10_min = int(input('Enter your Households number, 10 min PCA: '))
Num_15_min = int(input('Enter your Households number, 15 min PCA: '))
Num_20_min = int(input('Enter your Households number, 20 min PCA: '))
Num_traffic = int(input('Enter your Pedestrian traffic: '))
Format = input('Enter your Format: ')
Region = input('Enter your Region: ')
Clients_from_traffic = float(input('Enter your Clients from traffic: '))



Household_in_20_min = Num_5_min + Num_10_min + Num_15_min + Num_20_min
Household_in_10_min = Num_5_min + Num_10_min
print('HOUSEHOLDS in 20 min PCA: ', Household_in_20_min)
print('HOUSEHOLDS in 10 min PCA: ', Household_in_10_min)


penetr_united = '{},{},{},{}'.format(Households_5_min_PCA(Num_5_min), Households_20_min_PCA(Num_20_min),
                         Pedestrian_traffic(Num_traffic), Format)
Penetration = df2[df2['CODE_FIN'] == penetr_united]['PENETRATION'].sum()
print('\n')
print('Penetration is:', Penetration)


avg_var = '{},{}'.format(Region, Format)
Avg_visit = df1[df1['CODE_Region_Format'] == avg_var]['AVG_VISIT'].sum()
Avg_ticket = df1[df1['CODE_Region_Format'] == avg_var]['AVG_TICKET'].sum()
Avg_num_visits = df1[df1['CODE_Region_Format'] == avg_var]['AVG_NUM_VISITS'].sum()
print('Average visit by format and region is: ', int(Avg_visit))
print('Average ticket by format and region is: ', int(Avg_ticket))
print('Average number of visits by format and region is: ', round(Avg_num_visits, 2))

small_stores = ['SM S', 'CONV S', 'CONV M', 'CONV L']
RampUP_years = 0.15
Sales_forecast_2nd_year = define_household(Format) * Penetration * Avg_visit *\
Avg_num_visits*12+Clients_from_traffic*Num_traffic*Avg_ticket*365
Sales_forecast_1st_year = Sales_forecast_2nd_year/(1+RampUP_years)
Avg_daily_num_tickets = Sales_forecast_1st_year/Avg_ticket/365
print('\n')
print('Sales forecast by households criterias 1st Year: ', int(Sales_forecast_1st_year))
print('Sales forecast by households criterias 2nd Year: ', int(Sales_forecast_2nd_year))
print('Average daily number of tickets in 1st year: ', int(Avg_daily_num_tickets))