import streamlit as st

from api.fast import root

import requests

st.write(root())

st.write('This is obviously very simple, in reality one would rather use this page to display API results more nicely! :)')

st.write("trivial change")

#call live backend, with requests

backend_url = "https://ci-cd-example-2241-1085609219419.europe-west1.run.app"

st.write("calling live backend")
result = requests.get(backend_url)

output = result.json()

st.write(output)

