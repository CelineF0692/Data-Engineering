import pandas as pd 

import datetime as dt

college = pd.read_csv('CollegeEnrollment.csv')

print(college)

print(len(college))

print(college.isna().sum())

college.duplicated().sum()

college.head()

unpivot_college = college.melt(id_vars= ['ID','Level of Student','Graduate Level of Student','Total Men','Total Women'],var_name='Ethnicity',value_name='Total' )
#print(unpivot_college)

unpivot_college.drop(columns=['Total Women', 'Total Men'],inplace=True)
print(unpivot_college)


#After I've completed all manipulation, now i will uplaoded the cleaned data into the MySQL database



import pandas as pd
import datetime as dt
import mysql.connector
from sqlalchemy import create_engine  # Corrected import statement

#Configuring...defining connection parameters
config = {
    'host': 'LocalHost',
    'user': 'root',
    'password':'celine',
    'database':'ETL_Project'

}

#Now we need to establish connection to MySQL 
# Create an SQLAlchemy engine
engine = create_engine('mysql+pymysql://root:celine@localhost/ETL_Project')



# Save the DataFrame to SQL
unpivot_college.to_sql('CollegeDets', engine, if_exists='append', index=False)








