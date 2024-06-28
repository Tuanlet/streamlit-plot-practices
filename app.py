import streamlit as st

st.title('hello geeks')
st.header('Header')
st.subheader('subhead')
st.text('text = input')

st.markdown('hi')
st.markdown('#### hi')
st.markdown('###### hi')

st.success('data is submitted')
st.info('info is submitted')
st.warning('warning!')
st.error('Error')

exp = ZeroDivisionError('division not possible with 0')
st.exception(exp)

st.write("range(1,10)")
st.write(range(1,10))
st.write( 1*2*3)

st.code('x = 10\n'
        'for i in range(x)\n'
        '  \t print (i)')

st.checkbox('male')
st.checkbox('female')

if(st.checkbox('Adult')):
   st.write("you are an adult!")

#st.radio('Select : ', ('male', 'Female', 'Other'))

radioButton = st.radio('Select : ', ('male', 'Female', 'Other'))

if(radioButton == 'male'):
   st.write("You are male")
elif(radioButton == 'Female'):
   st.write("you are female")
elif(radioButton == 'Other'):
   st.write("you are other gender")


st.subheader('select box')
selectBox = st.selectbox("Data Science : ", ['Data analysis', ' Web scraping', 'machine learning', 
                                             ' deep learning', 'naturan language processing', 'computer vision', 'image processing'])

st.write("you've selected: ", selectBox)

st.subheader('multiselect box')
multiSelbox = st.multiselect("Data Science : ", ['Data analysis', ' Web scraping', 'machine learning', 
                                                        ' deep learning', 'naturan language processing', 'computer vision', 'image processing'])

st.write("You've selected: ", len(multiSelbox), 'courses')

st.subheader("Button")

if(st.button('click me')):
   st.write('thanks for clicking on me')
   
st.subheader("slider")
slRange = st.slider('select the range', 0,100, step = 1)
st.write('Range is : ', slRange)


st.subheader("text input")
username = st.text_input('Username:  ')
if (username):
   st.write('hi', username)

password = st.text_input('Password:  ', type = 'password')

st.subheader("Text Area")
textArea = st.text_area('Write something interesting about yourself in 500 words')
st.write(textArea)


st.subheader("Input number")
st.number_input('select your age', 18,100)


st.subheader("Input Date")
st.date_input('Date ')


st.subheader("Input time")
time_input('Time')