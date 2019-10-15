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

# DO NOT EDIT! This is a generated sample ("RequestPagedAll",  "translate_list_glossary_beta")

# To install the latest published package dependency, execute the following:
#   pip install google-cloud-translate

# sample-metadata
#   title: List Glossaries
#   description: List Glossaries
#   usage: python3 samples/v3beta1/translate_list_glossary_beta.py [--project "[Google Cloud Project ID]"]

# [START translate_list_glossary_beta]
from google.cloud import translate_v3beta1


def sample_list_glossaries(project):
    """List Glossaries"""

    client = translate_v3beta1.TranslationServiceClient()

    # project = '[Google Cloud Project ID]'
    parent = client.location_path(project, "us-central1")

    # Iterate over all results
    for response_item in client.list_glossaries(parent=parent):
        print(u"Glossary name: {}".format(response_item.name))
        print(u"Entry count: {}".format(response_item.entry_count))
        print(u"Input URI: {}".format(response_item.input_config.gcs_source.input_uri))


# [END translate_list_glossary_beta]


def main():
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--project", type=str, default="[Google Cloud Project ID]")
    args = parser.parse_args()

    sample_list_glossaries(args.project)


if __name__ == "__main__":
    main()
