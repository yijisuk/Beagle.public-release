import plotly.graph_objects as go


def gauge(value, range, title=None):

    indicator_args = {
        "mode": "gauge+number",
        "value": value,
        "domain": {'x': [0, 1], 'y': [0, 1]},
        "gauge": {
            'axis': {'range': range},
            'bar': {'color': gauge_color(value, range[0]/2, range[1]/2, range[1])}
        }
    }
    
    if title is not None:
        indicator_args["title"] = {'text': title}
        
    return go.Indicator(**indicator_args)



def gauge_color(score, min_val, mid_val, max_val):

    if score <= min_val:
        return "#e5383b"
    elif min_val < score <= mid_val:
        return "#fdc500"
    elif mid_val < score <= max_val:
        return "#2dc653"