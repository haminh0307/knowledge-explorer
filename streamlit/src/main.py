"""Streamlit main"""

import urllib.parse
import requests
from config import app_settings, settings
import streamlit as st

# Set page config
st.set_page_config(
    page_title='Knowledge explorer',
    page_icon=app_settings.PAGE_EMOJI,
    layout='wide',
)

if 'keyword' not in st.session_state:
    st.session_state['keyword'] = None
if 'keywords' not in st.session_state:
    st.session_state['keywords'] = []
if 'keyword_definition' not in st.session_state:
    st.session_state['keyword_definition'] = None
if 'quiz' not in st.session_state:
    st.session_state['quiz'] = None
if 'balloon' not in st.session_state:
    st.session_state['balloon'] = False


def explore(keyword: str):
    """Explore a keyword"""

    if keyword is not None:
        st.session_state.keyword = keyword
    if not st.session_state.keyword:
        return

    try:
        response = requests.post(
            urllib.parse.urljoin(f'{settings.API_URL}', 'definitions')
            + f'?keyword={st.session_state.keyword}',
        )
    except Exception:
        response = None
        st.error('Server is busy. Please try again later', icon=':rotating_light:')

    if response:
        if response.status_code != 200 or response.json()['message'] != 'success':
            st.error(response.json()['message'], icon=':rotating_light:')
        else:
            st.session_state.keyword_definition = response.json()['result']

    try:
        response = requests.post(
            urllib.parse.urljoin(f'{settings.API_URL}', 'quizzes')
            + f'?keyword={st.session_state.keyword}',
        )
    except Exception:
        response = None
        st.error('Server is busy. Please try again later', icon=':rotating_light:')

    if response:
        if response.status_code != 200 or response.json()['message'] != 'success':
            st.error(response.json()['message'], icon=':rotating_light:')
        else:
            st.session_state.quiz = response.json()['result']


with st.sidebar:
    st.title('Knowledge explorer')
    st.selectbox('Keyword', st.session_state.keywords,
                 key='keyword', on_change=explore, args=[None])

    st.write('### Definition')
    st.text_area(label='Definition', value='', key='keyword_definition')

    def quiz_update():
        """Balloon available after changing quiz answer"""

        st.session_state.balloon = True

    st.write('### Random quiz')
    if st.session_state.quiz:
        st.write(st.session_state.quiz['question'])
        opt = st.radio(label='Options', options=st.session_state.quiz['options'],
                       index=None, on_change=quiz_update)

        if opt == st.session_state.quiz['answer']:
            st.write(':ok_hand: Correct!')
            if st.session_state.balloon:
                st.session_state.balloon = False
                st.balloons()
        elif opt is not None:
            st.write(':pensive: Incorrect!')

c = st.container()

c.title(':eyes: Knowledge explorer')

with c:
    st.text_area('Text', key='text', height=256)

    if st.button('Extract', type='primary') and 'text' in st.session_state:
        try:
            response = requests.post(
                urllib.parse.urljoin(f'{settings.API_URL}', 'keywords')
                + f'?content={st.session_state.text}',
            )
        except Exception:
            response = None
            st.error('Server is busy. Please try again later', icon=':rotating_light:')

        if response:
            if response.status_code != 200 or response.json()['message'] != 'success':
                st.error(response.json()['message'], icon=':rotating_light:')
            else:
                st.session_state.keywords = response.json()['result']

    for keyword in st.session_state.keywords:
        st.button(keyword, on_click=explore, args=[keyword])
