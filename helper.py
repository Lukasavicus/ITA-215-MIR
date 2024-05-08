import pandas as pd
import numpy as np

def normalize(df):
    x=df.copy()

    for i in x.columns[1:]:
        x[i]=x[i]/x[i][0]
    return x

# Let's define a function to calculate stocks daily returns (for all stocks)
def daily_return(df):
        df_daily_return=df.copy()

        for i in df.columns[1:]:
            for j in range(1, len(df)):
                    df_daily_return[i][j]=((df[i][j]-df[i][j-1])/df[i][j-1])*100
            df_daily_return[i][0]=0
        return df_daily_return

def portfolio_assemble(all_assets_df, portfolio, weights=[]):
        values = all_assets_df[portfolio].sum(axis=1) / len(portfolio)
    
        df = pd.DataFrame()
        df['date'] = all_assets_df['date']
        df['portfolio'] = values

        return df

def calculate_daily_return(df):
        cols = df.columns[1:]
        returns_df = df[cols].pct_change()
        k = df.columns[0]
        returns_df[k] = df[k]
        return returns_df

def calculate_metrics(df):
    pass
    # cumulative_returns = (returns_df + 1).prod() - 1
    # return (
    #     prices_daily_return.mean(),
    #     prices_daily_return.sum(axis=1),
    #     cumulative_returns
    # )
# usage: calculate_metrics

def calculate_sharpe_ratio(returns_df, risk_free_rate=0):
        daily_risk_free_rate = (1 + risk_free_rate) ** (1/252) - 1    # Assuming 252 trading days per year
        sharpe_ratio = (returns_df.mean() - daily_risk_free_rate) / returns_df.std() * np.sqrt(252)
        return sharpe_ratio

def calculate_capm(base_asset_serie, asset_serie, risk_free_rate=0):

        # X = list(base_asset_serie)
        X = list(base_asset_serie)[1:]
        # Y = list(asset_serie.fillna(0))
        Y = list(asset_serie.dropna())

        beta, alpha = np.polyfit(X, Y, 1)
        # print("Beta for {} stock is ={}, and the Alpha is {}".format(asset_serie.name, beta, alpha))

        return_of_market = base_asset_serie.mean()*252
        expected_return = risk_free_rate + (beta * (return_of_market-risk_free_rate))

        return (expected_return, alpha, beta)
