# Copyright (c) Opendatalab. All rights reserved.

BACKEND_PIPELINE = "pipeline"

DEFAULT_BACKEND = BACKEND_PIPELINE

PUBLIC_BACKEND_CHOICES = (BACKEND_PIPELINE,)
BACKEND_SCHEMA_EXTRA = {"enum": list(PUBLIC_BACKEND_CHOICES)}


def get_backend_choices(include_http_client: bool = True) -> list[str]:
    """按入口配置返回公开 backend 选项，避免各入口重复维护字符串列表。"""
    return list(PUBLIC_BACKEND_CHOICES)


def normalize_backend(backend: str) -> str:
    """将旧 backend 别名规范为当前公开名称，并校验最终名称是否合法。"""
    if backend != BACKEND_PIPELINE:
        raise ValueError(f"Invalid backend. Only '{BACKEND_PIPELINE}' is supported.")
    return backend


def validate_backend(backend: str) -> str:
    """校验公开入口允许的 backend 名称，并返回规范后的后端名称。"""
    return normalize_backend(backend)


def validate_effort(effort: str) -> str:
    """hybrid effort 参数已不再支持。"""
    raise ValueError("effort is no longer supported. Only pipeline backend is available.")
