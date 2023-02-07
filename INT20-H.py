import pandas as pd

class Person:
		user_id = ''
		state = ''
		event_name = ''
		event_attributes = ''
		date = ''
		platform = ''
		device = ''
		device_model = ''
		
		def __init__(self, id:str, state:str, event_name:str, event_attributes:str, date:str, platform:str, device:str, device_model:str) -> None:
			self.user_id = id
			self.state = state
			self.event_name = event_name
			self.event_attributes = event_attributes
			self.date = date
			self.platform = platform
			self.device = device
			self.device_model = device_model

		def setstate(self, a):
			self.state = a

		def setplatform(self, a):
			self.platform = a

		def setdevise_manifacture(self, a):
			self.device = a

		def print_id(self):
			print(self.user_id)


rows = 23357

pd.set_option('display.max_columns', 8)
pd.set_option('display.max_rows', rows)
df = pd.read_csv('data.csv')

clients = []

for i in range(rows):
    loc = df.loc[i]

    clients.append(Person(loc['userid'], loc['user_state'], 
                          loc['event_name'], loc['event_attributes'], 
                          loc['event_created_date'], loc['event_platform'],
                          loc['device_manufacture'], loc['device_model']))

def unique():
    unique_list = []

    for id in df['userid']:
        if id not in unique_list:
            unique_list.append(id)
            print(id)
    
    print(len(unique_list))


df = pd.read_csv('data.csv')

# Adding a label column indicating whether the account is cancelled or not
df['Subscription Premium Cancel'] = df.apply(lambda row: 1 if row['Subscription Premium Cancel'] == 'Account Cancel' else 0, axis=1)
df['event_created_date'] = pd.to_datetime(df['event_created_date'])
df['month'] = df['event_created_date'].dt.month

print("\n")

#######################################################################################
# Aggregating data based on the label column and state
aggregated_data = df.groupby(['user_state'])['cancelled'].sum().reset_index()

# Sorting the results to get the states that are most correlated with account cancellations
aggregated_data = aggregated_data.sort_values(by='cancelled', ascending=False)

# Printing the results
print("States sorted correlation:")
print(aggregated_data)
print("\n")
#######################################################################################
# Aggregating data based on the label column and event_name
aggregated_data = df.groupby(['event_name'])['cancelled'].sum().reset_index()

# Sorting the results to get the events that are most correlated with account cancellations
aggregated_data = aggregated_data.sort_values(by='cancelled', ascending=False)

# Printing the results
print("Events sorted correlation:")
print(aggregated_data)
print("\n")
#######################################################################################
# Aggregating data based on the label column and date
aggregated_data = df.groupby(['month'])['cancelled'].sum().reset_index()

# Sorting the results to get the dates that are most correlated with account cancellations
aggregated_data = aggregated_data.sort_values(by='cancelled', ascending=False)

# Printing the results
print("Dates sorted correlation:")
print(aggregated_data)
print("\n")
#######################################################################################

# Aggregating data based on the label column and platform
aggregated_data = df.groupby(['event_platform'])['cancelled'].sum().reset_index()

# Sorting the results to get the platforms that are most correlated with account cancellations
aggregated_data = aggregated_data.sort_values(by='cancelled', ascending=False)

# Printing the results
print("event_platform sorted correlation:")
print(aggregated_data)
print("\n")
#######################################################################################

# Aggregating data based on the label column and platform
aggregated_data = df.groupby(['device_manufacture'])['cancelled'].sum().reset_index()

# Sorting the results to get the platforms that are most correlated with account cancellations
aggregated_data = aggregated_data.sort_values(by='cancelled', ascending=False)

# Printing the results
print("device_manufacture sorted correlation:")
print(aggregated_data)
print("\n")
#######################################################################################

# Aggregating data based on the label column and platform
aggregated_data = df.groupby(['device_model'])['cancelled'].sum().reset_index()

# Sorting the results to get the platforms that are most correlated with account cancellations
aggregated_data = aggregated_data.sort_values(by='cancelled', ascending=False)

# Printing the results
print("device_model sorted correlation:")
print(aggregated_data)
###

aggregated_data = df.groupby(['event_name'])['cancelled'].sum().reset_index()