# craft beer acquire

# imports

import pandas as pd

# acquire function

def beer_df():
    '''
    This function takes in the beer data and brewery data 
    and merges into one dataframe 
    and renames the columns for readbility
    and saves the new dataframe as a csv
    '''
    # getting the beers data
    df = pd.read_csv('beers.csv')
    # getting the breweries data
    df_1 = pd.read_csv('breweries.csv')
    # merging the two csv files together
    df = pd.merge(df, df_1, 
                   on='Unnamed: 0', 
                   how='inner')
    # renaming columns for readability
    df = df.rename(columns = {"style": "beer_style", "name_y": "brewery", "Unnamed: 0": "number", "name_x": "beer"})
    
    df.to_csv('beer_data.csv')
    
    return df


def beer_states():
    '''
    This function will take the count of each state in the data and 
    make a new dataframe with the states and number of breweries
    '''
    df = beer_df()
    state_df = df['state'].value_counts().rename_axis('states').reset_index(name='breweries')
    
    return state_df