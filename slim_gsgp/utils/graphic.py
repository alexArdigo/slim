import pandas as pd
import plotly.graph_objects as go


def build_graphic(log_path, dataset_name):
    train_color = 'blue'
    test_color = 'orange'

    fig = go.Figure()
    fig.add_trace(go.Scatter(y=pd.read_csv(log_path, header=None).iloc[:, 5].values,
                             mode='lines', name='Train', line=dict(color=train_color)))
    fig.add_trace(go.Scatter(y=pd.read_csv(log_path, header=None).iloc[:, 8].values,
                             mode='lines', name='Test', line=dict(color=test_color)))
    fig.update_layout(
        height=400, width=800,
        margin=dict(t=50),
        yaxis_range=[0, None],
        title_text='GP - Train vs Test Fitness (' + dataset_name + ' dataset)',
        xaxis_title='Generation', yaxis_title='RMSE'
    )
    fig.update_yaxes(range=[0, None])
    fig.show()
