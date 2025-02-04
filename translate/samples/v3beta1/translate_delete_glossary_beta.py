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

# DO NOT EDIT! This is a generated sample ("LongRunningPromise",  "translate_delete_glossary_beta")

# To install the latest published package dependency, execute the following:
#   pip install google-cloud-translate

# sample-metadata
#   title: Delete Glossary
#   description: Delete Glossary
#   usage: python3 samples/v3beta1/translate_delete_glossary_beta.py [--project "[Google Cloud Project ID]"] [--glossary_id "[Glossary ID]"]

# [START translate_delete_glossary_beta]
from google.cloud import translate_v3beta1


def sample_delete_glossary(project, glossary_id):
    """Delete Glossary"""

    client = translate_v3beta1.TranslationServiceClient()

    # project = '[Google Cloud Project ID]'
    # glossary_id = '[Glossary ID]'
    name = client.glossary_path(project, "us-central1", glossary_id)

    operation = client.delete_glossary(name)

    print(u"Waiting for operation to complete...")
    response = operation.result()

    print(u"Deleted Glossary.")


# [END translate_delete_glossary_beta]


def main():
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--project", type=str, default="[Google Cloud Project ID]")
    parser.add_argument("--glossary_id", type=str, default="[Glossary ID]")
    args = parser.parse_args()

    sample_delete_glossary(args.project, args.glossary_id)


if __name__ == "__main__":
    main()
