import streamlit as st
import requests

st.set_page_config(page_title="Country Info Cards", page_icon="🌍")

st.title("🌍 Country Information Cards")
st.write("Search for any country and get basic information!")

# Input
country_name = st.text_input("Enter Country Name", "Pakistan")

def get_country_data(name):
    url = f"https://restcountries.com/v3.1/name/{name}"
    res = requests.get(url)

    if res.status_code == 200:
        data = res.json()[0]
        return {
            "flag": data["flags"]["png"],
            "name": data["name"]["common"],
            "capital": data.get("capital", ["N/A"])[0],
            "region": data.get("region", "N/A"),
            "subregion": data.get("subregion", "N/A"),
            "population": f"{data.get('population', 0):,}",
            "area": f"{data.get('area', 0):,} km²"
        }
    else:
        return None

if country_name:
    data = get_country_data(country_name)
    
    if data:
        st.image(data["flag"], width=150)
        st.subheader(f"{data['name']}")
        st.markdown(f"""
        - 🏛️ **Capital:** {data['capital']}  
        - 🌍 **Region:** {data['region']} / {data['subregion']}  
        - 👥 **Population:** {data['population']}  
        - 📐 **Area:** {data['area']}
        """)
    else:
        st.error("Country not found or API error.")
