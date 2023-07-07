import os
from typing import Callable, TypeVar


ScanDirectoryResult = TypeVar('ScanDirectoryResult')

class PredefinedCallbacks:
    @staticmethod
    def files_only(
        entry_path: str,
        is_directory: bool,
        dir_entry: os.DirEntry,
        kwargs_dict: dict
    ) -> ScanDirectoryResult:
        return entry_path if not is_directory else None


def scan_directory(
    path: str,
    *,
    recursive: bool = False,
    on_entry_found_callback: Callable[[str, bool, os.DirEntry, dict], ScanDirectoryResult] = None,
    **on_entry_found_callback_kwargs
) -> list[str]:
    if on_entry_found_callback is None:
        on_entry_found_callback = lambda w, x, y, z: w

    def _recursion(path_: str) -> list[ScanDirectoryResult]:
        results: list[ScanDirectoryResult] = []
        f: os.DirEntry
        for f in os.scandir(path_):
            if recursive and f.is_dir():
                results.extend(_recursion(f.path))

            result: ScanDirectoryResult = on_entry_found_callback(f.path, f.is_dir(), f, on_entry_found_callback_kwargs)
            if result is not None:
                results.append(result)

        return results

    return _recursion(path)

