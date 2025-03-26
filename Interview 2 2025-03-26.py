import pandas as pd
df = pd.read_csv('C:\\Users\\debra\\Downloads\\test_de.csv')
print(df.count())
df = df.query('is_clock_in == 1 or is_clock_out == 1')
print(df.count())
df['start_time'] = pd.to_datetime(df['start_time'])
df['end_time'] = pd.to_datetime(df['end_time'])


print(df.dtypes)
df_sorted = df.sort_values(by=['resource_id', 'start_time'], ascending=[True, True])
print(df_sorted[['date','resource_id','is_clock_in', 'is_clock_out' ,'start_time','end_time']])

result = []
curr, date, clock_in, diff, new_row = None, None, None, None, None
for row in df_sorted.itertuples():
    if row.is_clock_in == 1:
        curr = row.resource_id
        date = row.date
        clock_in = row.start_time
	
    if row.is_clock_out == 1 and clock_in is not None:
        diff = row.end_time - clock_in # time difference might not be in hours as requested
        print(diff)
        new_row = {'date':row.date, 'resource_id':row.resource_id, 'clock_in':clock_in, 'clock_out':row.end_time, 'total_hours':diff}
        result.append(new_row)
        curr, date, clock_in, diff, new_row = None, None, None, None, None


final = pd.DataFrame(result)
print(final)


