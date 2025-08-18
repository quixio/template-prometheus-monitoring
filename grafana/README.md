# Grafana

Grafana is an open-source analytics and visualization platform used to monitor metrics 
from various data sources like Prometheus, InfluxDB, and PostgreSQL. 

It lets you build interactive dashboards with graphs, tables, and alerts 
to track system performance, application behavior, or business KPIs.

## Adding/Editing Dashboards

You can edit dashboards interactively and import/export them as needed via JSON files,
which can then be added to the `/provisioning/dashboards` folder.

Other data sources can also be added, but only Prometheus is included in this example.

If state is used, you can create/edit dashboards and changes will persist as desired.

> NOTE: be sure to backup/export any important dashboards, which can provide useful 
> restore points.

## Accessing the Example Dashboard

You can log in by clicking the application's link in the pipeline view:

![quix_url](quix_url.png)

Once authenticated, you can access the pre-made dashboard by navigating to "dashboards" 
from the top left menu (by clicking on the grafana icon).

To learn more about how to use Grafana, be sure to check out their docs.