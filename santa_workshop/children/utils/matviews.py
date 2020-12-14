from django.db import connection


class MaterializedViewModelMixin:
    @classmethod
    def _select__sql(cls) -> str:
        raise NotImplementedError

    @classmethod
    def _create__sql(cls) -> str:
        return f'''
            create materialized view if not exists {cls._meta.db_table} as 
            {cls._select__sql()}
        '''

    @classmethod
    def _refresh__sql(cls) -> str:
        return f'refresh materialized view {cls._meta.db_table}'

    @classmethod
    def _drop__sql(cls) -> str:
        return f'drop materialized view if exists {cls._meta.db_table}'

    @classmethod
    def refresh(cls) -> None:
        with connection.cursor() as cursor:
            cursor.execute(cls._create__sql())
            cursor.execute(cls._refresh__sql()) 