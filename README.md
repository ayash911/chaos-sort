# Chaos Sort

A educational (and satirical) library of sorting algorithms, ranging from the classically efficient to the intentionally disastrous.

## Features

- **Standard Algorithms**: Classic implementations (Merge, Quick, Heap, etc.)
- **Esoteric Algorithms**: Real-world "terrible" algorithms (Bogo, Bozo, etc.)
- **Satirical Algorithms**: Custom parodies of tech culture and society (Thanos Sort, etc.)
- **Real-time Visualization**: Animated bar charts with live statistics using Matplotlib
- **Generator-based API**: Easily hook into the sorting process for your own visualizations
- **Speed Control**: Toggle between fast, normal, and slow simulation speeds

## Installation

Install the stable version from PyPI:

```bash
pip install chaos-sort
```

Or clone the repository for development:

```bash
git clone https://github.com/ayash911/chaos-sort.git
cd chaos-sort
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -e .
```

## Quick Start

Run the interactive demo to see the chaos in action:

```bash
python examples/demo.py -v
```

To run a specific algorithm with visualization and custom speed:

```bash
python examples/demo.py --algorithm merge --visualize --speed fast
```

## The Roster

### Module A: Standards (The Efficient)

Classic, well-known sorting algorithms.

| Algorithm | Complexity | Stable | Status |
|-----------|-----------|--------|--------|
| Bubble Sort | O(n^2) | Yes | Implemented |
| Selection Sort | O(n^2) | No | Implemented |
| Insertion Sort | O(n^2) | Yes | Implemented |
| Merge Sort | O(n log n) | Yes | Implemented |
| Quick Sort | O(n log n) avg | No | Implemented |
| Heap Sort | O(n log n) | No | Implemented |
| Radix Sort | O(nk) | Yes | Implemented |
| Counting Sort | O(n+k) | Yes | Implemented |
| Shell Sort | O(n log n) | No | Implemented |
| Cocktail Shaker Sort | O(n^2) | Yes | Implemented |

### Module B: Esoteric (The Terrible)

Historically awful algorithms. **Educational nightmares with astronomical complexity.**

| Algorithm | Complexity | Description | Status |
|-----------|-----------|-------------|--------|
| Bogo Sort | O((n+1)!) | Random shuffle until sorted | Implemented |
| Bozo Sort | O(n*n!) | Random swap until sorted | Implemented |
| Stalin Sort | O(n) | Delete elements that are out of order | Implemented |
| Sleep Sort | O(max(input)) | Thread sleep based on value | Implemented |
| Miracle Sort | O(inf) | Wait for cosmic rays to sort the array | Implemented |
| Slow Sort | O(n^(log n)) | Multiply and surrender | Implemented |
| Quantum Bogo Sort | O(1)* | Destroy universe if not sorted | Implemented |
| Pancake Sort | O(n^2) | Only reverse prefixes | Implemented |
| Stooge Sort | O(n^2.7) | Recursive 2/3 overlapping | Implemented |
| Gnome Sort | O(n^2) | Garden gnome sorting | Implemented |
| Spaghetti Sort | O(n) | Physical simulation | Implemented |
| BogoBogo Sort | O(inf^2) | Recursively verify Bogo Sort | Implemented |

### Module C: Satire (The Absurd)

Custom algorithms that satirize tech culture, society, and optimization obsession.

| Algorithm | Parodies | Description | Status |
|-----------|----------|-------------|--------|
| Thanos Sort | MCU | Delete half until sorted | Implemented |
| Politician Sort | Politics | Declare it sorted, blame predecessor | Implemented |
| Procrastination Sort | Work culture | Wait 5 minutes, call .sort() | Implemented |
| Intimidation Sort | Gaslighting | Claim it's sorted, pressure user | Implemented |
| Gaslight Sort | Toxic behavior | Change user's original array | Implemented |
| Bureaucracy Sort | Red tape | 3-second approval per swap | Implemented |
| StackOverflow Sort | Dev culture | Web scrape sorting tutorial | Implemented |
| Gen Z Sort | Generational | Delete elements with "bad vibes" | Implemented |
| Lottery Sort | Gambling | 1/14M chance to actually sort | Implemented |
| Philosophical Sort | Philosophy | Question the nature of order | Implemented |
| Trust Fund Sort | Privilege | Inherit a sorted array | Implemented |

## Visualization Examples

The `Visualizer` class provides real-time animated bar charts:

```python
from chaos_sort.core.visualizer import Visualizer
from chaos_sort.esoteric.bogo_sort import bogo_sort

data = [5, 2, 8, 1, 9]  # KEEP IT SMALL for Bogo!
sort_gen = bogo_sort(data, max_iterations=1000)

viz = Visualizer(
    data=data,
    sort_generator=sort_gen,
    title="Bogo Sort: Pray to RNG",
    interval=50,  # ms between frames
    figsize=(12, 7)
)

viz.run()
```

### What You See:

- **Live bar chart** showing array state
- **Sorted validation** status (actually sorted or not)
- **Statistics panel** showing comparisons, swaps, time, and ops

## Advanced Usage

### Custom Parameters

Every sorting algorithm accepts `**kwargs` for customization:

```python
# Add dramatic delays
thanos_sort(data, delay=0.5, snap_quota=0.5)

# Control speed via demo
python examples/demo.py --speed fast
```

## Project Structure

```
chaos-sort/
├── pyproject.toml           # Project configuration
├── README.md                # This file
├── LICENSE                  # MIT License
├── chaos_sort/
│   ├── __init__.py
│   ├── core/
│   │   ├── __init__.py
│   │   └── visualizer.py   # Visualization framework
│   ├── standards/
│   │   ├── __init__.py
│   │   ├── ...
│   ├── esoteric/
│   │   ├── __init__.py
│   │   ├── ...
│   └── satire/
│       ├── __init__.py
│       └── ...
├── tests/
│   ├── base_test.py        # Base test class
│   ├── ...
└── examples/
    ├── demo.py             # Main project demo
    └── ...
```

## Contributing

We welcome contributions! Implement a planned algorithm, create new satirical ones, or improve the visualizations.

## License

MIT License - see [LICENSE](LICENSE) file for details.

## Contact

- **Issues**: [GitHub Issues](https://github.com/ayash911/chaos-sort/issues)
- **Email**: ya828197@gmail.com

---

"In a world of O(n log n), be O((n+1)!)"