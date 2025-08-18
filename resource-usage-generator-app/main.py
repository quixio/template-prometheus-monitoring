import random
import time

from metric_scraper import MetricsService
import os
from quixstreams import Application
from quixstreams.sources import Source

RESOURCE_TYPE = os.environ["RESOURCE_TYPE"]
CONSUMER_GROUP = f"{RESOURCE_TYPE}_event_generator"

class ResourceUsageGenerator(Source):

    def generate_usage_event(self, host_id):
        return {
            "resource": RESOURCE_TYPE,
            "host": f"host_{host_id}",
            "used_percent": round(random.random() * 100, 2),
            "time": time.time()
        }

    def run(self):
        """
        Each Source must have a `run` method.

        It will include the logic behind your source, contained within a
        "while self.running" block for exiting when its parent Application stops.

        There a few methods on a Source available for producing to Kafka, like
        `self.serialize` and `self.produce`.
        """
        # either break when the app is stopped, or data is exhausted
        while self.running:
            try:
                for host_id in range(3):
                    event = self.generate_usage_event(host_id)
                    event_serialized = self.serialize(key=event["host"], value=event)
                    self.produce(key=event_serialized.key, value=event_serialized.value)
                    time.sleep(random.random()*3)
            except StopIteration:
                print("Source finished producing messages.")
                return


def main():

    metrics_service = MetricsService(
        os.environ.get("Quix__Deployment__ReplicaName", "local"),
        CONSUMER_GROUP,
        os.environ["Quix__Workspace__Id"],
        os.environ["PUSHGATEWAY_PROXY_URL"],
        os.environ["PUSHGATEWAY_PROXY_PASSWORD"]
    )

    # Setup necessary objects
    app = Application(
        consumer_group=CONSUMER_GROUP,
        auto_offset_reset="latest",
    )
    resource_usage_source = ResourceUsageGenerator(name=f"{CONSUMER_GROUP}-producer")
    sdf = app.dataframe(source=resource_usage_source)
    sdf.update(metrics_service.publish_event_processed_metrics(), metadata=True)
    sdf.print(metadata=True)

    app.run()

if __name__ == "__main__":
    main()
