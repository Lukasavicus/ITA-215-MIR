

# === PORTFOLIO ALLOCATION ====================================================
def portfolio_allocation(df_portfolio, df_stocks, weights, budget):
  _df_portfolio = df_portfolio.copy()
  _df_stocks    = df_stocks.copy()

  for counter, stock in enumerate(_df_portfolio.columns[1:]):
    _df_portfolio[stock] = _df_portfolio[stock] * weights[counter]
    _df_portfolio[stock] = _df_portfolio[stock] * budget

  _df_portfolio["portfolio daily worth $"]=_df_portfolio[_df_portfolio != "Date"].sum(axis=1)
  _df_portfolio['Portfolio % return']=0.0000

  for i in range(1, len(_df_stocks)):
    _df_portfolio['Portfolio % return'][i]=((_df_portfolio['portfolio daily worth $'][i]-_df_portfolio['portfolio daily worth $'][i-1])/_df_portfolio['portfolio daily worth $'][i-1])*100

  _df_portfolio['Portfolio % return'][0]=0

  return _df_portfolio

# --- cell sep ----------------------------------------------------------------
prices_df.shape[1]
# --- cell sep ----------------------------------------------------------------
NO_ASSETS = prices_df.shape[1] - 1 # Excluding 'date' colunm
np.random.seed(101)
weights=np.array(np.random.random(NO_ASSETS))
weights=weights/np.sum(weights)

print(weights)
# --- cell sep ----------------------------------------------------------------
df_portfolio = normalize(prices_df)

BUDGET = 1000000
df_portfolio_allocated = portfolio_allocation(df_portfolio, prices_df, weights, BUDGET)
# --- cell sep ----------------------------------------------------------------
df_portfolio_allocated
# --- cell sep ----------------------------------------------------------------
fig=px.line(x=df_portfolio_allocated.date, y=df_portfolio_allocated['Portfolio % return'])
fig.show()
# --- cell sep ----------------------------------------------------------------
# Plot all stocks (normalized)

interactive_plot(df_portfolio_allocated.drop(['Portfolio % return','portfolio daily worth $'], axis=1), title="Portfolio Indivual Stocks")
# --- cell sep ----------------------------------------------------------------
# Print out a histogram of daily returns
fig=px.histogram(df_portfolio_allocated, x='Portfolio % return')
fig.show()
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++