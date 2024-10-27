import streamlit as st

#function to feedback page

def feedback(session):
    st.write("Why is this {session} your favourite?")
    reason=st.text_input("because...")
    pass 
    st.write("Why is this {session} not your favourite?")
    reason=st.text_input("because...",key="reason_2")
    st.write("Finally click the submit button to record your response")
    if st.button("submit"):
        st.session_state.feedback={"session":session,"reason":reason}  
        st.rerun()       
        
#Main page
st.header("Interactive Feedback Page")   
st.write("welcome to our Interactive Feedback Page!!!.This is a fun and educational way were we were able to find our strength and weekness which helps us to improve our communication skills .let's collaborate and see what kinds of feedbacks we are getting!")  
if "feedback"  not in st. session_state:
    st.write("feedback for the session:")
    st.write("Click the option A and choose the question and enter the reason for choosing it")
    if st.button("option A"):
        feedback("option A")
else:
    st.write("your feedback for {st.session_state.feedback['session']}because{st.session_state.feedback['reason']}")
                
     
