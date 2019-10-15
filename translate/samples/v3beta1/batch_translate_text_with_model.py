# -*- coding: utf-8 -*-
#
# Copyright 2019 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# DO NOT EDIT! This is a generated sample ("LongRunningPromise",  "batch_translate_text_with_model")

# To install the latest published package dependency, execute the following:
#   pip install google-cloud-translate

# sample-metadata
#   title: Batch Translate with Model
#   description: Batch translate text using AutoML Translation model
#   usage: python3 samples/v3beta1/batch_translate_text_with_model.py [--input_uri "gs://cloud-samples-data/text.txt"] [--output_uri "gs://YOUR_BUCKET_ID/path_to_store_results/"] [--project "[Google Cloud Project ID]"] [--location "us-central1"] [--target_language en] [--source_language de] [--model_path "projects/{project-id}/locations/{location-id}/models/{your-model-id}"]

# [START batch_translate_text_with_model]
from google.cloud import translate_v3beta1


def sample_batch_translate_text(
    input_uri,
    output_uri,
    project,
    location,
    target_language,
    source_language,
    model_path,
):
    """
    Batch translate text using AutoML Translation model

    Args:
      target_language Required. Specify up to 10 language codes here.
      source_language Required. Source language code.
      model_path The models to use for translation. Map's key is target language
      code.
    """

    client = translate_v3beta1.TranslationServiceClient()

    # input_uri = 'gs://cloud-samples-data/text.txt'
    # output_uri = 'gs://YOUR_BUCKET_ID/path_to_store_results/'
    # project = '[Google Cloud Project ID]'
    # location = 'us-central1'
    # target_language = 'en'
    # source_language = 'de'
    # model_path = 'projects/{project-id}/locations/{location-id}/models/{your-model-id}'
    target_language_codes = [target_language]
    gcs_source = {"input_uri": input_uri}

    # Optional. Can be "text/plain" or "text/html".
    mime_type = "text/plain"
    input_configs_element = {"gcs_source": gcs_source, "mime_type": mime_type}
    input_configs = [input_configs_element]
    gcs_destination = {"output_uri_prefix": output_uri}
    output_config = {"gcs_destination": gcs_destination}
    parent = client.location_path(project, location)
    models = {"ja": model_path}

    operation = client.batch_translate_text(
        source_language,
        target_language_codes,
        input_configs,
        output_config,
        parent=parent,
        models=models,
    )

    print(u"Waiting for operation to complete...")
    response = operation.result()

    # Display the translation for each input text provided
    print(u"Total Characters: {}".format(response.total_characters))
    print(u"Translated Characters: {}".format(response.translated_characters))


# [END batch_translate_text_with_model]


def main():
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--input_uri", type=str, default="gs://cloud-samples-data/text.txt"
    )
    parser.add_argument(
        "--output_uri", type=str, default="gs://YOUR_BUCKET_ID/path_to_store_results/"
    )
    parser.add_argument("--project", type=str, default="[Google Cloud Project ID]")
    parser.add_argument("--location", type=str, default="us-central1")
    parser.add_argument("--target_language", type=str, default="en")
    parser.add_argument("--source_language", type=str, default="de")
    parser.add_argument(
        "--model_path",
        type=str,
        default="projects/{project-id}/locations/{location-id}/models/{your-model-id}",
    )
    args = parser.parse_args()

    sample_batch_translate_text(
        args.input_uri,
        args.output_uri,
        args.project,
        args.location,
        args.target_language,
        args.source_language,
        args.model_path,
    )


if __name__ == "__main__":
    main()
