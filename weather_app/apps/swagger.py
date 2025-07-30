import yaml
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiTypes

TYPE_MAP = {
    "string": str,
    "integer": int,
    "number": float,
    "boolean": bool,
}


def convert_parameter(param_dict):
    type_str = param_dict.get("schema", {}).get("type", "string")
    py_type = TYPE_MAP.get(type_str, str)
    return OpenApiParameter(
        name=param_dict["name"],
        location=param_dict.get("in", "query"),
        description=param_dict.get("description"),
        required=param_dict.get("required", False),
        type=py_type,
    )


def extend_schema_from_yaml(yaml_file_path, operation_id=None):
    def decorator(view_func):
        with open(yaml_file_path, "r") as file:
            schema = yaml.safe_load(file)

        summary = schema.get("summary", "")
        description = schema.get("description", "")
        responses = schema.get("responses", {})
        tags = schema.get("tags")
        parameters_raw = schema.get("parameters", [])

        parameters = [convert_parameter(p) for p in parameters_raw]

        extend_schema_kwargs = {
            "operation_id": operation_id,
            "summary": summary,
            "description": description,
            "responses": responses,
            "parameters": parameters,
        }

        if tags:
            extend_schema_kwargs["tags"] = tags

        # Apply extend_schema to the view function
        return extend_schema(**extend_schema_kwargs)(view_func)

    return decorator
