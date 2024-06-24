import httpx
from prefect import flow, task, get_run_logger, serve
from prefect.exceptions import FlowRunWaitTimeout


base_url = 'https://rickandmortyapi.com/api'


@task
def get_api_info(url: str):
    response = httpx.get(url)
    response.raise_for_status()
    url_info = response.json()
    return url_info


@task(retries=2, retry_delay_seconds=10, timeout_seconds=0.01)
def get_api_info_timeout(url: str):
    response = httpx.get(url)
    response.raise_for_status()
    url_info = response.json()
    return url_info


@flow
def get_rick_and_morty_characters_info():
    logger = get_run_logger()
    url = f'{base_url}/character'
    api_info = get_api_info(url)
    logger.info(api_info)


@flow
def get_rick_morty_episode_list():
    logger = get_run_logger()
    url = f'{base_url}/episode'
    try:
        api_info = get_api_info_timeout(url)
        logger.info(api_info)
    except Exception as e:
        logger.error(f"Something went wrong while getting info from the api:"
                     f"{e}")
    except FlowRunWaitTimeout as e:
        logger.error(f"Timeout Error: {e}")


if __name__ == "__main__":
    rick_morty_character_deployment = get_rick_and_morty_characters_info. \
        to_deployment(name="Rick and Morty Characters")

    rick_morty_episode_list_deployment = get_rick_morty_episode_list. \
        to_deployment(name="Rick and Morty Episode List")

    serve(rick_morty_character_deployment, rick_morty_episode_list_deployment)
