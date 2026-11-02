# Maze Runner 🧩

**AI Powered Maze Solving and Visualization**

Maze Runner is a Streamlit-based application that allows users to
generate mazes, solve them manually, or watch artificial intelligence
search algorithms explore and solve them. It also includes an automatic
AI agent mode that analyzes the maze and selects an algorithm.

## Project Overview

The application generates a maze based on the selected number of rows
and columns. Users can interact with the maze in two main modes:

1.  **Solve Manually** -- control the player using directional buttons.
2.  **AI Solve** -- let an AI algorithm or an automatic agent find a
    path from the start to the goal.

During AI solving, the application visualizes explored cells and then
displays the final solution path.

## Features

-   **Maze generation:** Create a new maze using configurable row and
    column values.
-   **Adjustable dimensions:** Select between 5 and 30 rows and columns
    using sidebar sliders.
-   **Maze visualization:** Display the generated maze using the
    `MazeDrawer` class.
-   **Manual gameplay:** Move the player up, down, left, and right using
    on-screen buttons.
-   **Player reset:** Reset the player to the starting position.
-   **Goal detection:** Display a congratulations message and balloons
    when the player reaches the goal.
-   **AI solving:** Solve the maze using a selected search algorithm.
-   **Animated exploration:** Show explored nodes progressively during
    the search.
-   **Automatic agent:** Allow the `AIAgent` to analyze the maze and
    select an algorithm.
-   **Performance metrics:** Display path length and number of explored
    nodes for algorithm-based solving.
-   **Maze analysis:** Display the analysis and decision rules returned
    by the automatic agent.

## AI Search Algorithms

The application provides the following algorithm choices:

  -----------------------------------------------------------------------
  Algorithm                           General approach
  ----------------------------------- -----------------------------------
  Breadth First Search (BFS)          Explores the search space level by
                                      level.

  Depth First Search (DFS)            Explores one branch deeply before
                                      backtracking.

  Uniform Cost Search (UCS)           Expands paths according to their
                                      accumulated cost.

  Greedy Best First Search            Uses a heuristic estimate to guide
                                      exploration toward the goal.

  A\* Search                          Combines the cost so far with a
                                      heuristic estimate.

  Bidirectional Search                Searches from the start and goal
                                      sides until the searches meet.
  -----------------------------------------------------------------------

The exact implementation details, movement costs, heuristic, and
optimality guarantees depend on the individual algorithm modules in this
project.

## Technologies Used

-   **Python** -- main programming language.
-   **Streamlit** -- web application interface and interactive controls.
-   **Time** -- adds short pauses between animation frames.
-   **Maze-solving modules** -- custom implementations of the search
    algorithms and AI agent.

## Project Structure

The imports in the supplied application code indicate that the project
uses the following modules. Keep the corresponding Python files in the
same folder unless your project uses a package structure.

``` text
maze-runner/
├── app.py
├── generator.py
├── draw_maze.py
├── player.py
├── controler.py
├── bfs.py
├── dfs.py
├── ucs.py
├── greedy.py
├── astart.py
├── bidirectional.py
├── ai.py
└── README.md
```

### File Description

  -----------------------------------------------------------------------
  File                                Purpose
  ----------------------------------- -----------------------------------
  `app.py`                            Main Streamlit application. Handles
                                      page setup, controls, maze display,
                                      and solving modes.

  `generator.py`                      Provides the `MazeGenerator` class
                                      used to generate mazes.

  `draw_maze.py`                      Provides the `MazeDrawer` class
                                      used to draw the maze and solution
                                      visualization.

  `player.py`                         Provides the `Player` class for
                                      manual maze movement.

  `controler.py`                      Provides the `GameController` class
                                      for handling player movement
                                      commands.

  `bfs.py`                            Contains the Breadth First Search
                                      implementation.

  `dfs.py`                            Contains the Depth First Search
                                      implementation.

  `ucs.py`                            Contains the Uniform Cost Search
                                      implementation.

  `greedy.py`                         Contains the Greedy Best First
                                      Search implementation.

  `astart.py`                         Contains the A\* Search
                                      implementation.

  `bidirectional.py`                  Contains the Bidirectional Search
                                      implementation.

  `ai.py`                             Provides the `AIAgent` used in
                                      Agent Automatic mode.
  -----------------------------------------------------------------------

**Note:** The filenames above follow the import statements in the
supplied code. The main Streamlit file is named `app.py` here as an
example; use its actual filename in your project.

## Installation and Setup

### 1. Install Python

Install a compatible Python version if Python is not already available.

### 2. Install Streamlit

Open a terminal in the project folder and run:

``` bash
pip install streamlit
```

Install any additional dependencies required by your maze generation,
drawing, or search modules. For example, if the drawing module uses
OpenCV, install its required package as well.

### 3. Arrange the Project Files

Make sure the imported Python modules are available in the project
folder and that their filenames match the import statements.

### 4. Run the Application

If your main file is named `app.py`, run:

``` bash
streamlit run app.py
```

If it has a different filename, replace `app.py` with that filename.

Streamlit will provide a local URL that you can open in your browser.

## How to Use

1.  Start the application.
2.  Use the sidebar sliders to choose the maze's number of rows and
    columns.
3.  Select **Generate New Maze** to create a maze with the chosen
    dimensions.
4.  Choose one of the two modes:
    -   **Solve Manually:** use the directional controls to move the
        player. Use the reset button to return to the starting position.
    -   **AI Solve:** choose either **Agent Automatic** or **Solve Using
        Algorithms**.
5.  In Agent Automatic mode, select **Start Agent**. The agent returns
    maze analysis, decision rules, performance metrics, and a solution.
6.  In Solve Using Algorithms mode, select an algorithm and click **Run
    Algorithm**.
7.  Watch the explored cells animate, followed by the final solution
    path.

## How the Application Works

1.  Streamlit displays the page title, sidebar settings, and maze
    controls.
2.  The application checks whether a maze already exists in
    `st.session_state`. If not, it generates an initial maze and creates
    a player.
3.  When **Generate New Maze** is clicked, a new maze and player are
    created, and the stored solution path is cleared.
4.  `MazeDrawer` draws the current maze and displays it in the
    application.
5.  The selected mode determines whether the player is controlled
    manually or a search algorithm is executed.
6.  In manual mode, `GameController` passes movement commands to the
    player.
7.  In AI mode, the selected solver returns a path and explored nodes.
    The application redraws the maze repeatedly to animate exploration.
8.  The final path is drawn and a success message is displayed.

## Performance Information

For the individual algorithm mode, the application displays:

-   **Path Length:** the number of positions or nodes in the returned
    path, as measured by `len(path)` in the supplied code.
-   **Nodes Explored:** the number of explored entries returned by the
    solver, as measured by `len(explored)`.

In Agent Automatic mode, the application displays the metrics and
analysis returned by `AIAgent.solve()`. The exact metric definitions
depend on the implementation of the agent and algorithm modules.

## Important Notes

-   The application uses `st.session_state` to retain the maze and
    player across Streamlit reruns.
-   The supplied code imports custom modules. They must be present and
    importable for the application to run.
-   The import filename is `controler.py` (one `l` in "controler") in
    the supplied code. Keep that spelling consistent or update the
    import and filename together.
-   The code uses `MazeDrawer.draw()` with `channels="BGR"` when
    displaying images. The drawing implementation should return an image
    compatible with this setting.
-   The `inspect` import and commented `inspect.getfile()` line are not
    required for normal application execution.
-   The code uses short `time.sleep()` pauses to animate the search.
    Animation duration depends on the number of explored nodes.
-   The exact maze-generation method, AI decision rules, and algorithm
    internals are defined in the corresponding source modules and are
    not visible in the supplied Streamlit file.

## Future Improvements

-   Add a pause and resume option for AI animation.
-   Allow users to adjust animation speed.
-   Display execution time and memory usage for each algorithm.
-   Compare algorithms using the same maze.
-   Add a downloadable maze or solution report.
-   Improve mobile layout and accessibility.
-   Add clear feedback when no solution path is found.

## Author

Add your name or team name here.

------------------------------------------------------------------------

Built with Python and Streamlit. 🧩
