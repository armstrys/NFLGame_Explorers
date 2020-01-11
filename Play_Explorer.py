## Packages
import streamlit as st
import nflgame as nflgame

##Sidebar
st.sidebar.header('Season and Week Selection')

y = st.sidebar.slider(label='Season',min_value=2009,max_value=2019,value=2019)
w = st.sidebar.slider(label='Week',min_value=1, max_value=17,value=1)

## Main Page
st.header('NFLGames API Play Explorer')
st.markdown('''
            This widget is based on  the [NFLGame](https://github.com/derek-adair/nflgame) Python package
            maintained by [Derek Adair](https://github.com/derek-adair). Be sure to check the docs for the API
            [here](http://nflgame.derekadair.com/) to get a better feel fro the capabilities of the package beyond
            the data model.

            
            I started this as a quick project to learn some basics of the [Streamlit](https://www.streamlit.io/)
            Python package and to get a better idea of what sorts of data is buried in the rich NFLGame
            API. This widget calls the 'nflgame.games' function using the season and year selected in sidebar
            uses a series of select boxes to dig down to the most detailed parts of the data structure.

            Start by selecting a season and week in the side panel of this page!
            ''')

@st.cache(allow_output_mutation=True)
def get_games(y,w):
    return nflgame.games(y, week=w, kind = 'REG')

games = get_games(y, w)

game_list = list(games)
game_select = st.multiselect(label='After choosing a season/week, select a game:', options = game_list)

if game_select:
    drive_list = []
    for game in game_select:
        st.text('''
        The 'game' object is a nested object that holds some high level statistics, but
        also generators that produce more detailed objects at the 'drive' and 'play'
        level. Either click the checkbox to dive into some of the 'game' object structure
        or select a drive to continue on.
        ''')
        if st.checkbox('Show game object dictionary'):
            st.write(game.__dict__) 
        else:
            pass
        drive_list += list(game.drives)
    
    drive_select = st.multiselect(label='Select a drive from above games:', options = drive_list)

    if drive_select:
        for drive in drive_select:
            st.text('''
            The 'drive' object is contained within the 'game' object and has a similar structure.
            Drive summary statistics can be found here. Click the checkbox to view the 'object' or
            select a 'play' to get more detailed information.
            ''')
            if st.checkbox('Show drive object dictionary'):
                st.write(drive.__dict__) # still lots of data here... lets keep diving down.
            else:
                pass
            
            play_list = {}
            for play in drive.plays:
                play_list[play.__dict__['desc']] = play.__dict__
        play_select = st.selectbox(label='Select a play from the drive:', options = list(play_list))

        if play_select:
            play_dict = play_list[play_select]
            st.text('''
            The 'play' object is the most detailed object that we will look at. It holds timing of specific
            plays and breaks out individual events assigned to players, such as tackles, targets, or yards
            after catch. Some of these detailed statistics are not found at the game level and can only be
            found by retrieving specific events.
            ''')
            if st.checkbox('Show play object dictionary'):    
                st.write(play_dict)
            else:
                pass
        else:
            pass
    else:
        pass
else:
    pass