import os
import yaml
import json


class SourceData():
    def __init__(self, name, database, schema, loader, loaded_at_field, freshness, tables, filepath):
        self.name = name
        self.database = database
        self.schema = schema
        self.loader = loader
        self.loaded_at_field = loaded_at_field
        self.freshness = freshness
        self.tables = tables
        self.filepath = filepath

    def to_dict(self):
        return {
            "name": self.name,
            "database": self.database,
            "schema": self.schema,
            "loader": self.loader,
            "loaded_at_field": self.loaded_at_field,
            "freshness": self.freshness,
            "tables": self.tables,
            "filepath": self.filepath
        }

def get_sources_data(folder):
    sources_data = []
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith(".yml") and os.path.basename(file) == 'datasources.yml':
                filepath = os.path.join(root, file)
                with open(filepath, 'r') as f:
                    data = yaml.load(f, Loader=yaml.FullLoader)
                    version = data.get("version")
                    if version == 2:
                        sources = data.get("datasources")
                        for source in sources:
                            name = source.get("name")
                            database = source.get("database")
                            schema = source.get("schema")
                            loader = source.get("loader")
                            loaded_at_field = source.get("loaded_at_field")
                            freshness = source.get("freshness")
                            tables = source.get("tables")

                            source_data = SourceData(name, database, schema, loader, loaded_at_field, freshness, tables, filepath.replace(folder,''))
                            sources_data.append(source_data.to_dict())
    return sources_data

result = get_sources_data("/Users/jicuss/Documents/microk8s/dbt-snowflake")
json.dump(result, open("../../dbt-snowflake/output.json", "w"))
print(result)