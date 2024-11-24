import streamlit as st
import time  # time for delay

# Sample Questions and Answers
questions = [
    {"question": "What is the capital of France?", 
     "options": ["Paris", "London", "Berlin", "Madrid"], 
     "answer": "Paris"},
    
    {"question": "Which planet is known as the Red Planet?", 
     "options": ["Earth", "Mars", "Jupiter", "Venus"], 
     "answer": "Mars"},
    
    {"question": "Who wrote 'Romeo and Juliet'?", 
     "options": ["William Shakespeare", "Mark Twain", "J.K. Rowling", "Charles Dickens"], 
     "answer": "William Shakespeare"},
    
    {"question": "What is the largest mammal?", 
     "options": ["Elephant", "Blue Whale", "Great White Shark", "Giraffe"], 
     "answer": "Blue Whale"},
    
    {"question": "Which element has the chemical symbol 'O'?", 
     "options": ["Oxygen", "Gold", "Osmium", "Oxide"], 
     "answer": "Oxygen"}
]

# Initialize the quiz session state if it's not already initialized
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'question_index' not in st.session_state:
    st.session_state.question_index = 0
if 'quiz_completed' not in st.session_state:
    st.session_state.quiz_completed = False

# Display title of the app
st.title("Simple Quiz App")

# Function to display the current question
def display_question():
    # Get the current question and options
    question_data = questions[st.session_state.question_index]
    st.write(f"**Question {st.session_state.question_index + 1}:** {question_data['question']}")
    
    # Display the options as radio buttons
    selected_option = st.radio("Choose your answer:", question_data["options"], key=f"question_{st.session_state.question_index}")

    return selected_option

if not st.session_state.quiz_completed:
    # Display the current question
    selected_option = display_question()

    # Button to check the answer
    if st.button("Submit Answer"):
        correct_answer = questions[st.session_state.question_index]["answer"]

        # Check if the selected option is correct
        if selected_option == correct_answer:
            st.session_state.score += 1
            st.markdown('<p style="color:green; font-size:18px;">Correct! 🎉</p>', unsafe_allow_html=True)
        else:
            st.markdown(f'<p style="color:red; font-size:18px;">Wrong! The correct answer was: {correct_answer}</p>', unsafe_allow_html=True)
        
        # Add a delay before moving to the next question
        time.sleep(2)  # 2-second delay

        # Move to the next question
        st.session_state.question_index += 1

        # Check if there are more questions
        if st.session_state.question_index < len(questions):
            st.rerun()  # This will trigger the app to re-render
        else:
            # If the quiz is finished, show the final score
            st.session_state.quiz_completed = True
            st.write(f"**Quiz Completed!** Your final score is: {st.session_state.score}/{len(questions)}")
else:
    st.write(f"**Quiz Completed!** Your final score is: {st.session_state.score}/{len(questions)}")
    if st.button("Retake Quiz"):
        # Reset the quiz state
        st.session_state.score = 0
        st.session_state.question_index = 0
        st.session_state.quiz_completed = False
        st.rerun()  # Restart the quiz
