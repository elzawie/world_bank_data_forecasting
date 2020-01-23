import plotly.express as px


def plot_historical_and_forecasted_values(dataframe, x, y, color_by_col,
                                          indicator_code, country):
    """Function used to plot historical and forecasted values represented as
    lines with markers.

    Arguments:
        dataframe {[DataFrame]} -- just as the name implies, expects a DataFrame object
        x {[str]} -- column which values should be displayed on the x-axis
        y {[str]} -- column which values should be displayed on the y-axis
        color_by_col {[str]} -- column which should be used to color the lines and markers
    """

    fig = px.line(dataframe, x=x, y=y,
                  color=color_by_col,
                  line_shape='spline',
                  width=980, height=576)
    fig.data[0].update(mode='markers+lines')
    fig.data[1].update(mode='markers+lines')
    fig.update_layout(title=f'Historical and forecasted values for {indicator_code} in {country}',
                      xaxis_title='Year',
                      yaxis_title='Value')
    fig.show()
