# Contributing to airflow-provider-ibm-db2

First off, thank you for considering contributing to this project! 🚀  
We welcome contributions of all kinds — from bug reports and feature requests to documentation and code improvements.

---

## 📝 How to contribute

### 1. Reporting bugs & suggesting features
- Use the [GitHub Issues](https://github.com/YOUR_GITHUB_USERNAME/airflow-provider-ibm-db2/issues) page.
- Clearly describe the problem or idea, steps to reproduce (if applicable), and expected behavior.

### 2. Submitting code
- Fork the repository and create your branch from `main`.
- Write clear commit messages (e.g., `fix: handle SSL parameter in Db2Hook`).
- Add tests for new features or fixes.
- Ensure your code passes linting and tests locally before submitting.

### 3. Pull Requests
- Open a PR against the `main` branch.
- Fill in the PR template (if available).
- Reference related issues (e.g., `Closes #42`).
- Keep PRs focused and concise. Large PRs are harder to review.

---

## 💻 Development setup

```bash
git clone https://github.com/armandospxp/airflow-provider-ibm-db2.git
cd airflow-provider-ibm-db2
python -m venv .venv
source .venv/bin/activate
pip install -e .[dev]
```

Run tests:

```bash
pytest
```

Lint and format:

```bash
ruff check src tests
```

---

## 📐 Coding style
- Follow [PEP8](https://peps.python.org/pep-0008/).
- Use [ruff](https://github.com/astral-sh/ruff) for linting.
- Keep functions small and focused.
- Prefer clear names over abbreviations.

---

## 🔑 Commit message convention
We follow [Conventional Commits](https://www.conventionalcommits.org/):  

- `feat:` — new feature  
- `fix:` — bug fix  
- `docs:` — documentation only changes  
- `test:` — adding or updating tests  
- `chore:` — tooling, CI, build changes  

Example: `feat: add Db2ToParquetOperator`

---

## 🤝 Code of Conduct
Please note that this project follows the [Contributor Covenant](https://www.contributor-covenant.org/).  
Be respectful and constructive in all interactions.

---

## 🙌 Getting help
- Open an [issue](https://github.com/YOUR_GITHUB_USERNAME/airflow-provider-ibm-db2/issues)
- Join discussions (if enabled on GitHub repo)

We’re excited to build **airflow-provider-ibm-db2** together with the community! 🎉
