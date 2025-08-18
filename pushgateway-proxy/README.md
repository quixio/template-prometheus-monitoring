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


### HTTP Endpoint Url

To get the necessary HTTP endpoint path, simply navigate to the pipeline view and
copy the link presented by the `pushgateway-proxy`.

> NOTE: do not remove public access, otherwise the link will not exist, which means 
> applications external to the project will not be able to communicate with the proxy.

### HTTP Endpoint Authentication

The `pushgateway-proxy` also requires a password to send data to it. Use the same
password used for `PUSHGATEWAY_PROXY_PASSWORD` when generating the deployment for 
`pushgateway-proxy`.
