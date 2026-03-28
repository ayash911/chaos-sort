# Publishing Chaos Sort

Follow these steps to package and distribute `chaos-sort` to the Python Package Index (PyPI).

## 1. Prepare for Distribution

Ensure you have the build tools installed:

```bash
pip install --upgrade build twine
```

## 2. Build the Package

Run the build module in the project root:

```bash
python -m build
```

This will create a `dist/` directory containing:
- `chaos-sort-0.1.0.tar.gz` (Source Distribution)
- `chaos_sort-0.1.0-py3-none-any.whl` (Built Wheel)

## 3. Upload to PyPI

### To TestPyPI (Recommended first)
```bash
python -m twine upload --repository testpypi dist/*
```

### To Official PyPI
```bash
python -m twine upload dist/*
```

## 4. Installation for Users

Once published, anyone can install it via:

```bash
pip install chaos-sort
```

## 5. Usage Example

```python
import chaos_sort
from chaos_sort.standards.quick_sort import quick_sort
from chaos_sort.core.visualizer import Visualizer

# 1. Custom usage
data = [10, 5, 2, 3, 7]
for arr, stats in quick_sort(data):
    # arr is the state at this step
    # stats is a dict with comparisons, swaps, etc.
    pass

# 2. visualizer usage
sort_gen = quick_sort(data)
viz = Visualizer(data, sort_gen, title="Quick Sort Example")
viz.run()
```
