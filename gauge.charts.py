import plotly.graph_objects as go

value = float(input("Enter the value: "))


fig = go.Figure(go.Indicator(
            mode ="gauge+number",
            value= value,
            title = {'text':"Speed"},
            gauge= {'axis':{'range':[0,100]},
                     'bar':{'color': "darkblue"},
                     'steps':[{'range':[0, 50], 'color':"lightgray"},
                              {'range':[50, 100], 'color':"gray"}],
                     'threshold': {'line': {'color': "red", 'width': 4},
                                    'thickness':1, 'value':75
                                   }
                    }
        ))

fig.show()
