# Prometheus

Prometheus is a timeseries database that scrapes data from designated endpoints.

It has many use cases, but here it is primarily used as a backend for Grafana, a 
data visualization/dashboarding tool.


## How to Use

Ensure that Prometheus is scraping the desired endpoints, which in a Quix-based application 
monitoring configuration, be at least a `Prometheus Pushgateway`.
