import httpx
from prefect import flow, task, get_run_logger, serve
import time


@task
def get_api_info(url: str):
    response = httpx.get(url)
    response.raise_for_status()
    url_info = response.json()
    return url_info




@flow()
def get_rick_and_morty_characters_info():
    logger = get_run_logger()
    url = 'https://rickandmortyapi.com/api/character'
    api_info = get_api_info(url)
    logger.info(api_info)


@flow()
def get_rick_morty_episode_list():
    logger = get_run_logger()
    url = 'https://rickandmortyapi.com/api/episode'
    api_info = get_api_info(url)
    logger.info(api_info)


if __name__ == "__main__":
    rick_morty_character_deployment = get_rick_and_morty_characters_info. \
        to_deployment(name="Rick and Morty Characters")

    rick_morty_episode_list_deployment = get_rick_morty_episode_list. \
        to_deployment(name="Rick and Morty Episode List")

    serve(rick_morty_character_deployment, rick_morty_episode_list_deployment)
