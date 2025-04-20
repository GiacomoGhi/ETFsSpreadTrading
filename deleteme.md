# ETFsInverseCorrelation

Progetto sulla ricerca di coppie di ETF inversamente correlati.

ETF interessanti da analizzare:

Ticker Descrizione
SPY S&P 500 ETF
TLT Treasury Bonds 20+ anni
GLD Oro
UUP US Dollar Index ETF
QQQ Nasdaq-100
VXX VIX Short-Term Futures
SH Short S&P 500 (inverso di SPY)
IWM Russell 2000
SLV Argento
TIP Treasury Inflation-Protected Bonds

1. Correlazione
   Correlazione statica su tutto il periodo.

Correlazione mobile (es. rolling window di 30 o 90 giorni).

2. Regressione lineare
   Per vedere quanto bene uno ETF può essere spiegato da un altro (es. TLT ~ SPY).

Utile per stimare il beta e costruire un hedge ratio.

3. Z-score su spread
   Se una coppia ha relazione stabile, lo spread tra i prezzi può essere usato per generare segnali di ingresso/uscita.
