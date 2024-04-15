# News Summarizer

News Summarizer is a Python application that extracts and summarizes news articles while providing sentiment analysis. It offers users a straightforward interface for inputting article URLs and receiving concise summaries along with sentiment analysis results. Built with Tkinter for the interface, NLTK for natural language processing, TextBlob for sentiment analysis, and Newspaper for article extraction, this project streamlines the process of digesting online news content.

## Features

- **URL Input:** Users can input the URL of the news article they want to summarize.
- **Article Extraction:** The application extracts the article's title, author, publication date, and main content.
- **Summarization:** Utilizing NLTK, the application generates a summary of the article's content.
- **Sentiment Analysis:** TextBlob is employed to analyze the sentiment of the article, categorizing it as positive, negative, or neutral based on polarity.

## How to Use

1. Install the required dependencies: Tkinter, NLTK, TextBlob, and Newspaper.
2. Run the Python script `news_summarizer.py`.
3. Enter the URL of the news article you want to summarize.
4. Click the "Summarize" button to initiate the summarization process.
5. The application will display the title, author, publication date, summary, and sentiment analysis of the article in the respective fields.

## Dependencies

- Tkinter
- NLTK
- TextBlob
- Newspaper

Ensure that NLTK's 'punkt' package is downloaded before running the application.

## Contributing

Contributions to this project are welcome! Feel free to submit bug reports, feature requests, or pull requests on GitHub to help improve the functionality and usability of the News Summarizer.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
