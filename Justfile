import ".config/copier/python.just"

default: gen-init lint

compile:
    pyinstaller --noconfirm --clean --onefile --name "lollipop" \
        --collect-all "liblaf.grapes" \
        --collect-all "liblaf.lollipop" \
        --optimize 2 --console \
        "src/liblaf/lollipop/__main__.py"

help: help-markdown

help-markdown:
    mkdir --parents --verbose -- "docs/markdown/"
    typer liblaf.lollipop utils docs --output "docs/markdown/lollipop.md"
