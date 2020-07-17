import pandas as pd
import matplotlib.dates
import matplotlib.pyplot as plt
from datetime import datetime as dt ## ADDED

#how long below 637kW

def date_function(input):
    return dt.strptime(input, '%d/%m/%Y %H:%M:%S') ## this needed a return so added that

df = pd.read_excel('Data_Import.xlsx') ## Changed as the auto parse is shit

df = df.dropna()
p = df['P_tot (kW)'].to_list()
pf = df['PF_avg'].to_list()
f = df['F_avg (Hz)'].to_list()
s = df['S_tot (kVA)'].to_list()
q = df['Q_tot (kVAr)'].to_list()

datetime = df['Date'] + " " + df['Time']
datetime = datetime.apply(date_function) ## ADDED TO CONVERT TO datetime objects

# matplotlib.pyplot.plot_date(datetime, p, fmt='k.')
# plt.xlabel('Date and Time')
# plt.ylabel('Real Power (kW)')
# plt.title('Real Power (kW) over Time')
# matplotlib.pyplot.show() ## ADDED TO SHOW PLOT

# matplotlib.pyplot.plot_date(datetime, q, fmt='r.')
# plt.xlabel('Date and Time')
# plt.ylabel('Reactive Power (kVAr)')
# plt.title('Reactive Power (kVAr) over Time')
# matplotlib.pyplot.show() ## ADDED TO SHOW PLOT

# matplotlib.pyplot.plot_date(datetime, f, fmt='b.')
# plt.xlabel('Date and Time')
# plt.ylabel('Frequency (Hz)')
# plt.title('Frequency (Hz) over Time')
# matplotlib.pyplot.show() ## ADDED TO SHOW PLOT

# matplotlib.pyplot.plot_date(datetime, pf, fmt='g.')
# plt.xlabel('Date and Time')
# plt.ylabel('Power Factor')
# plt.title('Power Factor over Time')
# matplotlib.pyplot.show() ## ADDED TO SHOW PLOT

# colors = (0,0,0)
# plt.scatter(q,p,c=colors, alpha=0.5)
# plt.xlabel('Q (kVAr)')
# plt.ylabel('P (kW)')
# plt.title('Reactive Power Q vs Real Power P')
# plt.show()


count_percent = round((len([i for i in p if i <= 637]) / len(p)) * 100, 1)
print(count_percent)


p_max = max(p)
p_min = min(p)
p_avg = sum(p) / len(p)

pf_max = max(pf)
pf_min = min(pf)
pf_avg = sum(pf) / len(pf)

f_max = max(f)
f_min = min(f)
f_avg = sum(f) / len(f)

q_max = max(q)
q_min = min(q)
q_avg = sum(q) / len(q)



min_p_position = df.loc[df['P_tot (kW)'] == p_min]
min_p_time = min_p_position[['Date', 'Time']]
max_p_position = df.loc[df['P_tot (kW)'] == p_max]
max_p_time = max_p_position[['Date', 'Time']]

print()
print("Average Power = " + str(round(p_avg, 3)) + " kW")
print("Min. Power = " + str(round(p_min, 3)) + " kW @")
print(min_p_time)
print("Max. Power  = " + str(round(p_max, 3)) + " kW @")
print(max_p_time)
print()
print("Average Frequency = " + str(round(f_avg, 3)) + " Hz")
print("Min. Frequency = " + str(round(f_min, 3)) + " Hz")
print("Max. Frequency = " + str(round(f_max, 3)) + " Hz")
print()
print("Average PF = " + str(round(pf_avg, 3)))
print("Min. PF = " + str(round(pf_min, 3)))
print("Max. PF = " + str(round(pf_max, 3)))
print()
print("Average Q = " + str(round(q_avg, 3)) + " kVAr")
print("Min. Q = " + str(round(q_min, 3)) + " kVAr")
print("Max. Q = " + str(round(q_max, 3)) + " kVAr")

