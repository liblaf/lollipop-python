import re
import shutil
import subprocess as sp
from pathlib import Path

from toml_sort import tomlsort


def main(files: list[Path]) -> None:
    for fpath in files:
        original_text: str = fpath.read_text()
        ts = tomlsort.TomlSort(
            original_text,
            sort_config=tomlsort.SortConfiguration(
                tables=True,
                table_keys=True,
                inline_tables=True,
                inline_arrays=True,
                ignore_case=True,
            ),
        )
        text: str = ts.sorted()
        text = fix_schema_comments(text)
        if (taplo_exe := shutil.which("taplo")) is not None:
            proc: sp.CompletedProcess[str] = sp.run(
                [taplo_exe, "fmt", "-"],
                stdout=sp.PIPE,
                check=True,
                input=text,
                text=True,
            )
            text = proc.stdout
        if text != original_text:
            fpath.write_text(text)


def fix_schema_comments(text: str) -> str:
    text = re.sub(r"^# :schema ", "#:schema ", text)
    return text
