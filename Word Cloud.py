import numpy as np
from PIL import Image
import wikipediaapi
from wordcloud import WordCloud, STOPWORDS

def generate_wordcloud():
    topic = input("Enter the name of the topic you want to create a word cloud for: ")
    
    user_agent = "WordCloudGenerator/1.0 (your_email@example.com)"
    
    wiki_wiki = wikipediaapi.Wikipedia('en', user_agent=user_agent)
    
    page = wiki_wiki.page(topic)
    
    if not page.exists():
        print("No page found for the topic.")
        return
    
    text = page.text

    print(f"Generating word cloud for: {page.title}")

    try:
        background_image = np.array(Image.open("abcd.jpg"))
    except FileNotFoundError:
        print("Background image 'abcd.jpg' not found.")
        return

    stop_words = set(STOPWORDS)

    wordcloud = WordCloud(
        background_color="white",
        max_words=500,
        mask=background_image,
        stopwords=stop_words
    ).generate(text)

    output_file = "wordcloud.png"
    wordcloud.to_file(output_file)

    print(f"Word cloud saved as {output_file}")


    generate_wordcloud()
