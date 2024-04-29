from hydra.core.config_store import ConfigStore
from omegaconf import MISSING
from pydantic.dataclasses import dataclass

from cybulde.config_schemas.data_processing import dataset_cleaner_schema, dataset_readers_schema
from cybulde.config_schemas.infrastructure import gcp_schema


@dataclass
class DataProcessingConfig:
    version: str = MISSING
    data_local_save_dir: str = "./data/raw"
    dvc_remote_repo: str = "https://github.com/amrelshall/cybulde-data.git"
    dvc_data_folder: str = "data"
    github_user_name: str = "amrelshall"
    github_access_token: str = (
        "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"
    )

    infrastructure: gcp_schema.GCPConfig = gcp_schema.GCPConfig()
    dataset_reader_manager: dataset_readers_schema.DatasetReaderManagerConfig = MISSING
    dataset_cleaner_manager: dataset_cleaner_schema.DatasetCleanerManagerConfig = MISSING


def setup_config() -> None:
    gcp_schema.setup_config()
    dataset_readers_schema.setup_config()
    dataset_cleaner_schema.setup_config()

    cs = ConfigStore.instance()
    cs.store(name="data_processing_config_schema", node=DataProcessingConfig)
