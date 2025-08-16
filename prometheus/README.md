# Prometheus

Prometheus is a timeseries database that scrapes data from designated endpoints.

It has many use cases, but here it is primarily used as a backend for Grafana, a 
data visualization/dashboarding tool.


## How to Use

There is nothing special to configure here if deploying with this template.

In general, just ensure that Prometheus is scraping the provided `Push Gateway` in its 
configuration.
