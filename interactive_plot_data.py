import plotly.express as px
import plotly.figure_factory as ff
import math

def show_plot(df, title):
  fig=px.line(title = title)
  for i in df.columns[1:]:
    fig.add_scatter(x=df["date"], y=df[i], name=i)

  fig.show()

def show_distplot(df_returns):
  # Group all data returns together in a list
    # Make a copy of the daily returns dataframe
    df_hist=df_returns.copy()

    df_hist=df_returns.drop(columns=["date"])
    data=[]

    df_hist = df_hist.fillna(0)

    for i in df_hist.columns:
        data.append(df_returns[i].values)

    data_without_nan = []
    for d in data:
        dd = [(0 if(math.isnan(di)) else di) for di in d]
        data_without_nan.append(dd)

    fig = ff.create_distplot(data_without_nan, df_hist.columns)
    fig.show();

# usage: show_distplot(prices_daily_return)