from langchain_community.document_loaders import DirectoryLoader
from dotenv import load_dotenv
from ragas.llms import LangchainLLMWrapper
from ragas.embeddings import LangchainEmbeddingsWrapper
from langchain_openai import ChatOpenAI
from langchain_openai import OpenAIEmbeddings

from ragas.testset import TestsetGenerator


# Intro
# Just following https://docs.ragas.io/en/stable/getstarted/rag_testset_generation/#load-sample-documents


# Load Documents

path = "/Users/veselda7/git-projects/Sample_Docs_Markdown"
loader = DirectoryLoader(path, glob="**/*.md")
docs = loader.load()


# Setup OpenAI LLM


load_dotenv()

generator_llm = LangchainLLMWrapper(ChatOpenAI(model="gpt-4o"))
generator_embeddings = LangchainEmbeddingsWrapper(OpenAIEmbeddings())


# Generate Dataset


generator = TestsetGenerator(llm=generator_llm, embedding_model=generator_embeddings)
dataset = generator.generate_with_langchain_docs(docs, testset_size=10)

df = dataset.to_pandas()
df.to_csv("output/generated_data.tsv", sep="\t")