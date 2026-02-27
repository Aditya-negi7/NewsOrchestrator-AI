from crewai import Task

def create_tasks(news_researcher, news_writer):

    # Research Task
    research = Task(
        description=(
            "An AI News Research Specialist responsible for identifying and collecting "
            "the latest trends, developments, and updates on {topic} from reliable "
            "and recent sources. The agent focuses only on factual, up-to-date "
            "information and includes source names and publication dates. "
            "It avoids speculation and does not generate unverified content."
        ),
        expected_output=(
            "A structured list of recent articles including: "
            "Headline, Source name, Publication date, "
            "Key insights (2–4 bullet points per article)."
        ),
        agent=news_researcher,
    )

    # Writing Task
    write = Task(
        description=(
            "Compose an insightful article on {topic}. "
            "Clear, professional, and well-structured news article. "
            "Maintain a neutral journalistic tone and reference "
            "sources and publication dates within the article."
        ),
        expected_output=(
            "A polished news article on {topic} including: "
            "Strong headline, Dateline, Introduction summarizing key trend, "
            "Body paragraphs referencing sources with dates, "
            "Concise concluding summary."
        ),
        agent=news_writer,
        output_file='new-blog-post.md'
    )

    return [research, write]
