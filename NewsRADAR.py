import streamlit as st
import requests
import time
import base64
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu
from bs4 import BeautifulSoup

st.set_page_config(layout="wide")
def load_lottie_url(url):
    r = requests.get(url)
    if r.status_code!=200:
        return None
    return r.json()
lottie_url1 = "https://lottie.host/d0247001-a863-44c8-b945-ef158fd0c1a6/LnaSdYvnJe.json"
#lottie_url2 = ""
lottie_json1 = load_lottie_url(lottie_url1)
#lottie_json2 = load_lottie_url(lottie_url2)

# Background image function
def get_base64(image_file):
    with open(image_file, "rb") as file:
        return base64.b64encode(file.read()).decode()

def set_background(image_path):
    base64_str = get_base64(image_path)
    css = f"""
    <style>
    .stApp {{
    background-image: url("data:image/png;base64,{base64_str}");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    }}
    """
    st.markdown(css, unsafe_allow_html=True)


set_background("bkgfake.JPG")

st.title("News RADAR")
st.header("Scanning the News :satellite_antenna:, Spotting the Fake🤖⚠️")
with st.sidebar:
    selected = option_menu(
        menu_title="Menu",
        options=["Analyze News","Current News"],
        icons=["binoculars","globe"]
    )
if selected=="Analyze News":
    st.subheader("Analyze News")
    with st.form("Enter Link"):
        url = st.text_input("Enter the URL")
        btn = st.form_submit_button("Analyze News")

    if btn:
        if not url:
            st.error("Please enter a URL!")
        elif url:
            try:
                response = requests.get(url)
                if response.status_code == 200:
                    st.success("Link Fetched Successfully ✅")
                    placeholder = st.empty()
                    with placeholder:
                        st.image("scanner.gif")
                    time.sleep(3)

                    placeholder.empty()

                    with placeholder:
                        st.image("search.gif")
                    time.sleep(3)

                    placeholder.empty()
                    st.write("Results will appear here")
                
                else:
                    st.error(f"Failed to fetch URL. Status Code: {response.status_code}")
            except requests.exceptions.RequestException as e:
                st.error(f"Error fetching URL: {e}")


if selected == "Current News":
    option = st.selectbox("Select the category",["WORLD","NATIONAL","BUSINESS","TECHNOLOGY","ENTERTAINMENT","SPORTS","SCIENCE","HEALTH"])
    st.subheader("Current News")
    st.write(option)
    if option =="WORLD":
        url = "https://real-time-news-data.p.rapidapi.com/topic-headlines"
        headers = {
	"x-rapidapi-key": "df945c98f0mshbc4598bcebed63dp161025jsn17a90b18476e",
	"x-rapidapi-host": "real-time-news-data.p.rapidapi.com"
        }

        querystring = {"topic":"WORLD","limit":"500","country":"US","lang":"en"}
    elif option == "NATIONAL":
        url = "https://real-time-news-data.p.rapidapi.com/topic-headlines"
        querystring = {"topic":"NATIONAL","limit":"500","country":"US","lang":"en"}
        headers = {
	"x-rapidapi-key": "df945c98f0mshbc4598bcebed63dp161025jsn17a90b18476e",
	"x-rapidapi-host": "real-time-news-data.p.rapidapi.com"
        }
    elif option == "BUSINESS":
        url = "https://real-time-news-data.p.rapidapi.com/topic-headlines"

        querystring = {"topic":"BUSINESS","limit":"500","country":"US","lang":"en"}
    elif option == "TECHNOLOGY":
        url = "https://real-time-news-data.p.rapidapi.com/topic-headlines"
        querystring = {"topic":"TECHNOLOGY","limit":"500","country":"US","lang":"en"}
        headers = {
	"x-rapidapi-key": "df945c98f0mshbc4598bcebed63dp161025jsn17a90b18476e",
	"x-rapidapi-host": "real-time-news-data.p.rapidapi.com"
        }
    elif option == "ENTERTAINMENT":
        url = "https://real-time-news-data.p.rapidapi.com/topic-headlines"
        querystring = {"topic":"ENTERTAINMENT","limit":"500","country":"US","lang":"en"}
        headers = {
	"x-rapidapi-key": "df945c98f0mshbc4598bcebed63dp161025jsn17a90b18476e",
	"x-rapidapi-host": "real-time-news-data.p.rapidapi.com"
            }
    elif option == "SPORTS":
        url = "https://real-time-news-data.p.rapidapi.com/topic-headlines"
        querystring = {"topic":"SPORTS","limit":"500","country":"US","lang":"en"} 
        headers = {
	"x-rapidapi-key": "df945c98f0mshbc4598bcebed63dp161025jsn17a90b18476e",
	"x-rapidapi-host": "real-time-news-data.p.rapidapi.com"
            }
   
    elif option =="SCIENCE":
        url = "https://real-time-news-data.p.rapidapi.com/topic-headlines"
        querystring = {"topic":"SCIENCE","limit":"500","country":"US","lang":"en"}
        headers = {
	"x-rapidapi-key": "df945c98f0mshbc4598bcebed63dp161025jsn17a90b18476e",
	"x-rapidapi-host": "real-time-news-data.p.rapidapi.com"
            }
    elif option == "HEALTH":
        url = "https://real-time-news-data.p.rapidapi.com/topic-headlines"
        querystring = {"topic":"HEALTH","limit":"500","country":"US","lang":"en"}
        headers = {
	"x-rapidapi-key": "df945c98f0mshbc4598bcebed63dp161025jsn17a90b18476e",
	"x-rapidapi-host": "real-time-news-data.p.rapidapi.com"
            }
    
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
            data = response.json()
            articles = data.get("data", [])
    
            if articles:
                for index, article in enumerate(articles, start=1):
                    title = article.get("title", "No Title Available")
                    link = article.get("link")
                    
                    st.write(f"{index}. {title} {link}")
            else:
                st.write("No articles found.")
    else:
            st.error(f"Failed to fetch news. Status Code: {response.status_code}")



    
    