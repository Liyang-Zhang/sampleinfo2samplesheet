# sampleinfo2samplesheet

## dev

Prerequisites

- [Poetry](https://python-poetry.org/)
- [pyenv](https://github.com/pyenv/pyenv)

```bash
git clone https://github.com/Liyang-Zhang/sampleinfo2samplesheet.git
cd sampleinfo2samplesheet

pyenv install 3.12.0
poetry env use $(pyenv which python)

cat <<EOF > ".env"
export GPG_TTY=\$(tty)
export PYTHON_KEYRING_BACKEND=keyring.backends.null.Keyring
source \$(poetry env info --path)/bin/activate
EOF

source .env
poetry install
pre-commit install
pre-commit run --all-files
```
