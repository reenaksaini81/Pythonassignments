import pandas as pd

df = pd.read_csv('Jmeter_log1.jtl', sep=',', header=0, parse_dates=['timeStamp'],
                     usecols=['timeStamp','label','responseCode','responseMessage','failureMessage'],
                     engine='python')
df = df[df['responseMessage'] != 'OK']
print(df)

