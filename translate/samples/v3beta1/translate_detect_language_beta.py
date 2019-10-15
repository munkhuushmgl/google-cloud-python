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

# DO NOT EDIT! This is a generated sample ("Request",  "translate_detect_language_beta")

# To install the latest published package dependency, execute the following:
#   pip install google-cloud-translate

# sample-metadata
#   title: Detect Language
#   description: Detecting the language of a text string
#   usage: python3 samples/v3beta1/translate_detect_language_beta.py [--text "Hello, world!"] [--project "[Google Cloud Project ID]"]

# [START translate_detect_language_beta]
from google.cloud import translate_v3beta1


def sample_detect_language(text, project):
    """
    Detecting the language of a text string

    Args:
      text The text string for performing language detection
    """

    client = translate_v3beta1.TranslationServiceClient()

    # text = 'Hello, world!'
    # project = '[Google Cloud Project ID]'
    parent = client.location_path(project, "global")

    response = client.detect_language(content=text, parent=parent)
    # Display list of detected languages sorted by detection confidence.
    # The most probable language is first.
    for language in response.languages:
        # The language detected
        print(u"Language code: {}".format(language.language_code))
        # Confidence of detection result for this language
        print(u"Confidence: {}".format(language.confidence))


# [END translate_detect_language_beta]


def main():
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--text", type=str, default="Hello, world!")
    parser.add_argument("--project", type=str, default="[Google Cloud Project ID]")
    args = parser.parse_args()

    sample_detect_language(args.text, args.project)


if __name__ == "__main__":
    main()
