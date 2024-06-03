import streamlit as st
import chess
import chess.svg
from PIL import Image
from io import BytesIO
import base64

def render_svg(svg):
    """Renders the given SVG string."""
    b64 = base64.b64encode(svg.encode('utf-8')).decode("utf-8")
    html = f'<img src="data:image/svg+xml;base64,{b64}"/>'
    st.write(html, unsafe_allow_html=True)

def main():
    st.title("Chess Game")
    
    # Initialize chess board
    board = chess.Board()
    
    # Game loop
    while not board.is_game_over():
        st.subheader("Current Board")
        svg = chess.svg.board(board=board)
        render_svg(svg)

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

        if board.is_checkmate():
            st.write("Checkmate!")
            break
        elif board.is_stalemate():
            st.write("Stalemate!")
            break
        elif board.is_insufficient_material():
            st.write("Draw due to insufficient material!")
            break

if __name__ == "__main__":
    main()
