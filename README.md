# Chinese Fuzzy Finder

This is a small project that I have created for my Python Software Development: CS 3270 at UVU.

I wanted to experiment with fuzzy finding as well as languages. Given that we had a focus on sqlite over the course of the semester, I decided to use sqlite, as well as Streamlit to create a simple fuzzy finding application.

I used an open source [Chinese Dictionary](https://www.mdbg.net/chinese/dictionary?page=cc-cedict) and implemented a simple fuzzy search on the pinyin (pronunciation) and the definition of each Chinese word.

A cool feature that I was able to implement is the ability to fuzzy search both at the same time. Try it out and see!

## Usage

To use the app there are two different options:

1. [Docker](https://www.docker.com/)

2. Python Virtual Environment

### Docker

1. First build the container:

```bash
docker build -t fuzzy-chinese ./src 
```

2. Then run the container:

```bash
docker run -p 8501:8501 fuzzy-chinese 
```

### Python Virtual Environment

1. Install necessary requirements: 

```bash
pip install -r requirements.txt --upgrade
```

2.  Make sure to change directory into the `./src` folder:

```bash
cd ./src
```

3. Then run the app:

```bash
streamlit run app.py
```

### Lastly

Then the site should be live at:

[`localhost:8501`](http://localhost:8501/)

---

* Tremendous thanks to [Dr. Brian Durney](https://www.uvu.edu/directory/employee/?id=RXYyMEVpNHFhaVBmR21rVG8yM2tNdz09) at [UVU](https://www.uvu.edu/). It has been an excellent and insightful semester.
