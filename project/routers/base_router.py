from abc import ABC, abstractmethod

from django.db.models import Model


class AbstractDBRouter(ABC):
    @property
    @abstractmethod
    def route_app_labels(self) -> set[str]: ...

    @property
    @abstractmethod
    def db_key(self) -> str: ...

    @abstractmethod
    def db_for_read(self, model: Model, **hints) -> str|None: ...

    @abstractmethod
    def db_for_write(self, model: Model, **hints) -> str|None: ...

    @abstractmethod
    def allow_migrate(self, db_key: str, app_label: str, model_name=None, **hints) -> bool|None: ...

    @abstractmethod
    def allow_relation(self, obj1: Model, obj2: Model, **hints) -> bool|None: ...


def base_router_factory(db_key: str, app_labels: set[str]):
    class _BaseRouter(AbstractDBRouter):
        @property
        def db_key(self):
            return db_key

        @property
        def route_app_labels(self):
            return app_labels

        def db_for_read(self, model, **hints) -> str|None:
            if model._meta.app_label in self.route_app_labels:
                return self.db_key
            return None

        def db_for_write(self, model, **hints) -> str|None:
            if model._meta.app_label in self.route_app_labels:
                return self.db_key
            return None

        def allow_relation(self, obj1, obj2, **hints) -> bool|None:
            """Allow Relation if both objects are from same app_label"""
            return (
                obj1._meta.app_label == obj2._meta.app_label
                and obj1._meta.app_label in self.route_app_labels
            ) or None

        def allow_migrate(self, db_key, app_label, model_name=None, **hints) -> bool|None:
            if app_label in self.route_app_labels:
                return db_key == self.db_key
            return None

    return _BaseRouter