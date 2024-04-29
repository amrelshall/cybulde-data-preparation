from hydra.utils import instantiate

from cybulde.config_schemas.data_processing_config_schema import DataProcessingConfig
from cybulde.utils.config_utils import get_config


@get_config(config_path="../configs", config_name="data_processing_config")
def process_data(config: DataProcessingConfig) -> None:
    # github_access_token = "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"

    dataset_reader_manager = instantiate(config.dataset_reader_manager)
    dataset_cleaner_manager = instantiate(config.dataset_cleaner_manager)

    df = dataset_reader_manager.read_data().compute()
    sample_df = df.sample(n=5)

    for _, row in sample_df.iterrows():
        text = row["text"]
        cleaned_text = dataset_cleaner_manager(text)

        print(60 * "=")
        print(f"{text = }")
        print(f"{cleaned_text = }")
        print(60 * "=")


if __name__ == "__main__":
    process_data()  
