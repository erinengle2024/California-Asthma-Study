from sqlalchemy import create_engine
import pandas as pd
import psycopg2
# ========Kevins below========
# # engine=create_engine('sqlite:///database.db')
# engine = create_engine('postgresql://postgres:posgres:5432/database.db')
# conn=engine.connect()

# df=pd.read_csv('survey_2018_data.csv')
# # https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_sql.html
# # creates schema and inserts records
# df.to_sql('data_table', con=conn)

# conn.close()
# =====

# # File paths
# files = ['survey_2018_data.csv', 'survey_2019_data.csv', 'survey_2022_data.csv']
# # Database connection details
# db_config = {
#     'dbname': 'database.db',
#     'user': 'postgres',
#     'password': 'postgres',
#     'host': 'localhost',
#     'port': '5432'
# }
# # Connect to PostgreSQL database
# conn = psycopg2.connect(**db_config)
# cur = conn.cursor()
# # Create table if it does not exist
# cur.execute('''
#     CREATE TABLE IF NOT EXISTS  survey_2018(
#            TotalPopulation INT,
#     CaliforniaCounty VARCHAR(255),
#     ZIP VARCHAR(10),
#     Longitude DOUBLE PRECISION,
#     Latitude DOUBLE PRECISION,
#     OzonePctl NUMERIC(5, 2),
#     PM25Pctl NUMERIC(5, 2),
#     DieselPMPctl NUMERIC(5, 2),
#     PesticidesPctl NUMERIC(5, 2),
#     TrafficPctl NUMERIC(5, 2),
#     AsthmaPctl NUMERIC(5, 2),
#     PovertyPctl NUMERIC(5, 2),
#     CardiovascularDiseasePctl NUMERIC(5, 2)
#     )
# ''')
# cur.execute('''
#     CREATE TABLE IF NOT EXISTS  survey_2019(
#             TotalPopulation INT,
#     CaliforniaCounty VARCHAR(255),
#     ZIP VARCHAR(10),
#     Longitude DOUBLE PRECISION,
#     Latitude DOUBLE PRECISION,
#     OzonePctl NUMERIC(5, 2),
#     PM25Pctl NUMERIC(5, 2),
#     DieselPMPctl NUMERIC(5, 2),
#     PesticidesPctl NUMERIC(5, 2),
#     TrafficPctl NUMERIC(5, 2),
#     AsthmaPctl NUMERIC(5, 2),
#     PovertyPctl NUMERIC(5, 2),
#     CardiovascularDiseasePctl NUMERIC(5, 2)
#     )
# ''')
# cur.execute('''
#     CREATE TABLE IF NOT EXISTS  survey_2022(
#           TotalPopulation INT,
#     CaliforniaCounty VARCHAR(255),
#     ZIP VARCHAR(10),
#     Longitude DOUBLE PRECISION,
#     Latitude DOUBLE PRECISION,
#     OzonePctl NUMERIC(5, 2),
#     PM25Pctl NUMERIC(5, 2),
#     DieselPMPctl NUMERIC(5, 2),
#     PesticidesPctl NUMERIC(5, 2),
#     TrafficPctl NUMERIC(5, 2),
#     AsthmaPctl NUMERIC(5, 2),
#     PovertyPctl NUMERIC(5, 2),
#     CardiovascularDiseasePctl NUMERIC(5, 2)
#     )
# ''')
# # Load and insert data from CSV files
# # for file in files:
# #     df = pd.read_csv(file)

    
# #     for _, row in df.iterrows():
# #         cur.execute('''
# #             INSERT INTO survey_2018 (Total Population,California County,ZIP,Longitude,Latitude,Ozone Pctl,PM2.5 Pctl,Diesel PM Pctl,Pesticides Pctl,Traffic Pctl,Asthma Pctl,Poverty Pctl,Cardiovascular Disease Pctl)
# #             VALUES  (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
# #         ''', (row['Total Population'],
# #             row['California County'],
# #             row['ZIP'],
# #             row['Longitude'],
# #             row['Latitude'],
# #             row['Ozone Pctl'],
# #             row['PM2.5 Pctl'],
# #             row['Diesel PM Pctl'],
# #             row['Pesticides Pctl'],
# #             row['Traffic Pctl'],
# #             row['Asthma Pctl'],
# #             row['Poverty Pctl'],
# #             row['Cardiovascular Disease Pctl']))
# # Load and insert data from CSV files
# for file in files:
#     df = pd.read_csv(file)
#     for _, row in df.iterrows():
#         cur.execute('''
#             INSERT INTO survey_2018 (
#                 TotalPopulation,
#                 CaliforniaCounty,
#                 ZIP,
#                 Longitude,
#                 Latitude,
#                 OzonePctl,
#                 PM25Pctl,
#                 DieselPMPctl,
#                 PesticidesPctl,
#                 TrafficPctl,
#                 AsthmaPctl,
#                 PovertyPctl,
#                 CardiovascularDiseasePctl
#             ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
#         ''', (
#             row['Total Population'],
#             row['California County'],
#             row['ZIP'],
#             row['Longitude'],
#             row['Latitude'],
#             row['Ozone Pctl'],
#             row['PM2.5 Pctl'],
#             row['Diesel PM Pctl'],
#             row['Pesticides Pctl'],
#             row['Traffic Pctl'],
#             row['Asthma Pctl'],
#             row['Poverty Pctl'],
#             row['Cardiovascular Disease Pctl']
#         ))

# conn.commit()
# cur.close()
# conn.close()
from sqlalchemy import create_engine
import pandas as pd
import psycopg2

# File paths
files = ['survey_2018_data.csv', 'survey_2019_data.csv', 'survey_2022_data.csv']

# Database connection details
db_config = {
    'dbname': 'database',
    'user': 'postgres',
    'password': 'postgres',
    'host': 'localhost',
    'port': '5432'
}

# Connect to PostgreSQL database using SQLAlchemy
engine = create_engine(f"postgresql://{db_config['user']}:{db_config['password']}@{db_config['host']}:{db_config['port']}/{db_config['dbname']}")
conn = psycopg2.connect(**db_config)
cur = conn.cursor()

# Create table if it does not exist
table_creation_query = '''
CREATE TABLE IF NOT EXISTS survey_2018 (
    TotalPopulation INT,
    CaliforniaCounty VARCHAR(255),
    ZIP VARCHAR(10),
    Longitude DOUBLE PRECISION,
    Latitude DOUBLE PRECISION,
    OzonePctl NUMERIC(5, 2),
    PM25Pctl NUMERIC(5, 2),
    DieselPMPctl NUMERIC(5, 2),
    PesticidesPctl NUMERIC(5, 2),
    TrafficPctl NUMERIC(5, 2),
    AsthmaPctl NUMERIC(5, 2),
    PovertyPctl NUMERIC(5, 2),
    CardiovascularDiseasePctl NUMERIC(5, 2)
)
'''
for year in ['2018', '2019', '2022']:
    cur.execute(table_creation_query.format(table_name=f"{survey_2018}"))

# Load and insert data from CSV files
for file in files:
    year = file.split(',')[1]
    df = pd.read_csv(file)

    # Prepare data for insertion
    data_to_insert = [
        (
            row['Total Population'],
            row['California County'],
            row['ZIP'],
            row['Longitude'],
            row['Latitude'],
            row['Ozone Pctl'],
            row['PM2.5 Pctl'],
            row['Diesel PM Pctl'],
            row['Pesticides Pctl'],
            row['Traffic Pctl'],
            row['Asthma Pctl'],
            row['Poverty Pctl'],
            row['Cardiovascular Disease Pctl']
        )
        for _, row in df.iterrows()
    ]

    # Insert data using executemany for better performance
    insert_query = f'''
    INSERT INTO survey_{year} (
        TotalPopulation,
        CaliforniaCounty,
        ZIP,
        Longitude,
        Latitude,
        OzonePctl,
        PM25Pctl,
        DieselPMPctl,
        PesticidesPctl,
        TrafficPctl,
        AsthmaPctl,
        PovertyPctl,
        CardiovascularDiseasePctl
    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    '''
    cur.executemany(insert_query, data_to_insert)

# Commit the transaction
conn.commit()

# Close the cursor and connection
cur.close()
conn.close()
