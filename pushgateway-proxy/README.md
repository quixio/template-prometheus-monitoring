# Prometheus Pushgateway Proxy

This service provides a way for applications to publish metric data to
`Prometheus` through an authenticated public HTTP endpoint.

It is a Flask app that simply forwards its traffic to an actual 
`Prometheus Pushgateway` instance, which is scraped from periodically with `Prometheus`.

## How to Use

Ensure that this service has `public access` enabled under the `Network` tab when
deploying. This HTTP endpoint is where applications will publish their Prometheus 
metrics to.

> NOTE: `public access` should already be enabled when deploying with this template.

Also upon deployment, you'll need to generate a password which applications must 
provide when attempting to publish data to the public URL. You'll need to refresh the
deployment once this is set.

## Sending Prometheus Data to the Proxy

You will need to provide the `Prometheus Pushgateway Proxy` URL and its respective password
(which you generated earlier) to the `push_to_gateway` function from Python's 
`prometheus_client` library (which should also include your desired metrics).

You can find the URL in Quix Cloud by opening the `deployments` list from the
left side panel and copying the url from the blue box near the `Pushgateway Proxy` 
deployment name:

![quix_url](quix_url.png)

You can [check out this example python file](../resource-usage-generator-app/metric_scraper.py)
(from the `resource-usage-generator-app` example app in this template) for more details on how to use the `prometheus_client`.