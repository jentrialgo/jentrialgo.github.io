Title: Metrics per stage in k6
Date: 2022-11-25 18:00
Category: k6
Tags: k6

If you want to have custom metrics per each stage in an executor, you have to
tag the stages (with `tagWithCurrentStageIndex()`) and add bogus thresholds for
each metric that you want with the tag `stage:i` (being `i` the number of each
stage). The bogus threshold has to be different for gauges (`max>0`) and rates
(`rate>=0`).

This example file shows how to do it:

```javascript
import http from 'k6/http';
import { tagWithCurrentStageIndex } from 'https://jslib.k6.io/k6-utils/1.3.0/index.js';

const stages = [
    { target: 1, duration: '10s' },
    { target: 5, duration: '10s' },
];

export const options = {
  scenarios: {
    contacts: {
      executor: 'ramping-arrival-rate',
      timeUnit: '1s',
      preAllocatedVUs: 10,
      maxVUs: 200,
      stages: stages,
    },
  },
  // Uncomment the next line if you want the count statistic
  // summaryTrendStats: ['avg', 'min', 'med', 'max', 'p(90)', 'p(95)', 'p(99)', 'count'],
  thresholds: {
    // Intentionally empty. We'll programatically define our bogus
    // thresholds (to generate the sub-metrics) below. In your real-world
    // load test, you can add any real threshoulds you want here.
  }
}

function addThreshold(thresholdName, threshold) {
    if (!options.thresholds[thresholdName]) {
        options.thresholds[thresholdName] = [];
    }

    // 'max>=0' is a bogus condition that will always be fulfilled
    options.thresholds[thresholdName].push(threshold);
}

for (var i=0; i<stages.length; i++) {
    // This adds per stage metrics for http_req_duration (a gauge)
    addThreshold(`http_req_duration{stage:${i}}`, 'max>=0');

    // This adds per stage metrics for iterations (a rate)
    addThreshold(`iterations{stage:${i}}`, 'rate>=0');
}

export default function () {
    tagWithCurrentStageIndex();
    http.get('https://test.k6.io');
}
```

The idea has been taken from [this post about metrics per
scenario](https://community.k6.io/t/multiple-scenarios-metrics-per-each/1314/3).
