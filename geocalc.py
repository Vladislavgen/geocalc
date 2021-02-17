import pandas as pd

df1 = pd.read_excel('/Users/lubava/Desktop/task geocalc/SM_CONV_Calculator_10.02.2021.xlsx', sheet_name='DATA')
df2 = pd.read_excel('/Users/lubava/Desktop/task geocalc/SM_CONV_Calculator_10.02.2021.xlsx', sheet_name='PENETRATION')
df3 = pd.read_excel('/Users/lubava/Desktop/task geocalc/SM_CONV_Calculator_10.02.2021.xlsx', sheet_name='Full_data')
print(df1.head(), df2.head(), df3.head())


def households_5_min_pca(num_5_min):
    if num_5_min < 1000:
        return '<1000'
    elif num_5_min > 3000:
        return '>3000'
    else:
        return '1000 - 3000'


def households_20_min_pca(num_20_min):
    if num_20_min < 10000:
        return '<10000'
    elif num_20_min > 40000:
        return '>40000'
    elif num_20_min in range(20000, 30000):
        return '20000 - 30000'
    elif num_20_min in range(30000, 40000):
        return '30000 - 40000'
    else:
        return '10000 - 20000'


def pedestrian_traffic(num_traffic):
    if num_traffic < 3000:
        return 'low'
    elif num_traffic > 9000:
        return 'high'
    else:
        return 'average'


def define_household(format_store):
    if format_store in small_stores:
        return household_in_10_min
    else:
        return household_in_20_min


# enter your Data
num_5_min = int(input('Enter your Households number, 5 min PCA: '))
num_10_min = int(input('Enter your Households number, 10 min PCA: '))
num_15_min = int(input('Enter your Households number, 15 min PCA: '))
num_20_min = int(input('Enter your Households number, 20 min PCA: '))
num_traffic = int(input('Enter your Pedestrian traffic: '))
format_store = input('Enter your Format: ')
region = input('Enter your Region: ')
clients_from_traffic = float(input('Enter your Clients from traffic: '))

household_in_20_min = num_5_min + num_10_min + num_15_min + num_20_min
household_in_10_min = num_5_min + num_10_min
print('HOUSEHOLDS in 20 min PCA: ', household_in_20_min)
print('HOUSEHOLDS in 10 min PCA: ', household_in_10_min)

penetr_united = '{},{},{},{}'.format(households_5_min_pca(num_5_min), households_20_min_pca(num_20_min),
                                     pedestrian_traffic(num_traffic), format_store)
penetration = df2[df2['CODE_FIN'] == penetr_united]['PENETRATION'].sum()
print('\n')
print('Penetration is:', penetration)

avg_var = '{},{}'.format(region, format_store)
avg_visit = df1[df1['CODE_Region_Format'] == avg_var]['AVG_VISIT'].sum()
avg_ticket = df1[df1['CODE_Region_Format'] == avg_var]['AVG_TICKET'].sum()
avg_num_visits = df1[df1['CODE_Region_Format'] == avg_var]['AVG_NUM_VISITS'].sum()
print('Average visit by format and region is: ', int(avg_visit))
print('Average ticket by format and region is: ', int(avg_ticket))
print('Average number of visits by format and region is: ', round(avg_num_visits, 2))

small_stores = ['SM S', 'CONV S', 'CONV M', 'CONV L']
rampup_years = 0.15
sales_forecast_2nd_year = define_household(format_store) * penetration * avg_visit * \
                          avg_num_visits * 12 + clients_from_traffic * num_traffic * avg_ticket * 365
sales_forecast_1st_year = sales_forecast_2nd_year / (1 + rampup_years)
avg_daily_num_tickets = sales_forecast_1st_year / avg_ticket / 365
print('\n')
print('Sales forecast by households criterias 1st Year: ', int(sales_forecast_1st_year))
print('Sales forecast by households criterias 2nd Year: ', int(sales_forecast_2nd_year))
print('Average daily number of tickets in 1st year: ', int(avg_daily_num_tickets))
