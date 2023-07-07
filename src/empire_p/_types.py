from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any


@dataclass(frozen=True, slots=True)
class Args:
    root_path: str
    project_name: str = ''
    project_description: str = ''
    project_version: str = ''
    project_code_name: str = ''
    minimum_python_version: str = ''
    classifiers: list[str] = field(default_factory=list)
    requirements: list[str] = field(default_factory=list)

    @classmethod
    def from_parsed_args_namespace(cls, root_path: str, args: Any) -> Args:
        return cls(
            root_path=root_path,
            #project_name=args.project_name,
            #project_description=args.project_description,
            #project_version=args.project_version,
            #project_code_name=args.project_code_name,
            #minimum_python_version=args.minimum_python_version,
            #classifiers=args.classifiers,
            #requirements=args.requirements
        )
