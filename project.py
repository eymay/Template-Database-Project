import pandas as pd

fed_files = ["MORTGAGE30US.csv", "RRVRUSQ156N.csv", "CPIAUCSL.csv"]

dfs = [pd.read_csv(f, parse_dates=True, index_col=0) for f in fed_files]


dfs[0] #interest rate table
fed_data = pd.concat(dfs, axis=1) #combines the individual tables
fed_data
fed_data = fed_data.ffill().dropna() #forward fill works by holding the known value until another known value arrives
fed_data
zillow_files = ["Metro_median_sale_price_uc_sfrcondo_week.csv", "Metro_zhvi_uc_sfrcondo_tier_0.33_0.67_month.csv"]

dfs = [pd.read_csv(f) for f in zillow_files]
#dfs[0] #median_sale_price table
#dfs[1] #zillow home value index

dfs = [pd.DataFrame(df.iloc[0,5:]) for df in dfs] #getting first row only discarding first 5 columns
for df in dfs:
    df.index = pd.to_datetime(df.index)  
    df["month"] = df.index.to_period("M")
price_data = dfs[0].merge(dfs[1], on="month")
price_data.index = dfs[0].index
price_data

del price_data["month"]
price_data.columns = ["price", "value"]

from datetime import timedelta

fed_data.index = fed_data.index + timedelta(days=2)

price_data = fed_data.merge(price_data, left_index=True, right_index=True)

price_data.columns = ["interest", "vacancy", "cpi", "price", "value"]

price_data.plot.line(y="price", use_index=True)

price_data["adj_price"] = price_data["price"] / price_data["cpi"] * 100
price_data["adj_value"] = price_data["value"] / price_data["cpi"] * 100

price_data.plot.line(y="adj_price", use_index=True)

price_data["next_quarter"] = price_data["adj_price"].shift(-13)

price_data.dropna(inplace=True)

price_data["change"] = (price_data["next_quarter"] > price_data["adj_price"]).astype(int)

price_data["change"].value_counts()

predictors = ["interest", "vacancy", "adj_value"]
target = "adj_price"

from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor, GradientBoostingRegressor
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.metrics import accuracy_score, mean_squared_error, mean_absolute_error, r2_score
from sklearn.inspection import permutation_importance
from xgboost import XGBRegressor
import numpy as np
from sklearn.model_selection import GridSearchCV

START = 260
STEP = 52


def predict(train, test, predictors, target):
    #rf = RandomForestRegressor(min_samples_split=10, random_state=1)
    rf = LinearRegression()
    #rf = Ridge(alpha = 0.1) 
    #rf = XGBRegressor()

    rf.fit(train[predictors], train[target])
    preds = rf.predict(test[predictors])
    result = permutation_importance(rf, price_data[predictors], price_data[target], n_repeats=10, random_state=1)
    print("Importances Mean", result["importances_mean"])
    return preds


def backtest(data, predictors, target):
    all_preds = []
    for i in range(START, data.shape[0], STEP):
        train = price_data.iloc[:i]
        test = price_data.iloc[i:(i+STEP)]
        all_preds.append(predict(train, test, predictors, target))
    preds = np.concatenate(all_preds)
    mse = mean_squared_error(data.iloc[START:][target], preds)
    mae = mean_absolute_error(data.iloc[START:][target], preds)
    r2 = r2_score(data.iloc[START:][target], preds)
    print("Mean Squared Error:", mse)
    print("Mean Absolute Error:", mae)
    print("R-Squared:", r2)
    return preds, mse, mae, r2

preds, mse, mae, r2 = backtest(price_data, predictors, target)



import matplotlib.pyplot as plt
true_values = price_data.iloc[START:][target].values

plt.scatter(range(len(preds)),preds,label='Predicted Values')
plt.scatter(range(len(true_values)),true_values,label='True Values')
plt.xlabel('Time')
plt.ylabel('Price')
plt.legend()
plt.show()

plt.plot(preds, label='Predicted Values')
plt.plot(true_values, label='True Values')
plt.xlabel('Time')
plt.ylabel('Price')
plt.legend()
plt.show()

preds = backtest(price_data, predictors, target)[0]
true_values = price_data.iloc[START:]['adj_price'].values
interest_rate = price_data.iloc[START:]['interest'].values
vacancy_rate = price_data.iloc[START:]['vacancy'].values
adj_value = price_data.iloc[START:]['adj_value'].values

# Create the figure and subplots
fig, axes = plt.subplots(5, 1, figsize=(8, 8), sharex=True)

# Plot the predicted values
axes[0].plot(preds, label='Predicted Values')
axes[0].set_ylabel('Predicted Price')
axes[0].legend()

# Plot the true values
axes[1].plot(true_values, label='True Values')
axes[1].set_ylabel('True Price')
axes[1].legend()

# Plot the interest rate
axes[2].plot(interest_rate, label='Interest Rate')
axes[2].set_ylabel('Interest Rate')
axes[2].legend()

# Plot the vacancy rate
axes[3].plot(vacancy_rate, label='Vacancy Rate')
axes[3].set_ylabel('Vacancy Rate')
axes[3].legend()

# Plot the adj_value
axes[4].plot(adj_value, label='adj_value')
axes[4].set_ylabel('adj_value')
axes[4].legend()

plt.xlabel('Time')
plt.show()

# Plot the predicted values
plt.plot(preds, label='Predicted Values', linestyle='-')

# Plot the true values
plt.plot(true_values, label='True Values', linestyle='-.')

# Plot the interest rate
plt.plot(interest_rate, label='Interest Rate', linestyle=':')

# Plot the vacancy rate
plt.plot(vacancy_rate, label='Vacancy Rate', linestyle='-.')

# Plot the adj_value
plt.plot(adj_value, label='adj_value', linestyle=':')

plt.xlabel('Time')
plt.ylabel('Values')
plt.legend()
plt.show()

