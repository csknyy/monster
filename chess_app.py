import streamlit as st
import chess
import chess.svg
from io import BytesIO
import cairosvg
import pygame
import tempfile

def render_svg(svg):
    """Renders the given SVG string."""
    b64 = base64.b64encode(svg.encode('utf-8')).decode("utf-8")
    html = f'<img src="data:image/svg+xml;base64,{b64}"/>'
    st.write(html, unsafe_allow_html=True)

def save_svg_as_png(svg_code):
    """Convert SVG code to PNG."""
    with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as f:
        cairosvg.svg2png(bytestring=svg_code.encode('utf-8'), write_to=f.name)
        return f.name

def main():
    st.title("Interactive Chess Game with Pygame")

    # Initialize chess board
    board = chess.Board()

    # Initialize Pygame
    pygame.init()
    screen = pygame.display.set_mode((400, 400))
    pygame.display.set_caption('Chess')
    clock = pygame.time.Clock()

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

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        pygame.display.flip()
        clock.tick(30)

        if board.is_checkmate():
            st.write("Checkmate!")
            break
        elif board.is_stalemate():
            st.write("Stalemate!")
            break
        elif board.is_insufficient_material():
            st.write("Draw due to insufficient material!")
            break

    pygame.quit()

if __name__ == "__main__":
    main()
