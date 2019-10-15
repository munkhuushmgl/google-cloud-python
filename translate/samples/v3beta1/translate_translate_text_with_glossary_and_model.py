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

# DO NOT EDIT! This is a generated sample ("Request",  "translate_translate_text_with_glossary_and_model")

# To install the latest published package dependency, execute the following:
#   pip install google-cloud-translate

# sample-metadata
#   title: Translating Text with Glossary and Model
#   description: Translating Text with Glossary and Model
#   usage: python3 samples/v3beta1/translate_translate_text_with_glossary_and_model.py [--model_path "projects/[PROJECT ID]/locations/[LOCATION ID]/models/[MODEL ID]"] [--glossary_path "projects/[YOUR_PROJECT_ID]/locations/[LOCATION]/glossaries/[YOUR_GLOSSARY_ID]"] [--text "Hello, world!"] [--target_language fr] [--source_language en] [--project "[Google Cloud Project ID]"] [--location global]

# [START translate_translate_text_with_glossary_and_model]
from google.cloud import translate_v3beta1


def sample_translate_text(
    model_path, glossary_path, text, target_language, source_language, project, location
):
    """
    Translating Text with Glossary and Model

    Args:
      model_path The `model` type requested for this translation.
      glossary_path Specifies the glossary used for this translation.
      text The content to translate in string format
      target_language Required. The BCP-47 language code to use for translation.
      source_language Optional. The BCP-47 language code of the input text.
    """

    client = translate_v3beta1.TranslationServiceClient()

    # model_path = 'projects/[PROJECT ID]/locations/[LOCATION ID]/models/[MODEL ID]'
    # glossary_path = 'projects/[YOUR_PROJECT_ID]/locations/[LOCATION]/glossaries/[YOUR_GLOSSARY_ID]'
    # text = 'Hello, world!'
    # target_language = 'fr'
    # source_language = 'en'
    # project = '[Google Cloud Project ID]'
    # location = 'global'
    contents = [text]
    glossary_config = {"glossary": glossary_path}
    parent = client.location_path(project, location)

    response = client.translate_text(
        contents,
        target_language,
        model=model_path,
        glossary_config=glossary_config,
        source_language_code=source_language,
        parent=parent,
    )
    # Display the translation for each input text provided
    for translation in response.glossary_translations:
        print(u"Translated text: {}".format(translation.translated_text))


# [END translate_translate_text_with_glossary_and_model]


def main():
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--model_path",
        type=str,
        default="projects/[PROJECT ID]/locations/[LOCATION ID]/models/[MODEL ID]",
    )
    parser.add_argument(
        "--glossary_path",
        type=str,
        default="projects/[YOUR_PROJECT_ID]/locations/[LOCATION]/glossaries/[YOUR_GLOSSARY_ID]",
    )
    parser.add_argument("--text", type=str, default="Hello, world!")
    parser.add_argument("--target_language", type=str, default="fr")
    parser.add_argument("--source_language", type=str, default="en")
    parser.add_argument("--project", type=str, default="[Google Cloud Project ID]")
    parser.add_argument("--location", type=str, default="global")
    args = parser.parse_args()

    sample_translate_text(
        args.model_path,
        args.glossary_path,
        args.text,
        args.target_language,
        args.source_language,
        args.project,
        args.location,
    )


if __name__ == "__main__":
    main()
