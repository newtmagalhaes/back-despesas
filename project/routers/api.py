from .base_router import base_router_factory

APIRouter = base_router_factory('api_db', {'api'})
"""Filter models from 'api' app to 'api_db'"""
