import streamlit as st
import streamlit.components.v1 as components

def landing_page():
    st.markdown(
        """
        <style>
        .title {
            color: #FFA500; /* Orange color */
            font-size: 48px;
            font-weight: bold;
            text-align: center;
        }
        .note {
            color: rgb(255,255,255);
            font-size: 20px;
            text-align: center;
        }
        .button-container {
            display: flex;
            justify-content: center;
            gap: 20px;
            margin-top: 30px;
        }
        .stButton > button {
            font-size: 20px;
            font-weight: bold;
            background-color: #FFA500; /* Orange color */
            color: white;
            padding: 15px 30px;
            border-radius: 10px;
            border: none;
            cursor: pointer;
            margin: 10px;
        }
        .stButton > button:hover {
            background-color: #e59400; /* Darker orange */
        }
        </style>
        <div class="title">Let’s Talk</div>
        <p class="note">
            Welcome to the Dyslexia Support App! We are here to help you with any questions or provide you with useful resources.
        </p>
        <p class="note">
            Choose one of the options below to get started:
        </p>
        <div class="button-container">
        </div>
        """,
        unsafe_allow_html=True
    )

    col1, col2 = st.columns([1, 1])
    
    with col1:
        if st.button("I Have a Doubt"):
            st.session_state.page = "Chatbot"
            st.experimental_rerun()

    with col2:
        if st.button("Get Support"):
            st.session_state.page = "Therapy"
            st.experimental_rerun()





# Function to create the chatbot page

def render_html_with_text(text_variable):
    
    # Read the HTML content from the index.html file
    with open("chatbot.html", "r", encoding="utf-8") as file:
        html_code = file.read()

    # Replace the placeholder text with the actual text variable
    html_code = html_code.replace("{text_variable}", text_variable)

    # Render the HTML code in Streamlit
    components.html(html_code, height=600)


def chatbot_page():
    import pandas as pd
    import streamlit as st
    from sklearn.feature_extraction.text import TfidfVectorizer
    import faiss
    import google.generativeai as genai
    import speech_recognition as sr
    import pyttsx3
    import time
    from streamlit_webrtc import webrtc_streamer, RTCConfiguration

    # Initialize the recognizer 
    r = sr.Recognizer() 

    genai.configure(api_key='AIzaSyBohDuGeJWtHgJrHmCA5EJXpdZ14jfQZPg')

    model = genai.GenerativeModel('gemini-1.5-flash')
    # Load the dataset
    

    def recognize_speech_from_microphone():
        # Use the microphone as the source for input
        with sr.Microphone() as source:
            # Wait for a second to let the recognizer adjust the energy threshold
            r.adjust_for_ambient_noise(source, duration=0.2)
            
            # Listens for the user's input
            audio = r.listen(source)
            
            # Using Google to recognize audio
            try:
                MyText = r.recognize_google(audio)
                MyText = MyText.lower()
                # st.write("Did you say: ", MyText)
                return MyText
            except sr.RequestError as e:
                st.write("Could not request results; {0}".format(e))
            except sr.UnknownValueError:
                st.write("Unknown error occurred")
            return ""

    # Ensure you have columns 'Query' and 'Response'
    def preprocess(text):
        # Add any preprocessing steps you need
        return text.lower()
    
    



    def generate_response(query):
        prompt = (
            f"{query}"
            f'''I'd like you to act as an educational assistant for a child with dyslexia. Please keep in mind that they might struggle with reading and writing, so it's important to present information in a simple and clear way'''
            f'''
        Keep the following things in mind:    
    Simple Language: Use short sentences and avoid complex vocabulary. Break down concepts into smaller, easier-to-understand parts.
    Visual Aids: Whenever possible, use pictures, diagrams, or other visual aids to support the explanation.
    Chunking: Present information in small chunks and allow time for the child to process it before moving on.
    Repetition: It's okay to repeat information if needed.
    Positive Reinforcement: Offer encouragement and praise the child's efforts.
    Dont make use of any image for illustration
    your response should me limited to 120 words
    '''
        )
        payload = {
            "prompt": prompt,
            "max_tokens": 150,  # adjust based on desired response length
        }
        response = model.generate_content(prompt)
        return response.text

    # Streamlit UI
    st.title("General simplifeid Chatbot for Dyslexic Individuals")

    user_query = ""
    text_input = st.text_input("Type your query here:")
    st.write("or use the microphone below:")

    if st.button("Start Microphone"):
        user_query = recognize_speech_from_microphone()
        st.write("Recognized Text: ", user_query)
        
        generated_response = generate_response(user_query)
        render_html_with_text(generated_response)


    if st.button("Submit"):
        if text_input:
            user_query = text_input
        if user_query:
            
            generated_response = generate_response(user_query)
            # st.write(generated_response)
            
            render_html_with_text(generated_response)
        else:
            st.write("Please provide a query through either text input or microphone.")
        
        

            
    
    

# Function to create the therapy page
def therapy_page():
    import pandas as pd
    import streamlit as st
    from sklearn.feature_extraction.text import TfidfVectorizer
    import faiss
    import google.generativeai as genai
    import speech_recognition as sr
    import pyttsx3
    import time
    from streamlit_webrtc import webrtc_streamer, RTCConfiguration

    # Initialize the recognizer 
    r = sr.Recognizer() 

    # Load the dataset
    df = pd.read_csv(r"C:\Users\Prashant Ronad\Documents\amBITion\final\files\dataset.csv", encoding='latin1')

    def recognize_speech_from_microphone():
        # Use the microphone as the source for input
        with sr.Microphone() as source:
            # Wait for a second to let the recognizer adjust the energy threshold
            r.adjust_for_ambient_noise(source, duration=0.2)
            
            # Listens for the user's input
            audio = r.listen(source)
            
            # Using Google to recognize audio
            try:
                MyText = r.recognize_google(audio)
                MyText = MyText.lower()
                # st.write("Did you say: ", MyText)
                return MyText
            except sr.RequestError as e:
                st.write("Could not request results; {0}".format(e))
            except sr.UnknownValueError:
                st.write("Unknown error occurred")
            return ""

    # Ensure you have columns 'Query' and 'Response'
    def preprocess(text):
        # Add any preprocessing steps you need
        return text.lower()

    df['Query'] = df['Query'].apply(preprocess)
    df['Response'] = df['Response'].apply(preprocess)

    # Vectorize the queries
    vectorizer = TfidfVectorizer()
    query_vectors = vectorizer.fit_transform(df['Query'])

    # Create a FAISS index
    dimension = query_vectors.shape[1]
    index = faiss.IndexFlatL2(dimension)

    # Convert query_vectors to a suitable format for FAISS
    query_vectors_faiss = query_vectors.toarray().astype('float32')

    # Add vectors to the FAISS index
    index.add(query_vectors_faiss)

    # Save the FAISS index to disk
    faiss.write_index(index, 'index.faiss')

    # Configure the generative AI model
    genai.configure(api_key='AIzaSyBohDuGeJWtHgJrHmCA5EJXpdZ14jfQZPg')
    model = genai.GenerativeModel('gemini-1.5-flash')

    def retrieve(query, vectorizer, index, responses):
        query_vec = vectorizer.transform([query]).toarray().astype('float32')
        D, I = index.search(query_vec, k=1)  # k is the number of closest vectors to search
        return responses[I[0][0]]

    def generate_response(query, context):
        prompt = (
            f"User: {query}\n"
            f"Therapist (focused on helping a dyslexic person): {context}\n"
            "Response (specific and tailored for dyslexic individuals):"
            f'''Focus on building a safe and supportive space.
            Acknowledge the child's feelings and validate their struggles.
            Emphasize that it's a different way of learning, not a disability.
            Showcase successful people with dyslexia.
            Motivate the child by demonstrating achievement is possible.
            Highlight the importance of support and tools.
            Briefly mention resources like audiobooks, specialized tutors, or assistive technologies.
            End on a positive and empowering note.
            Remind the child of their strengths and potential.
            Use positive and affirming language throughout.
            Maintain a conversational and approachable tone.
            Encourage the child to ask questions and express their feelings.\n
            Give the response in 120 to 150 words and stick to the query and remember the child in dyslexic'''
        )
        response = model.generate_content(prompt)
        return response.text

    # Streamlit UI
    st.title("Therapist Chatbot for Dyslexic Individuals")

    user_query = ""
    text_input = st.text_input("Type your query here:")
    st.write("or use the microphone below:")

    if st.button("Start Microphone"):
        user_query = recognize_speech_from_microphone()
        st.write("Recognized Text: ", user_query)
        retrieved_context = retrieve(user_query, vectorizer, index, df['Response'])
        generated_response = generate_response(user_query, retrieved_context)
        render_html_with_text(generated_response)
        


    if st.button("Submit"):
        if text_input:
            user_query = text_input
        if user_query:
            retrieved_context = retrieve(user_query, vectorizer, index, df['Response'])
            generated_response = generate_response(user_query, retrieved_context)
            render_html_with_text(generated_response)
        else:
            st.write("Please provide a query through either text input or microphone.")
        
        # render_html_with_text(generated_response)


# Main function to route pages
def main():
    # Initialize session state for page navigation
    if 'page' not in st.session_state:
        st.session_state.page = "landing"

    if st.session_state.page == "landing":
        landing_page()
    elif st.session_state.page == "Chatbot":
        chatbot_page()
    elif st.session_state.page == "Therapy":
        therapy_page()




# Run the main function
if __name__ == "__main__":
    main()
