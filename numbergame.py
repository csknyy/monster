import random
import streamlit as st

# Set up the Streamlit app
st.title("Number Guessing Game 🎯")

# Sidebar for setting game parameters
st.sidebar.header("Game Settings")
min_value = st.sidebar.number_input("Minimum Value", value=1, step=1)
max_value = st.sidebar.number_input("Maximum Value", value=100, step=1)
lives = st.sidebar.number_input("Number of Lives", value=5, min_value=1, step=1)

# Start the game
if min_value >= max_value:
    st.error("Minimum value must be less than the maximum value!")
else:
    if "secret_number" not in st.session_state:
        st.session_state.secret_number = random.randint(min_value, max_value)
        st.session_state.attempts = 0
        st.session_state.lives = lives
        st.session_state.game_over = False

    st.write(f"Guess the number between {min_value} and {max_value}!")
    st.write(f"Lives remaining: {st.session_state.lives}")

    if st.session_state.game_over:
        if st.session_state.lives == 0:
            st.error(f"Game Over! You've run out of lives. The number was {st.session_state.secret_number}. 😢")
        else:
            st.success(f"Congratulations! You guessed the number: {st.session_state.secret_number} 🎉")

        if st.button("Play Again"):
            st.session_state.secret_number = random.randint(min_value, max_value)
            st.session_state.attempts = 0
            st.session_state.lives = lives
            st.session_state.game_over = False
    else:
        guess = st.number_input("Enter your guess:", min_value=min_value, max_value=max_value, step=1, key="guess_input")
        if st.button("Submit Guess"):
            st.session_state.attempts += 1
            if guess < st.session_state.secret_number:
                st.session_state.lives -= 1
                st.warning("Too low! Try again.")
            elif guess > st.session_state.secret_number:
                st.session_state.lives -= 1
                st.warning("Too high! Try again.")
            else:
                st.session_state.game_over = True
                st.success(f"You got it in {st.session_state.attempts} attempts!")

            if st.session_state.lives == 0:
                st.session_state.game_over = True
