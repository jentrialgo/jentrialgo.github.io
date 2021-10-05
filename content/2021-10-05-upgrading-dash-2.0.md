Title: Upgrading to dash 2.0
Date: 2021-10-05 14:20
Category: Python
Tags: Python, Dash

I had some dashboards built in Python with
[Dash](https://github.com/plotly/dash). They were using version 1.13.4 and I
updated it to version 2.0.0. In addition to converting the imports, as explained
in the [migration guide](https://dash.plotly.com/dash-2-0-migration), I also
had to change state variables because I was getting the error:

```md
ValueError: The state keyword argument may not be provided without the input keyword argument
```

I didn't understand the explanation in the migration guide. After reading the
[new documentation about callbacks](https://dash.plotly.com/basic-callbacks),
I've found that I had to change my `app_callbacks`. Previously, I had something
like this:

```python
@app.callback(
    Output(component_id='wl-plot', component_property='src'),
    [
        Input(component_id='sol-select', component_property='value'),
        Input(component_id='button-apply', component_property='n_clicks'),
    ],
    state=
    [
        State(component_id='base-dir', component_property='value'),
    ]
)
```

And I had to change it to this:

```python
@app.callback(
    Output(component_id='wl-plot', component_property='src'),
    Input(component_id='sol-select', component_property='value'),
    Input(component_id='button-apply', component_property='n_clicks'),
    State(component_id='base-dir', component_property='value'),
)
```

So, basically, now you only have a list of `Output`, `Input` and `State`
instances and you don need the `state=...`.
