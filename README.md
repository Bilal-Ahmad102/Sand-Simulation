# Sand Simulation

## Description

This project is a sand simulation game implemented using Pygame and NumPy. The simulation features particles that behave like sand, falling and interacting with obstacles. The particles are rendered with different hues to create a visually appealing effect.

## Features

- **Sand Particle Simulation:** Particles fall, interact with each other, and are affected by obstacles.
- **Obstacle Creation:** Create obstacles in the simulation by dragging the mouse.
- **Dynamic Hue:** Sand particles have dynamically changing colors based on their movement.

## Requirements

- Python 3.x
- Pygame
- NumPy

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/Bilal-Ahmad102/Sand-Simulation
    cd Sand-Simulation
    ```

2. Install the required libraries:
    ```bash
    pip install pygame numpy
    ```

## Usage

Run the any of sand script to start the simulation, example:

```bash
python sand_1.py
```

### Controls

- **Mouse Drag:** Create obstacles by dragging the left mouse button.

## Code Structure

- **`sand_1.py`**: Contains the main `Space` class that handles the simulation.
- **`particles.py`**: Contains the `Particle` class used for rendering the sand particles.

## Detailed Explanation

### Space Class

- **`__init__`**: Initializes the simulation window, grids, and particles.
- **`make_obstacles`**: Placeholder for obstacle creation logic.
- **`on_mouse_drag`**: Handles mouse drag events to create obstacles.
- **`fall`**: Manages the falling behavior of sand particles.
- **`update_particles`**: Updates particle positions and renders them.
- **`update`**: Updates the simulation state.
- **`draw_obstacles`**: Draws obstacles on the window.
- **`run`**: Main loop for running the simulation.

### Particle Class

- **`__init__`**: Initializes particle attributes.
- **`show_sand`**: Renders the particle on the given surface.

## Future Improvements

- Add more particle types with different behaviors.
- Implement advanced obstacle interactions.
- Enhance the user interface with more controls and settings.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any improvements or bug fixes.


## Acknowledgments

- Pygame for the graphics library.
- NumPy for efficient array operations.
