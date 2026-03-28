"""
chaos-sort: A Unified Framework for 30+ Sorting Algorithms
===========================================================

From the efficient to the absurd, from the classic to the satirical.

This library provides a comprehensive collection of sorting algorithms with
a unified generator-based interface for real-time visualization and analysis.

Quick Start
-----------
    >>> from chaos_sort.standards.merge_sort import merge_sort
    >>> from chaos_sort.core.visualizer import Visualizer
    >>> 
    >>> data = [64, 34, 25, 12, 22, 11, 90]
    >>> sort_gen = merge_sort(data)
    >>> viz = Visualizer(data, sort_gen, title="Merge Sort")
    >>> viz.run()

Modules
-------
- standards: Classic sorting algorithms (Bubble, Merge, Quick, Heap, etc.)
- esoteric: Historically terrible algorithms (Bogo, Sleep, Miracle, etc.)
- satire: Pure satirical algorithms (Thanos, Politician, Gaslight, etc.)
- core: Visualization and utility framework

Author: The Chaos Collective
License: MIT
"""

__version__ = "0.1.0"
__author__ = "The Chaos Collective"
__license__ = "MIT"

# Core imports
from chaos_sort.core.visualizer import Visualizer, ComparisonVisualizer
from chaos_sort import standards, esoteric, satire

__all__ = [
    'Visualizer',
    'ComparisonVisualizer',
    'standards',
    'esoteric',
    'satire',
]