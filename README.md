# Chaos Sort: The Art of Inefficient Sorting

A comprehensive collection of sorting algorithms, ranging from the classically optimized to the intentionally absurd. Chaos Sort is designed for educational exploration, performance benchmarking (of the worst kind), and a satirical look at computational complexity.

## Overview

Chaos Sort bridges the gap between academic rigor and algorithmic performance art. Whether you're studying the efficiency of `Merge Sort` or the cosmic patience required for `Miracle Sort`, this library provides a unified, generator-based API to observe, visualize, and understand the mechanics of order and chaos.

## Key Features

- **Standard Algorithms**: Impeccable implementations of industry standards including Quick, Merge, and Heap sorts.
- **Esoteric Explorations**: A deep dive into historically "terrible" algorithms like Bogo, Bozo, and Sleep sorts.
- **Satirical Implementations**: Modern parodies of tech culture and social dynamics, from Thanos Sort to Procrastination Sort.
- **Dynamic Visualization**: Real-time Animated bar charts with live statistics using Matplotlib.
- **Extensible API**: Hook into the sorting process using Python generators for custom visualizations.

## Installation

\`\`\`bash
pip install chaos-sort
\`\`\`

For development and exploration:

\`\`\`bash
git clone https://github.com/ayash911/chaos-sort.git
cd chaos-sort
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -e .
\`\`\`

## Quick Start

Launch the interactive demo to witness the chaos:

\`\`\`bash
python examples/demo.py --visualize
\`\`\`

To visualize a specific algorithm at custom speeds:

\`\`\`bash
python examples/demo.py --algorithm merge --visualize --speed fast
\`\`\`

## The Roster

### Standard Algorithms (The Efficient)

These are the fundamental building blocks of computer science, optimized for real-world utility.

| Algorithm | Complexity | Stable |
|-----------|-----------|--------|
| Bubble Sort | O(n²) | Yes |
| Selection Sort | O(n²) | No |
| Insertion Sort | O(n²) | Yes |
| Merge Sort | O(n log n) | Yes |
| Quick Sort | O(n log n) avg | No |
| Heap Sort | O(n log n) | No |
| Radix Sort | O(nk) | Yes |
| Counting Sort | O(n+k) | Yes |
| Shell Sort | O(n log n) | No |
| Cocktail Shaker Sort | O(n²) | Yes |

### Esoteric Algorithms (The Terrible)

These algorithms represent the outer limits of computational inefficiency, often used as cautionary tales or mathematical curiosities.

| Algorithm | Complexity | Description |
|-----------|-----------|-------------|
| Bogo Sort | O((n+1)!) | Randomly shuffle until order emerges. |
| Bozo Sort | O(n·n!) | Pick two random elements and swap. |
| Stalin Sort | O(n) | Eliminate any element not in its place. |
| Sleep Sort | O(max(input)) | Utilize system sleep based on value. |
| Miracle Sort | O(∞) | Wait for an external event (e.g., cosmic ray) to sort. |
| Slow Sort | O(n^(log n)) | A multiply-and-surrender strategy. |
| Quantum Bogo Sort | O(1) | Assume the universe collapses if not sorted. |
| Pancake Sort | O(n²) | Sort by reversing prefixes. |
| Stooge Sort | O(n².⁷) | A recursive 2/3 overlapping approach. |
| Gnome Sort | O(n²) | Moving elements like a garden gnome. |
| Spaghetti Sort | O(n) | A physical simulation of sorting. |
| BogoBogo Sort | O(∞²) | Recursively verify the result of a Bogo Sort. |

### Satirical Algorithms (The Absurd)

Critiques of modern work culture, social dynamics, and the tech industry's obsession with "optimization."

| Algorithm | Parody | Strategy |
|-----------|----------|-------------|
| Thanos Sort | MCU | Snap fingers and delete half the array. |
| Politician Sort | Politics | Declare victory and shift the blame. |
| Procrastination Sort | Work Culture | Delay for 5 minutes, then use a standard sort. |
| Intimidation Sort | Gaslighting | Pressure the user into believing it’s sorted. |
| Gaslight Sort | Toxic Behavior | Secretly alter the user's input. |
| Bureaucracy Sort | Red Tape | Impose mandatory delays for every swap. |
| StackOverflow Sort | Dev Culture | Attempt to scrape a solution from the web. |
| Gen Z Sort | Generational | Remove elements with "bad vibes." |
| Lottery Sort | Gambling | Rely on a 1-in-14-million chance for success. |
| Philosophical Sort | Philosophy | Contemplate the inherent meaning of "order." |
| Trust Fund Sort | Privilege | Inherit a pre-sorted array from the system. |

## Visualization

The \`Visualizer\` class provides a high-fidelity window into the sorting process:

\`\`\`python
from chaos_sort.core.visualizer import Visualizer
from chaos_sort.esoteric.bogo_sort import bogo_sort

# Keeping it small for demonstration
data = [5, 2, 8, 1, 9] 
sort_gen = bogo_sort(data, max_iterations=1000)

viz = Visualizer(
    data=data,
    sort_generator=sort_gen,
    title="Bogo Sort: Stochastic Order",
    interval=50,
    figsize=(12, 7)
)

viz.run()
\`\`\`

---
"In a world of O(n log n), dare to be O((n+1)!)"
