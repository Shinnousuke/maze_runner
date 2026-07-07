import streamlit as st
#from maze.generator import MazeGenerator
#from visualization.draw_maze import MazeDrawer
#from game.player import Player
from generator import MazeGenerator
from draw_maze import MazeDrawer
from player import Player
from controler import GameController
from dfs import DFS
from ucs import UCS
import time
from ai import AIAgent
from astart import AStar
from greedy import Greedy
from bidirectional import BidirectionalSearch
import inspect

#st.write(inspect.getfile(MazeDrawer))

from bfs import BFS
#from keyboard import Keyboard
#from keyboard_hander import KeyboardHandler
#from maze_component import maze_component

# ==========================================
# Page Configuration
# ==========================================

st.set_page_config(
    page_title="Maze Runner",
    page_icon="🧩",
    layout="wide"
)

# ==========================================
# Title
# ==========================================

st.title("🧩 Maze Runner")
st.markdown("### AI Powered Maze Solving and Visualization")

st.divider()

# ==========================================
# Sidebar
# ==========================================

st.sidebar.title("Maze Settings")

maze_rows = st.sidebar.slider(
    "Rows",
    min_value=5,
    max_value=30,
    value=15
)

maze_cols = st.sidebar.slider(
    "Columns",
    min_value=5,
    max_value=30,
    value=15
)
generate = st.sidebar.button("Generate New Maze")

# Create a maze the first time the app runs
if "maze" not in st.session_state:

    generator = MazeGenerator(maze_rows, maze_cols)
    maze = generator.generate()

    st.session_state["maze"] = maze
    st.session_state["player"] = Player(maze)
# ==========================================
# Generate Maze
# ==========================================

# ==========================================
# Generate Maze
# ==========================================

if generate:

    generator = MazeGenerator(
        maze_rows,
        maze_cols
    )

    maze = generator.generate()

    st.session_state["maze"] = maze
    st.session_state["player"] = Player(maze)
    st.session_state["solution_path"] = None

    st.success("Maze Generated Successfully!")
# ==========================================
# Display Maze Placeholder
# ==========================================

st.subheader("Maze")

if "maze" in st.session_state:
    cell_size = max(
    15,
    min(35, 700 // max(maze_rows, maze_cols))
)
    drawer = MazeDrawer(
    st.session_state["maze"],
    cell_size=cell_size,
    player=st.session_state["player"],
    path=st.session_state.get("solution_path")
)

    
    image = drawer.draw()

    st.image(
        image,
        channels="BGR",
        use_container_width=True
    )

else:

    st.info("Click 'Generate New Maze' to create a maze.")

st.divider()

# ==========================================
# Choose Mode
# ==========================================

st.subheader("Choose Mode")

mode = st.radio(
    "",
    (
        "🎮 Solve Manually",
        "🤖 AI Solve"
    ),
    horizontal=True
)

# ==========================================
# Manual Mode
# ==========================================

# ==========================================
# Manual Mode
# ==========================================

if mode == "🎮 Solve Manually":

    st.success("Manual Mode Selected")

    controller = GameController(
        st.session_state["player"]
    )

    st.sidebar.markdown("---")
    st.sidebar.subheader("🎮 Controls")

    c1, c2, c3 = st.sidebar.columns(3)

    with c2:
        if st.button("⬆️", key="up"):
            controller.move("UP")
            st.rerun()

    c1, c2, c3 = st.sidebar.columns(3)

    with c1:
        if st.button("⬅️", key="left"):
            controller.move("LEFT")
            st.rerun()

    with c2:
        if st.button("🔄", key="reset"):
            st.session_state["player"].reset()
            st.rerun()

    with c3:
        if st.button("➡️", key="right"):
            controller.move("RIGHT")
            st.rerun()

    c1, c2, c3 = st.sidebar.columns(3)

    with c2:
        if st.button("⬇️", key="down"):
            controller.move("DOWN")
            st.rerun()

    if st.session_state["player"].reached_goal():
        st.balloons()
        st.success("🎉 Congratulations!")
# ==========================================
# AI Mode
# ==========================================

else:

    st.success("AI Mode Selected")

    ai_mode = st.radio(
        "Choose AI Mode",
        (
            "Agent Automatic",
            "Solve Using Algorithms"
        )
    )

    # --------------------------------------

    if ai_mode == "Agent Automatic":

     st.write("The AI Agent will automatically choose the best algorithm.")

     if st.button("Start Agent"):

        agent = AIAgent(st.session_state["maze"])

        path, explored, metrics, analysis = agent.solve()

        placeholder = st.empty()

        st.subheader("Maze Analysis")

        for key, value in analysis.items():

             if key != "Rules":
                st.write(f"**{key}:** {value}")

        st.subheader("Decision Rules")

        for rule, result in analysis["Rules"].items():

            if result:
                st.success(f"✓ {rule}")
            else:
                st.error(f"✗ {rule}")

        st.subheader("Performance Metrics")

        for key, value in metrics.items():
            st.write(f"**{key}:** {value}")

        # Animate explored nodes
        for i in range(len(explored)):

            drawer = MazeDrawer(
                st.session_state["maze"],
                cell_size=cell_size,
                explored=explored[:i+1]
            )

            placeholder.image(
                drawer.draw(),
                channels="BGR",
                use_container_width=True
            )

            time.sleep(0.03)

        # Draw final path
        drawer = MazeDrawer(
            st.session_state["maze"],
            cell_size=cell_size,
            path=path
        )

        placeholder.image(
            drawer.draw(),
            channels="BGR",
            use_container_width=True
        )

        st.success("Maze Solved!")

        st.subheader("AI Decision")

        st.write(f"**Selected Algorithm:** {analysis['Selected Algorithm']}")
        st.write(f"**Difficulty:** {analysis['Difficulty']}")
        st.write(f"**Maze Density:** {analysis['Maze Density']}")
        st.write(f"**Dead Ends:** {analysis['Dead Ends']}")
        st.write(f"**Branching Factor:** {analysis['Branching Factor']}")
        st.write(f"**Goal Distance:** {analysis['Goal Distance']}")

        st.subheader("Performance Metrics")

        for key, value in metrics.items():
            st.write(f"**{key}:** {value}")

    # --------------------------------------

    else:

        st.subheader("Select Algorithm")

        algorithm = st.selectbox(
            "",
            (
                "Breadth First Search (BFS)",
                "Depth First Search (DFS)",
                "Uniform Cost Search (UCS)",
                "Greedy Best First Search",
                "A* Search",
                "Bidirectional Search"
            )
        )

        if st.button("Run Algorithm"):

    # -----------------------------
    # Select Algorithm
    # -----------------------------

         if algorithm == "Breadth First Search (BFS)":
            solver = BFS(st.session_state["maze"])

        elif algorithm == "Depth First Search (DFS)":
            solver = DFS(st.session_state["maze"])

        elif algorithm == "Uniform Cost Search (UCS)":
            solver = UCS(st.session_state["maze"])

        elif algorithm == "Greedy Best First Search":

            solver = Greedy(st.session_state["maze"])

        elif algorithm == "A* Search":

            solver = AStar(st.session_state["maze"])
        
        elif algorithm == "Bidirectional Search":

            solver = BidirectionalSearch(
        st.session_state["maze"]
    )

        else:
            st.warning("Algorithm not implemented yet.")
            st.stop()

    # -----------------------------
    # Solve Maze
    # -----------------------------

        path, explored = solver.solve()

    # -----------------------------
    # Animation Placeholder
    # -----------------------------

        placeholder = st.empty()

    # -----------------------------
    # Animate Search
    # -----------------------------

        for i in range(len(explored)):
            

            drawer = MazeDrawer(
            st.session_state["maze"],
            cell_size=cell_size,
            explored=explored[:i+1]
            )

            placeholder.image(
            drawer.draw(),
            channels="BGR",
            use_container_width=True
            )

            time.sleep(0.03)

    # -----------------------------
    # Draw Final Path
    # -----------------------------

        drawer = MazeDrawer(
        st.session_state["maze"],
        cell_size=cell_size,
        path=path
        )

        placeholder.image(
        drawer.draw(),
        channels="BGR",
        use_container_width=True
        )

        st.success("Maze Solved!")

        c1, c2 = st.columns(2)

        c1.metric("Path Length", len(path))
        c2.metric("Nodes Explored", len(explored))