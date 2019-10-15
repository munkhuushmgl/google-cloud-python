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

# DO NOT EDIT! This is a generated sample ("LongRunningPromise",  "translate_create_glossary_beta")

# To install the latest published package dependency, execute the following:
#   pip install google-cloud-translate

# sample-metadata
#   title: Create Glossary
#   description: Create Glossary
#   usage: python3 samples/v3beta1/translate_create_glossary_beta.py [--project "[Google Cloud Project ID]"] [--project_2 "[Your Google Cloud Project ID]"] [--glossary_id "my_glossary_id_123"]

# [START translate_create_glossary_beta]
from google.cloud import translate_v3beta1


def sample_create_glossary(project, project_2, glossary_id):
    """
    Create Glossary

    Args:
      glossary_id USEFUL DESCRIPTION
      This needs to inform the developer what value
      they should provide to glossary_id.
      It might even want to make a distinction between
      the full `name` and the `glossary-id`
    """

    client = translate_v3beta1.TranslationServiceClient()

    # project = '[Google Cloud Project ID]'
    # project_2 = '[Your Google Cloud Project ID]'
    # glossary_id = 'my_glossary_id_123'
    parent = client.location_path(project, "us-central1")
    name = client.glossary_path(project_2, "us-central1", glossary_id)
    language_codes_element = "en"
    language_codes_element_2 = "ja"
    language_codes = [language_codes_element, language_codes_element_2]
    language_codes_set = {"language_codes": language_codes}
    input_uri = "gs://translation_samples_beta/glossaries/glossary.csv"
    gcs_source = {"input_uri": input_uri}
    input_config = {"gcs_source": gcs_source}
    glossary = {
        "name": name,
        "language_codes_set": language_codes_set,
        "input_config": input_config,
    }

    operation = client.create_glossary(parent, glossary)

    print(u"Waiting for operation to complete...")
    response = operation.result()

    print(u"Created Glossary.")
    print(u"Glossary name: {}".format(response.name))
    print(u"Entry count: {}".format(response.entry_count))
    print(u"Input URI: {}".format(response.input_config.gcs_source.input_uri))


# [END translate_create_glossary_beta]


def main():
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--project", type=str, default="[Google Cloud Project ID]")
    parser.add_argument(
        "--project_2", type=str, default="[Your Google Cloud Project ID]"
    )
    parser.add_argument("--glossary_id", type=str, default="my_glossary_id_123")
    args = parser.parse_args()

    sample_create_glossary(args.project, args.project_2, args.glossary_id)


if __name__ == "__main__":
    main()
