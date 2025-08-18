from prometheus_client import Counter, CollectorRegistry, push_to_gateway
import time
from threading import Thread
import traceback
from prometheus_client.exposition import basic_auth_handler


class MetricsService:

    def __init__(
        self,
        replica_name: str,
        consumer_group: str,
        workspace_id: str,
        gateway_proxy_url: str,
        gateway_proxy_password: str,
    ):
        self.registry = CollectorRegistry()
        self.replica_name = replica_name
        self.consumer_group = consumer_group
        self.workspace_id = workspace_id
        self._url = gateway_proxy_url
        self._password = gateway_proxy_password

        # Prometheus metrics
        self._events_processed = Counter(
            'events_processed_total', 
            'Total events processed',
            ['consumer_group', 'replica_name', 'workspace_id'], 
            registry=self.registry
        )

        # Start Prometheus metrics server on port 8001
        # Start metric pushing in another thread
        pusher_thread = Thread(target=self.push_metrics, daemon=True)
        pusher_thread.start()

    def push_metrics(self):
        """Push aggregated metrics to the Pushgateway at regular intervals."""
        while True:
            try:
                push_to_gateway(
                    self._url,
                    job=self.replica_name,
                    registry=self.registry,
                    handler=lambda url, method, timeout, headers, data: basic_auth_handler(
                        url, method, timeout, headers, data, username='admin', password=self._password
                    )
                )
            except Exception:
                traceback.print_exc()
            finally:
                # Push metrics every 15 seconds, aligns with Prometheus scrape interval
                time.sleep(15)

    def publish_event_processed_metrics(self):
        def publish(row, key, *_):
            self._events_processed.labels(
                workspace_id=self.workspace_id,
                replica_name=self.replica_name,
                consumer_group=self.consumer_group
            ).inc()

        return publish
