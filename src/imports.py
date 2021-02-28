import importlib
import sys


def modify_and_import(module_name, package, modification_func):
    spec = importlib.util.find_spec(module_name, package)
    source = spec.loader.get_source(module_name)
    new_source = modification_func(source)
    breakpoint()
    module = importlib.util.module_from_spec(spec)
    codeobj = compile(new_source, module.__spec__.origin, 'exec')
    exec(codeobj, module.__dict__)
    sys.modules[module_name] = module
    return module

my_module = modify_and_import(
    "airflow_kubernetes_job_operator",
    None,
    lambda src: src.replace(
        "from airflow.operators import BaseOperator",
        "from airflow.models.baseoperator import BaseOperator"
    )
)