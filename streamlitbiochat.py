import streamlit as st
import requests

def main():
    # Set the page configuration (optional but adds a professional touch)
    st.set_page_config(
        page_title="BioChat",
        page_icon="🚀",
        layout="centered"
    )
    
    # App title and brief description
    st.title("BioChat")
    st.markdown(
        """
        Welcome to your BioChat interface!  
        Simply enter a query below, and we'll send it to the FastAPI endpoint.
        The response from the API will be displayed here, including any source 
        information returned by the server.
        """
    )
    
    # Text input for user query
    user_query = st.text_input("Enter your query:", "")
    
    # Button to submit query
    if st.button("Submit"):
        if user_query.strip():
            # Replace this with the actual URL of your FastAPI endpoint
            BASE_URL = "http://20.218.151.181:4951/api/v1/retrieve_data"
            
            # Show a spinner while we are contacting the API
            with st.spinner("Fetching response..."):
                try:
                    response = requests.get(
                        BASE_URL,
                        params={"query": user_query},
                        headers={"accept": "application/json"}
                    )
                    
                    # Check for successful request
                    if response.status_code == 200:
                        resp_json = response.json()
                        
                        # Display the result in a clean layout
                        st.success("Success! Response received.")
                        st.subheader("Response Data")
                        st.write(resp_json.get("data", "No data returned."))
                        
                        st.subheader("Source")
                        st.write(resp_json.get("source", "No source returned."))
                    else:
                        st.error(f"API call failed with status code {response.status_code}.")
                        
                except Exception as e:
                    st.error(f"Error calling the API: {e}")
        else:
            st.warning("Please enter a query before submitting.")

if __name__ == "__main__":
    main()
