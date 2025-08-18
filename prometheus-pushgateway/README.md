# Prometheus Pushgateway

This receives prometheus-based metrics published from external sources
and makes them available for Prometheus to scrape.

> NOTE: In this template, Applications instead publish to the 
> Prometheus `Pushgateway Proxy` which forwards its traffic to this (in order to 
> provide an authenticated public endpoint).


## How it Works

Normally, Prometheus is designed to scrape designated endpoints to collect its data 
(as set up during its configuration).

However, since Applications are ephemeral in nature in Kubernetes (you can do static
deployments, but they are only necessary in specific circumstances), this model does not
work well for many Kubernetes or microservice-based architectures 
(especially with Kafka's multi-consumer model).

The Prometheus `Pushgateway` is an official pattern/offering by Prometheus to allow
a single endpoint that any number of non-static applications can collectively publish 
their metrics to. Prometheus then scrapes the `Pushgateway` for this data.
