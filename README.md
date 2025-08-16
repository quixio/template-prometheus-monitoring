# Metrics and Monitoring Project Template

This template includes a set of services that enables a complete application 
metrics + monitoring stack using Prometheus + Grafana.

An example application is also included to show how to publish metrics to
the monitoring stack.



## Running the Template

### Syncing
Once the project is set up, an initial sync must be performed to deploy everything. 

Essentially, the cloud state must sync up to the current state of the new repository 
which now has a cloned version of the template.

![img](images/sync.png)

Syncing is always a manually initiated operation that's available whenever updates 
to the code (underlying repository) happen.

### Setting Secrets

>**WARNING**: These secrets exist to act as an authentication layer since 
> ***some services are openly accessible to the entire internet***;
> as such: **DO NOT PICK WEAK PASSWORDS**.

Upon syncing, there will be a prompt to set up some project-level secrets (passwords). 
Simply choose a secure password for each.

![img](images/secrets_missing.png)

![img](images/secrets_set.png)

Note that once set, you cannot view the values again. This largely only matters for 
services like Grafana, where users will be required to directly enter them for access to 
the UI, so make sure you save the value somewhere. 

Other services will reference these secrets directly in their project deployment 
configurations, so they do not need to be manually entered.

### Service Startup Delays and Application Restarts

Upon first sync, it is normal that some applications may restart/error a few times while 
some of its dependencies are still starting up.

Applications should not need to restart more than 3-5 times before everything is
up and running.




## How it Works

The `PushGatewayProxy` is set up to receive project-external traffic with an 
authenticated HTTP endpoint that Applications submit their Prometheus metrics to.

The `PushGateway` service receives the forwarded request from the `PushGatewayProxy`
and stores them until `Prometheus` scrapes them.

On a cadence, the metrics are all then scraped by `Prometheus`, 
a time series database. The data is now catalogued and ready for use.

`Grafana`, a realtime dashboarding application (also gated with credentials), 
provides visualizations through custom-built queries made on the Prometheus instance.




## Publishing Metrics to the PushGateway (Prometheus)

### Included Example Application
This template includes two different deployments of the `resource-usage-generator-app`
to showcase publishing metrics to the `PushGateway` using Python's `Prometheus` library.

To learn more, check out the `metrics_scraper.py` file which houses most of the data
scraping/pushing logic.


### HTTP endpoint

INFO HERE ABOUT IT



## Intended Use of Monitoring Template

![monitoring_diagram](images/monitoring_diagram.png)

While this template has two example applications running in the same 
workspace to showcase how it works, in general you should deploy this monitoring 
stack independently of your applications.

This means you can have one centralized project for monitoring, with separate 
environments for handling dev or prod operations, for example.

Then, applications can send metrics to it from any other project using the respective 
`Push Gateway Proxy` URL + password.

> Note: This example has the applications hitting a "localized" service endpoint on the 
> HTTP proxy for the sake of removing any additional user setup for the example. 
> When sending metrics from applications within other projects (as recommended),
> use the HTTP proxy url as [explained here](#http-endpoint).



## Grafana

### Accessing Grafana

Click on the blue link to log in to Grafana.

![img](images/grafana_link.png)

- **username**: `admin`
- **password**: whatever value `grafana_password` was set to when
  first setting up the template.

![img](images/grafana_login.png)

Then, navigate to the dashboards tab:

![img](images/grafana_home.png)

### Exploring the Dashboard

![grafana](images/grafana.png)


## Learn More

To learn more about each respective service, check out the `README.md` for each.





TODO:

- confirm latest versions of images (ex storage, permissions, etc)
- check readme's of other services and consolidate stuff to the main readme.
- get picture of pipeline
- fix grafana provisioning stuff
- better breakdown of http route and publishing