############### APPENDIX ###############

############### PART 1 ###############

############### TASK 1

solution1 = """
            CREATE TABLE BackUP_CarSharing
            AS SELECT * FROM `TABLE 1`;
            """

############### TASK 2

solution2 = """
            ALTER TABLE `TABLE 1`
            ADD COLUMN temp_category VARCHAR(10);
            
            UPDATE `TABLE 1`
            SET temp_category = CASE
                WHEN temp_feel < 10 THEN 'Cold' 
                WHEN temp_feel BETWEEN 10 AND 25 THEN 'Mild'
                WHEN temp_feel > 25 THEN 'Hot'
                ELSE 'Unknown' 
            END; 
            """

############### TASK 3

solution3 = """
            CREATE TABLE temperature
            AS SELECT temp,
            temp_feel,
            temp_category FROM `TABLE 1`;
            
            ALTER TABLE `TABLE 1`
            
            DROP COLUMN temp,
            DROP COLUMN temp_feel; 
            """

############### TASK 4

solution4 = """
            ALTER TABLE `TABLE 1`
            ADD COLUMN weather_code INT; 

            -- Step 2: Update the weather_code column based on the weather values UPDATE `TABLE 1` 
            UPDATE `TABLE 1`  
            SET weather_code =  
                CASE   
                    WHEN weather = 'Clear or partly cloudy' THEN 1
                    WHEN weather = 'Mist' THEN 2   
                    WHEN weather = 'Light snow or rain' THEN 3   
                    WHEN weather = 'heavy rain/ice pellets/snow + fog' THEN 4   
                    ELSE 0
                END;  
            """

############### TASK 5

solution5 = """ 
            """








############### TASK 1

solution1 = """
            def read_csv_file(file_path):
                try:
                    # Read the CSV file
                    df = pd.read_csv(file_path)

                    # Preprocess the DataFrame

                    # Drop duplicate rows
                    df = df.drop_duplicates()
                    
                    # Check for null values
                    null_values_count = df.isnull().sum()
                    print("Null values count:\n", null_values_count)
                    
                    # Handle null values
                    for column in df.columns:
                        if df[column].isnull().any():
                            # Replace null values with mean for numerical columns
                            if df[column].dtype in ['int64', 'float64']:
                                df[column] = df[column].fillna(df[column].mean())
                            # Replace null values with mode for categorical columns
                            else:
                                df[column] = df[column].fillna(df[column].mode()[0])

                    # Return the DataFrame
                    return df

                except FileNotFoundError:
                    print(f"File not found: {file_path}")
                    return None

                except pd.errors.EmptyDataError:
                    print(f"No data in file: {file_path}")
                    return None

                except pd.errors.ParserError:
                    print(f"Error parsing file: {file_path}")
                    return None


            file_path = 'CarSharing.csv'  # replace with your CSV file path
            car_sharing_df = read_csv_file(file_path)

            if car_sharing_df is not None:
                print("Original DataFrame shape:", car_sharing_df.shape)
                #print("Original DataFrame info:", car_sharing_df.info())
                print("\n------------------------------------------------------------------\n")
                print("Original Dataframe summary statistics:", car_sharing_df.describe())
            """


############### TASK 5

solution5 = """ 
            """

