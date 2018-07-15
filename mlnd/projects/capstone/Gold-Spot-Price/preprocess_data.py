import pandas as pd

# Import sklearn.preprocessing.StandardScaler
from sklearn.preprocessing import MinMaxScaler


def get_normalised_data(data):
    """
    Normalises the data values using MinMaxScaler from sklearn
    :param data: a DataFrame with columns as  ['Index','Buyer','Seller']
    :return: a DataFrame with normalised value for all the columns except index
    """
    # Initialize a scaler, then apply it to the features
    scaler = MinMaxScaler()
    numerical = ['Open','Close']
    data[numerical] = scaler.fit_transform(data[numerical])

    return data


def remove_data(data):
    """
    Remove columns from the data
    :param data: a record of all the stock prices with columns as  ['Date','Open','Close','USD1MTD156N', 'Silver','DGASNYH','DEXCHUS']
    :return: a DataFrame with columns as  ['index','Open','Close']
    """
    # Define columns of data to keep from historical stock data
    item = []
    open = []
    close = []

    # Loop through the stock data objects backwards and store factors we want to keep
    i_counter = 0
    for i in range(len(data) - 1, -1, -1):
        item.append(i_counter)
        open.append(data['Open'][i])
        close.append(data['Close'][i])
        i_counter += 1

    # Create a data frame for stock data
    commodity = pd.DataFrame()

    # Add factors to data frame
    commodity['Item'] = item
    commodity['Open'] = open
    commodity['Close'] = pd.to_numeric(close)

    # return new formatted data
    return commodity

def process_data(data):
    """
    Update columns from the data
    :param data: a record of all the stock prices with columns as  ['Date','Open','Close','USD1MTD156N', 'Silver','DGASNYH','DEXCHUS']
    :return: a DataFrame with columns as  ['index','Open','Close','USD1MTD156N', 'Silver','DGASNYH','DEXCHUS']
    """
    # Define columns of data to keep from historical stock data
    item = []
    open = []
    close = []
    LIBOR = []
    Silver = []
    Gasoline = []
    Forex =[]

    # Loop through the stock data objects backwards and store factors we want to keep
    i_counter = 0
    for i in range(len(data) - 1, -1, -1):
        item.append(i_counter)
        open.append(data['Open'][i])
        close.append(data['Close'][i])
        LIBOR.append(data['USD1MTD156N'][i])
        Silver.append(data['Silver'][i])
        Gasoline.append(data['DGASNYH'][i])
        Forex.append(data['DEXCHUS'][i])
        i_counter += 1

    # Create a data frame for stock data
    commodity = pd.DataFrame()

    # Add factors to data frame
    commodity['Item'] = item
    commodity['Open'] = open
    commodity['Close'] = pd.to_numeric(close)
    commodity['USD1MTD156N'] = pd.to_numeric(LIBOR)
    commodity['Silver'] = pd.to_numeric(Silver)
    commodity['DGASNYH'] = pd.to_numeric(Gasoline)
    commodity['DEXCHUS'] = pd.to_numeric(Forex)

    # return new formatted data
    return commodity