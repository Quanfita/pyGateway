from .models import Service
from itertools import cycle
import random


class Balancer:
    def __init__(self, mode=None) -> None:
        self._pool_map = {
            'cycle': self._cycle_server_pool,
            'random': self._normal_server_pool,
            'cycle_weight': self._cycle_weight_server_pool,
            'random_weight': self._weight_server_pool
        }
        self._method_map = {
            'cycle': self._cycle_mode,
            'random': self._random_mode,
            'cycle_weight': self._cycle_weight_mode,
            'random_weight': self._random_weight_mode
        }
        
        if mode:
            self.set_mode(mode)
    
    def set_service_by_slug(self, slug: str) -> None:
        self._slug = slug
        self._pool = self._pool_fun()
    
    def _normal_server_pool(self):
        service = Service.query.filter_by(slug=self._slug).first()
        return [f'{server.host}:{server.port}' for server in service.servers]
    
    def _weight_server_pool(self):
        service = Service.query.filter_by(slug=self._slug).first()
        return [f'{server.host}:{server.port}' for server in service.servers  for _ in range(server.process_num)]
    
    def _cycle_server_pool(self):
        service = Service.query.filter_by(slug=self._slug).first()
        return cycle([f'{server.host}:{server.port}' for server in service.servers])
    
    def _cycle_weight_server_pool(self):
        service = Service.query.filter_by(slug=self._slug).first()
        return cycle([f'{server.host}:{server.port}' for server in service.servers  for _ in range(server.process_num)])
    
    def set_mode(self, mode: str) -> None:
        self._method = self._method_map.get(mode, self._random_mode)
        self._pool_fun = self._pool_map.get(mode, self._normal_server_pool)
    
    def get_server(self) -> str:
        return self._method()
    
    def _cycle_mode(self) -> str:
        return next(self._cycle_server_pool())
    
    def _random_mode(self) -> str:
        return random.choice(self._normal_server_pool())
    
    def _cycle_weight_mode(self) -> str:
        return next(self._cycle_weight_server_pool())
    
    def _random_weight_mode(self) -> str:
        return random.choice(self._weight_server_pool())
