"""
chaos_sort.core.visualizer
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Real-time visualization framework for sorting algorithms using matplotlib.animation.
Supports any generator-based sorting algorithm that yields (data, stats) tuples.
"""

import time
from typing import Generator, Dict, List, Optional, Tuple, Any
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.patches import Rectangle
from matplotlib.widgets import Button


class Visualizer:
    """
    Real-time animated visualizer for sorting algorithms.
    
    This class takes any sorting generator from the chaos_sort library and renders
    a live bar chart showing the sorting process step by step.
    
    Parameters
    ----------
    data : List[int]
        The initial array to be sorted
    sort_generator : Generator
        A generator function that yields (data, stats) tuples at each step
    title : str, optional
        Custom title for the visualization window
    interval : int, optional
        Milliseconds between animation frames (default: 50)
    save_path : str, optional
        If provided, saves the animation to this file path
    figsize : Tuple[int, int], optional
        Figure size in inches (default: (12, 7))
    """
    
    def __init__(
        self,
        data: List[int],
        sort_generator: Generator[Tuple[List[int], Dict[str, Any]], None, None],
        title: str = "Chaos Sort Visualization",
        interval: int = 50,
        save_path: Optional[str] = None,
        figsize: Tuple[int, int] = (12, 7)
    ):
        self.original_data = data.copy()
        self.sort_generator = sort_generator
        self.title = title
        self.interval = interval
        self.save_path = save_path
        self.figsize = figsize
        
        # Animation state
        self.current_data: List[int] = data.copy()
        self.current_stats: Dict[str, Any] = {
            'comparisons': 0,
            'swaps': 0,
            'time_elapsed': 0.0,
            'theoretical_time': None,
            'current_operation': 'Initializing...'
        }
        self.frame_count = 0
        self.animation_complete = False
        
        # Setup figure and axes
        self.fig, self.ax = plt.subplots(figsize=figsize)
        self.fig.canvas.manager.set_window_title(title)
        
        # Initialize the bar plot
        self.bars = None
        self.stats_text = None
        
    def _init_animation(self) -> List[Any]:
        """Initialize the animation - called by FuncAnimation."""
        self.ax.clear()
        self.ax.set_xlim(-1, len(self.current_data))
        self.ax.set_ylim(0, max(self.current_data) * 1.1 if self.current_data else 1)
        self.ax.set_xlabel('Index', fontsize=12)
        self.ax.set_ylabel('Value', fontsize=12)
        
        # Create initial bars
        x_pos = np.arange(len(self.current_data))
        self.bars = self.ax.bar(x_pos, self.current_data, color='steelblue', edgecolor='black')
        
        # Setup stats display
        stats_str = self._format_stats()
        self.stats_text = self.ax.text(
            0.02, 0.98, stats_str,
            transform=self.ax.transAxes,
            verticalalignment='top',
            bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8),
            fontsize=10,
            family='monospace'
        )
        
        return list(self.bars) + [self.stats_text]
    
    def _update_frame(self, frame: int) -> List[Any]:
        """Update function called for each animation frame."""
        if self.animation_complete:
            return list(self.bars) + [self.stats_text]
        
        try:
            # Get next state from generator
            self.current_data, self.current_stats = next(self.sort_generator)
            self.frame_count += 1
            
            # Update bar heights and colors
            curr_max = max(self.current_data) if self.current_data else 1
            for i, bar in enumerate(self.bars):
                if i < len(self.current_data):
                    val = self.current_data[i]
                    bar.set_height(val)
                    # Color gradient based on value
                    normalized = val / curr_max
                    bar.set_color(plt.cm.viridis(normalized))
                    bar.set_visible(True)
                else:
                    # Element was eliminated (e.g. Thanos Sort)
                    bar.set_height(0)
                    bar.set_visible(False)
            
            # Update stats text
            self.stats_text.set_text(self._format_stats())
            
        except StopIteration:
            # Sorting complete
            self.animation_complete = True
            self.current_stats['current_operation'] = '[DONE] COMPLETE'
            self.stats_text.set_text(self._format_stats())
            
            # Final color: green for sorted survivors
            for i, bar in enumerate(self.bars):
                if i < len(self.current_data):
                    bar.set_color('limegreen')
                else:
                    bar.set_visible(False)
        
        return list(self.bars) + [self.stats_text]
    
    def _format_stats(self) -> str:
        """Format statistics for display."""
        stats = self.current_stats
        lines = [
            f"+--- {self.title} ---+",
            f"| Comparisons: {stats.get('comparisons', 0):,}",
            f"| Swaps/Mods:  {stats.get('swaps', 0):,}",
            f"| Time:        {stats.get('time_elapsed', 0):.3f}s",
        ]
        
        if stats.get('theoretical_time'):
            lines.append(f"| Complexity:  {stats['theoretical_time']}")
        
        lines.append(f"| Frame:       {self.frame_count:,}")
        lines.append(f"| Status:      {stats.get('current_operation', 'Running...')}")
        
        # Add a simple progress bar if elements are being sorted
        if 'original_size' in stats and len(self.current_data) < stats['original_size']:
             progress = (stats['original_size'] - len(self.current_data)) / stats['original_size']
             bar = "#" * int(progress * 20) + "-" * (20 - int(progress * 20))
             lines.append(f"| Balance:     [{bar}]")

        lines.append("+" + "-" * (len(lines[0]) - 2) + "+")
        
        return '\n'.join(lines)
    
    def run(self, repeat: bool = False) -> None:
        """
        Start the visualization animation.
        
        Parameters
        ----------
        repeat : bool, optional
            Whether to loop the animation (default: False)
        """
        anim = FuncAnimation(
            self.fig,
            self._update_frame,
            init_func=self._init_animation,
            interval=self.interval,
            blit=False,
            repeat=repeat,
            cache_frame_data=False
        )
        
        if self.save_path:
            print(f"Saving animation to {self.save_path}...")
            anim.save(self.save_path, writer='pillow', fps=1000//self.interval)
            print("Animation saved!")
        
        plt.tight_layout()
        plt.show()
        
        # Explicitly close the figure to free resources and prevent Segfaults on macOS
        plt.close(self.fig)
        
    def run_headless(self, max_frames: int = 10000) -> Dict[str, Any]:
        """
        Run sorting without visualization (for testing/benchmarking).
        
        Parameters
        ----------
        max_frames : int, optional
            Maximum number of frames to process (default: 10000)
            
        Returns
        -------
        Dict[str, Any]
            Final statistics dictionary
        """
        frame = 0
        try:
            while frame < max_frames:
                self.current_data, self.current_stats = next(self.sort_generator)
                frame += 1
        except StopIteration:
            pass
        
        return self.current_stats


class ComparisonVisualizer:
    """
    Side-by-side comparison of multiple sorting algorithms.
    
    Runs multiple sorting algorithms on the same data simultaneously and
    displays them in a grid for performance comparison.
    """
    
    def __init__(
        self,
        data: List[int],
        sort_generators: Dict[str, Generator],
        figsize: Tuple[int, int] = (16, 10)
    ):
        """
        Parameters
        ----------
        data : List[int]
            The array to sort
        sort_generators : Dict[str, Generator]
            Dictionary mapping algorithm names to their generators
        figsize : Tuple[int, int], optional
            Figure size in inches
        """
        self.data = data.copy()
        self.sort_generators = sort_generators
        self.figsize = figsize
        
        # Calculate grid layout
        n_algorithms = len(sort_generators)
        self.n_cols = min(3, n_algorithms)
        self.n_rows = (n_algorithms + self.n_cols - 1) // self.n_cols
        
    def run(self) -> None:
        """Run the comparison visualization."""
        fig, axes = plt.subplots(self.n_rows, self.n_cols, figsize=self.figsize)
        axes = np.array(axes).flatten() if isinstance(axes, np.ndarray) else [axes]
        
        visualizers = []
        for (name, gen), ax in zip(self.sort_generators.items(), axes):
            # This would require a modified Visualizer that accepts an axis
            # For now, this is a placeholder for the concept
            pass
        
        plt.tight_layout()
        plt.show()