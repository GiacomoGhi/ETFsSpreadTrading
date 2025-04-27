import pandas as pd

class Backtester:
    def __init__(self, spread: pd.Series, zscore: pd.Series, zscore_threshold: float = 2.0, initial_capital: float = 1000.0):
        self.spread = spread
        self.zscore = zscore
        self.zscore_threshold = zscore_threshold
        self.initial_capital = initial_capital
        self.capital = initial_capital
        self.position = 0  # 0 = no position, 1 = long spread, -1 = short spread
        self.entry_spread = 0
        self.equity_curve = []
        self.dates = spread.index

        # Calcolo position_size dinamico in base allo spread medio
        spread_mean_abs = spread.abs().mean()  # media assoluta dei valori dello spread
        if spread_mean_abs == 0:  # Evitiamo divisione per zero
            position_size = 1.0
        else:
            position_size = 100 / spread_mean_abs  # Obiettivo: circa 100€ di variazione ogni 1 unità di spread
        self.position_size = min(max(position_size, 1), 1000)  # Clip per sicurezza: minimo 1, massimo 1000

    def run(self):
        for i in range(len(self.spread)):
            today = self.dates[i]

            if self.position == 0:
                if self.zscore[today] > self.zscore_threshold:
                    self.position = -1  # short spread
                    self.entry_spread = self.spread[today]
                elif self.zscore[today] < -self.zscore_threshold:
                    self.position = 1   # long spread
                    self.entry_spread = self.spread[today]
                    
            elif self.position == 1:
                if self.zscore[today] >= 0:
                    profit = (self.spread[today] - self.entry_spread) * self.position_size
                    self.capital += profit
                    self.position = 0
                    
            elif self.position == -1:
                if self.zscore[today] <= 0:
                    profit = (self.entry_spread - self.spread[today]) * self.position_size
                    self.capital += profit
                    self.position = 0

            self.equity_curve.append(self.capital)
