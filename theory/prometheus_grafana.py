"""
Q:: What is grafana
A:: Grafana is a tool which is used to expose different types of metrics 
    at particular end point

    
Q:: What is prometheus
A:: Prometheus is an open-source monitoring and alerting system. It basically: 
    collects metrics in some intervals, stores them as time-series data, lets you 
    query and visualize them, screams at you (alerts) when things go wrong

    
Q:: How prometheus scrapes methrics from app?
A:: Prometheus requires .yml config file in order to determine which app it need to scrape the metrics 
    from (container name, handle, port) and to assign interval. Attached to prometheus docker via volume.
    FastAPI app exposes metrics on handle "/metrics".


Q:: How grafana pulls metrics from prometheus
A:: Grafana connects to prometheus via http request and querries the data using specific querrying file.   
    

Q:: Common types of metrics in grafana. Common metrics.
A:: counter, gauge, histogram metrics


Q:: How metrics are displayed in grafana
A:: Metrics on Grafana are exposed on dashboards/panels. Dashboard receives data by using prometheus queries. 
        - specify unit (secs, percents)
        - pycharts/timeseries/number


Q:: prometheus on kubernetes
A:: When we install kube-prometheus stack we release 
    Prometheus operator::
        - Prom itself
        - Alert manager
    Node exporter, Kube State metrics::
        - export metrics from kube itself
    Grafana::
        - grafana               
"""