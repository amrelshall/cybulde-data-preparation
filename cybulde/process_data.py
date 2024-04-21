from cybulde.config_schemas.config_schema import Config
from cybulde.utils.config_utils import get_config
from cybulde.utils.data_utils import get_raw_data_with_version


@get_config(config_path="../configs", config_name="config")
def process_data(config: Config) -> None:
    version = "v1"
    data_local_save_dir = "./data/raw"
    dvc_remote_repo = "https://github.com/amrelshall/cybulde-data.git"
    dvc_data_folder = "data"
    github_user_name = "amrelshall"
    github_access_token = "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"


    get_raw_data_with_version(
        version = version,
        data_local_save_dir = data_local_save_dir,
        dvc_remote_repo = dvc_remote_repo,
        dvc_data_folder = dvc_data_folder,
        github_user_name = github_user_name,
        github_access_token = github_access_token,
    )

if __name__ == "__main__":
    process_data()  # type: ignore
