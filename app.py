import streamlit as st
import json
import time
import requests

api_endpoint = 'https://xxxx.lambda-url.us-west-2.on.aws/'

def get_response(text):
    payload = {
        'prompt': f'Pleae summarize the following text.\n {text}'
    }
    response = requests.post(api_endpoint, json=payload)
    print(f'Response status':: {response.status_code})
    response_text = response.text

    for word in response_text.split():
        yield word + " "
        time.sleep(0.1)


def main():
    st.set_page_config('Text Summarization Demo')
    st.header('AWS Bedrock integration With Serverless Lambda Function')
    text = st.text_area('Write text to summarize')
    if st.button('Summarize It'):
        with st.spinner('Processing...'):
            # call lambda function url
            st.write(get_response(text))

    
if __name__ == '__main__':
    main()