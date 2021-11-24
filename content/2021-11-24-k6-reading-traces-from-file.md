Title: Reading traces from a file in k6
Date: 2021-11-24 9:24
Category: k6
Tags: k6, kubernetes

I wanted to read a trace of requests per second I have in a file and use it as
the injection pattern in k6. I could do it by reading the values into an array,
which is then used as the stages in a ramping arrival rate excutor, like this:

```javascript
import http from 'k6/http';
import papaparse from 'https://jslib.k6.io/papaparse/5.1.1/index.js';
import { SharedArray } from 'k6/data';

const trace_file = 'PATH_TO_THE_TRACE_FILE';
const trace = new SharedArray('another data name', function () {
  return papaparse.parse(open(trace_file)).data;
});

var stages = []
for (var i of trace) {
  stages.push({ target: trace[i][0], duration: "1s" })
}

export const options = {
  discardResponseBodies: true,
  scenarios: {
    contacts: {
      executor: 'ramping-arrival-rate',
      startRate: 1,
      timeUnit: '1s',
      preAllocatedVUs: 50,
      maxVUs: 1000,
      stages: stages
    },
  },
};

export default function () {
  const url = "http://localhost:8555";
  http.get(url);
}
```
