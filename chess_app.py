import streamlit as st
import chess
import chess.svg
import base64
from io import BytesIO
import cairosvg
import pygame
import tempfile
import threading

# Function to render SVG to Streamlit
def render_svg(svg):
    """Renders the given SVG string."""
    b64 = base64.b64encode(svg.encode('utf-8')).decode("utf-8")
    html = f'<img src="data:image/svg+xml;base64,{b64}"/>'
    st.write(html, unsafe_allow_html=True)

# Function to save SVG as PNG
def save_svg_as_png(svg_code):
    """Convert SVG code to PNG."""
    with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as f:
        cairosvg.svg2png(bytestring=svg_code.encode('utf-8'), write_to=f.name)
        return f.name

# Function to run pygame event loop
def run_pygame(board, move_queue):
    pygame.init()
    screen = pygame.display.set_mode((400, 400))
    pygame.display.set_caption('Chess')
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left click
                    x, y = event.pos
                    file = x // 50
                    rank = 7 - (y // 50)
                    square = chess.square(file, rank)
                    move_queue.append(chess.square_name(square))
                    
        screen.fill((255, 255, 255))
        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

def main():
    st.title("Interactive Chess Game with Pygame")

    # Initialize chess board
    board = chess.Board()
    move_queue = []

    # Start pygame in a separate thread
    pygame_thread = threading.Thread(target=run_pygame, args=(board, move_queue))
    pygame_thread.start()

    # Game loop
    while not board.is_game_over():
        st.subheader("Current Board")

        # Convert the board to an SVG and then to PNG for display
        svg = chess.svg.board(board=board)
        board_image_path = save_svg_as_png(svg)
        st.image(board_image_path)

        if board.turn == chess.WHITE:
            st.write("White's turn")
        else:
            st.write("Black's turn")

        move = st.text_input("Enter your move (e.g., e2e4):")
        if st.button("Make move"):
            try:
                board.push_san(move)
            except ValueError:
                st.error("Invalid move! Please try again.")

        if move_queue:
            move = move_queue.pop(0)
            if move:
                st.write(f"Move from pygame: {move}")

        if board.is_checkmate():
            st.write("Checkmate!")
            break
        elif board.is_stalemate():
            st.write("Stalemate!")
            break
        elif board.is_insufficient_material():
            st.write("Draw due to insufficient material!")
            break

    pygame_thread.join()

if __name__ == "__main__":
    main()
