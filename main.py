import pandas as pd

battery = pd.read_csv("battery_sensor_readings.csv")
trackers = pd.read_csv("trackers_metadata.csv")
market = pd.read_csv("market_prices.csv")

battery.head()

trackers.head()

market.head()

print("====== Battery ========")
print(battery.head())

print("\n====== Trackers =======")
print(trackers.head())

print("\n====== Market =========")
print(market.head())

print("\n====== Shapes ==========")
print("Battery:",battery.shape)
print("Trackers:",trackers.shape)
print("Market:",market.shape)

print("\n====== Battery Info=====")
print(battery.info())

print("\n====== Trackers Info=====")
print(trackers.info())

print("\n====== Market Info=====")
print(market.info())