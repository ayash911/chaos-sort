#!/usr/bin/env python3
"""
chaos-sort Demo Script
======================

This script demonstrates all 30+ implemented sorting algorithms across:
1. Standards (Merge, Quick, Heap, Bubble, etc.)
2. Esoteric (Bogo, Stalin, Sleep, Miracle, etc.)
3. Satire (Thanos, Politician, Gaslight, etc.)

Run with visualization or headless mode for comparison.
"""

import sys
import argparse
import time
import random
from typing import List, Callable

import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from chaos_sort import standards, esoteric, satire
from chaos_sort.core.visualizer import Visualizer


def print_header(text: str, char: str = "=") -> None:
    """Print a formatted header."""
    print(f"\n{char * 70}")
    print(f"{text:^70}")
    print(f"{char * 70}\n")


def demo_algorithm(
    name: str, 
    sort_func: Callable, 
    data: List[int], 
    visualize: bool = False,
    **kwargs
) -> None:
    """Generic demonstration function for any algorithm."""
    header_char = kwargs.get('header_char', '=')
    tagline = kwargs.get('tagline', '')
    print_header(f"{name.upper()} SORT - {tagline}", char=header_char)
    
    delay = kwargs.get('delay', 0.01 if visualize else 0.0)
    # Remove delay from kwargs to avoid multiple values error in sort_func
    sort_kwargs = kwargs.copy()
    if 'delay' in sort_kwargs:
        del sort_kwargs['delay']
        
    sort_gen = sort_func(data.copy(), delay=delay, **sort_kwargs)
    
    if visualize:
        viz = Visualizer(
            data=data,
            sort_generator=sort_gen,
            title=f"{name} Sort",
            interval=kwargs.get('interval', 30)
        )
        viz.run()
    else:
        # Headless execution
        step_count = 0
        last_array = []
        stats = {}
        for array, stats in sort_gen:
            step_count += 1
            last_array = array
            if step_count % 100 == 0 and name.lower() in ['bogo', 'bozo', 'bogobogo']:
                print(f"Attempt {step_count}: Still shuffling...")
            if step_count > 5000:
                print("... skipping further output for this headless run ...")
                break
        
        print(f"\nSorting Complete!")
        print(f"Final array: {last_array}")
        
        is_sorted = all(last_array[i] <= last_array[i+1] for i in range(len(last_array) - 1)) if last_array else True
        sorted_status = "\033[92mYES\033[0m" if is_sorted else "\033[91mNO (Satire/Esoteric behavior)\033[0m"
        print(f"Actually Sorted: {sorted_status}")
        
        print(f"Steps/Attempts: {step_count}")
        if 'comparisons' in stats: print(f"Comparisons: {stats['comparisons']:,}")
        if 'swaps' in stats: print(f"Swaps/Mods: {stats['swaps']:,}")
        print(f"Time: {stats.get('time_elapsed', 0.0):.4f}s")


def main():
    """Main demo function."""
    parser = argparse.ArgumentParser(
        description="Chaos Sort Demo - Experience sorting from efficient to absurd"
    )
    
    parser.add_argument(
        '--algorithm', '-a',
        default='all',
        help='Algorithm name (e.g. stalin, merge) or category (standards, esoteric, satire, all)'
    )
    parser.add_argument(
        '--visualize', '-v',
        action='store_true',
        help='Enable matplotlib visualization'
    )
    parser.add_argument(
        '--size', '-s',
        type=int,
        default=12,
        help='Size of the array (default: 12)'
    )
    parser.add_argument(
        '--speed',
        choices=['fast', 'normal', 'slow'],
        default='normal',
        help='Simulation speed (default: normal)'
    )
    
    args = parser.parse_args()
    
    # Speed mapping: (delay, interval)
    speed_map = {
        'fast': (0.0, 1),
        'normal': (0.01, 30),
        'slow': (0.1, 100)
    }
    selected_delay, selected_interval = speed_map[args.speed]
    
    random.seed(42)  # Reproducible chaos
    data = random.sample(range(1, 200), args.size)
    data_small = data[:5] if len(data) > 5 else data
    
    print_header("CHAOS-SORT DEMONSTRATION", char="*")
    print(f"Test Data: {data}")
    print(f"Array Size: {len(data)}")
    print(f"Visualization: {'Enabled' if args.visualize else 'Disabled (headless mode)'}")
    print("Transitions: Automated (Close plot window to continue)")
    
    # 1. Registries
    standard_algos = [
        ('Merge', standards.merge_sort, "Divide & Conquer"),
        ('Quick', standards.quick_sort, "Recursive Partitioning"),
        ('Heap', standards.heap_sort, "Binary Heap"),
        ('Bubble', standards.bubble_sort, "Adjacent Swaps"),
        ('Selection', standards.selection_sort, "Iterative Min-Finding"),
        ('Insertion', standards.insertion_sort, "Sequential Placement"),
        ('Radix', standards.radix_sort, "Digit Sort"),
        ('Counting', standards.counting_sort, "Occurrence Count"),
        ('Shell', standards.shell_sort, "Gap-based Insertion"),
        ('Cocktail', standards.cocktail_sort, "Bidirectional Bubble"),
    ]

    esoteric_algos = [
        ('Stalin', esoteric.stalin_sort, "Comrade, we must purge the disorder."),
        ('Gnome', esoteric.gnome_sort, "A garden gnome's steady progress."),
        ('Pancake', esoteric.pancake_sort, "Flipping our way to the top."),
        ('Stooge', esoteric.stooge_sort, "Recursive madness at O(n^2.7)"),
        ('Slow', esoteric.slow_sort, "Multiply and surrender."),
        ('Sleep', esoteric.sleep_sort, "Elements wake up in their own time."),
        ('Miracle', esoteric.miracle_sort, "Waiting for a cosmic ray..."),
        ('Quantum Bogo', esoteric.quantum_bogo_sort, "Destroying the wrong universes."),
        ('Spaghetti', esoteric.spaghetti_sort, "Physical simulation of pasta rods."),
        ('Bogo', esoteric.bogo_sort, "Pure random hope."),
        ('Bozo', esoteric.bozo_sort, "Randomly swapping until it works."),
        ('BogoBogo', esoteric.bogobogo_sort, "Recursively random suffering."),
    ]

    satire_algos = [
        ('Thanos', satire.thanos_sort, "Perfectly balanced, as all things should be."),
        ('Politician', satire.politician_sort, "Claiming success without doing the work."),
        ('Gaslight', satire.gaslight_sort, "Telling you it was sorted all along."),
        ('Bureaucracy', satire.bureaucracy_sort, "Sorting... pending supervisor approval."),
        ('StackOverflow', satire.stackoverflow_sort, "Copy-pasting your way to a solution."),
        ('Gen Z', satire.genz_sort, "Deleting anything with bad vibes."),
        ('Procrastination', satire.procrastination_sort, "I'll do it tomorrow, probably."),
        ('Intimidation', satire.intimidation_sort, "Agree it's sorted or else."),
        ('Lottery', satire.lottery_sort, "Betting it all on a single guess."),
        ('Philosophical', satire.philosophical_sort, "Does order even matter in an infinite universe?"),
        ('Trust Fund', satire.trust_fund_sort, "Inheriting a sorted array from my parents."),
    ]

    # Filtering logic
    selection = args.algorithm.lower()
    
    # 1. Run Standards
    if selection in ['all', 'standards']:
        for name, func, tagline in standard_algos:
            demo_algorithm(name, func, data.copy(), args.visualize, 
                          tagline=tagline, delay=selected_delay, interval=selected_interval)
    
    # 2. Run Esoteric
    if selection in ['all', 'esoteric']:
        print_header("ENTERING THE REALM OF ESOTERIC SORTS", char="!")
        for name, func, tagline in esoteric_algos:
            test_data = data_small.copy() if name in ["Stooge", "Slow", "BogoBogo", "Bogo", "Bozo"] else data.copy()
            demo_algorithm(name, func, test_data, args.visualize, 
                          tagline=tagline, header_char="!", delay=selected_delay, interval=selected_interval)
            
    # 3. Run Satire
    if selection in ['all', 'satire']:
        print_header("ENTERING THE REALM OF SATIRICAL SORTS", char="~")
        for name, func, tagline in satire_algos:
            demo_algorithm(name, func, data.copy(), args.visualize, 
                          tagline=tagline, header_char="~", delay=selected_delay, interval=selected_interval)

    # 4. Specific Algorithm
    all_all = standard_algos + esoteric_algos + satire_algos
    dict_all = {a[0].lower(): a for a in all_all}
    if selection in dict_all:
        name, func, tagline = dict_all[selection]
        test_data = data_small.copy() if name in ["Stooge", "Slow", "BogoBogo", "Bogo", "Bozo"] else data.copy()
        demo_algorithm(name, func, test_data, args.visualize, 
                      tagline=tagline, delay=selected_delay, interval=selected_interval)

    print_header("Demo Complete! Thanks for watching the chaos unfold.", char="*")


if __name__ == "__main__":
    main()
