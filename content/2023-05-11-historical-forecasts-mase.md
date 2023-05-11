Title: Computing the MASE for historical_forecasts in darts
Date: 2023-05-11 14:00
Category: Time series prediction, darts
Tags: Time series prediction, darts

I haven't found any example online on how to compute the MASE (Mean Absolute
Scaled Error) for historical forecasts in
[darts](https://unit8co.github.io/darts/), so I thought I'd share this example:

```python
import numpy as np
from darts import TimeSeries
from darts.models import NaiveSeasonal
from darts.metrics import mase

my_data = [40, 42, 41, 45, 45, 47, 50]
my_np = np.array(my_data)
my_ts = TimeSeries.from_values(my_np)
my_model = NaiveSeasonal(K=1)
start = 3
my_forecast = my_model.historical_forecasts(series=my_ts, start=start, forecast_horizon=1)
my_mase = mase(actual_series=my_ts, pred_series=my_forecast, insample=my_ts[:start])
print(f"my_mase: {my_mase}")
my_ts.plot(label="original", marker="o")
my_forecast.plot(label="historical_forecasts", marker="x")
```

Notice that the `insample` parameter is set to the original time series up to
the start of the historical forecast.
