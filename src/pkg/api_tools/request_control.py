import hashlib
import time
from multiprocessing import Lock
from typing import Dict

from src.pkg.api_tools import exceptions, structures


class NekoAPIDelayer:
    def __init__(self):
        self._client_url_delay_map: Dict[str, structures.Delay] = {}
        self._label_endpoint_map: Dict[str, structures.Endpoint] = {}

    def get_endpoint(self, label: str) -> structures.Endpoint:
        return self._label_endpoint_map[label]

    def add_endpoint(
        self,
        label: str,
        url: str,
        delay: float,
        key: str = "",
    ) -> structures.Endpoint:
        if label in self._label_endpoint_map:
            raise exceptions.UrlLabelAlreadyExistsException
        endpoint = structures.Endpoint(
            url=url,
            delay=structures.Delay(
                step=delay,
                set_actual_lock=Lock(),
                get_actual_lock=Lock(),
            ),
            label=label,
        )
        self.register_client_delay(endpoint=endpoint, key=key)
        self.register_endpoint_label(endpoint=endpoint)
        return endpoint

    def register_client_delay(self, endpoint: structures.Endpoint, key: str):
        hash_key = hashlib.md5((endpoint.url + key).encode()).hexdigest()
        self._client_url_delay_map[hash_key] = structures.Delay(
            step=endpoint.delay.step,
            set_actual_lock=Lock(),
            get_actual_lock=Lock(),
        )
        self._client_url_delay_map[hash_key].set_actual_lock.acquire()

    def register_endpoint_label(self, endpoint: structures.Endpoint):
        self._label_endpoint_map[endpoint.label] = endpoint

    def get_actual_request_time(self, search_key) -> float:
        self._client_url_delay_map[search_key].get_actual_lock.acquire()
        actual = self._client_url_delay_map[search_key].actual
        self._client_url_delay_map[search_key].set_actual_lock.release()
        return actual

    def set_actual_request_time(self, search_key, actual: float):
        self._client_url_delay_map[search_key].set_actual_lock.acquire()
        self._client_url_delay_map[search_key].actual = actual
        self._client_url_delay_map[search_key].get_actual_lock.release()

    def request_delay(self, endpoint: structures.Endpoint, key: str = ""):
        search_key = hashlib.md5((endpoint.url + key).encode()).hexdigest()
        if search_key not in self._client_url_delay_map:
            self.register_client_delay(endpoint=endpoint, key=key)
        now = time.time()
        if (
            now - self.get_actual_request_time(search_key=search_key)
            < self._client_url_delay_map[search_key].step
        ):
            time.sleep(self._client_url_delay_map[search_key].step)
        actual = time.time()
        self.set_actual_request_time(search_key=search_key, actual=actual)
