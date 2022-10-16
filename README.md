# book-recommendation
Build a book recommendation system using the the machine learning algorithms and deployment in cloud platfomr

1. save model --- artifacts/
2. save data -- data/
3. Create conda environment
```
conda create --prefix ./env python==3.7 -y #name of conda: ./env
conda activate ./env/
```
4. Create the setup file
```
touch setup.py
```
5. Create read me file
```
touch README.md
```
6. Create requirements txt file
```
touch requirements.txt
```
7. Create src folder
```
mkdir src
```
8. create init file inside src folder
```
touch src/__init__.py
```
9. install all requirement files
```
pip install -r requirements.txt
```
10. create app file
```
touch app.py
```
11. create streamlit web application
```
st.header("Book Recommender System using MAchine Learning")
```
12. run web application through the local system
```
streamlit run app.py
```
13. Select the book name by selectbox of streamlit
14. define button for recommendation
15. define gitignore
16. now define in Heroku
```
touch Procfile
```
17. create setup sh file
```
touch setup.sh
```
18. open the Heroku: 
