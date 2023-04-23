from urllib.parse import urlparse
from .models import Service

class Route:
    def __init__(self) -> None:
        services = Service.query.all()
        self._slug_list = [service.slug.replace('/','') for service in services]
    
    def check_route(self, route: str) -> bool:
        if self.get_slug(route) in self._slug_list:
            return True
        return False
    
    def get_slug(self, url: str) -> str:
        parsed_url = urlparse(url)
        path_parts = parsed_url.path.split("/")  # 将路径拆分为各个部分
        first_path = path_parts[1] if len(path_parts) > 1 else "" # 获取第一个 path
        return first_path

    def get_path(self, url: str) -> str:
        parsed_url = urlparse(url)
        path_parts = parsed_url.path.split("/")  # 将路径拆分为各个部分
        path = '/'.join(path_parts[2:]) if len(path_parts) > 2 else "" # 获取第一个 path
        return path
