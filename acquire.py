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
    # dropping columns that are not needed
    df.drop(['id'], axis=1, inplace=True)
    df.drop(['brewery_id'], axis=1, inplace=True)
    # creating average and mean to fill null values
    avg_abv = 0.05
    ibu_mean = df.ibu.mean()
    # filling null values in the beer data
    df.fillna({'abv' :avg_abv, 'ibu' :ibu_mean}, inplace=True)
    # saving the beer data to a csv file
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

def top_beers():
    '''
    This function will take the count of each beer type in the data and 
    make a new dataframe with the beer type and total number
    '''
    df = beer_df()
    
    top_beer = df.beer_style.value_counts().rename_axis('beer_type').reset_index(name='total')
    
    return top_beer

from sklearn.model_selection import train_test_split

def train_validate_test_split(df, target, seed=123):
    '''
    This function takes in a dataframe, the name of the target variable
    (for stratification purposes), and an integer for a setting a seed
    and splits the data into train, validate and test. 
    Test is 20% of the original dataset, validate is .30*.80= 24% of the 
    original dataset, and train is .70*.80= 56% of the original dataset. 
    The function returns, in this order, train, validate and test dataframes. 
    '''
    train_validate, test = train_test_split(df, test_size=0.2, 
                                            random_state=seed, 
                                            stratify=df[target])
    train, validate = train_test_split(train_validate, test_size=0.3, 
                                       random_state=seed,
                                       stratify=train_validate[target])
    return train, validate, test