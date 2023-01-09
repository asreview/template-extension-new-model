# Template for extending ASReview with new model

ASReview has support for extensions, which enable you to seamlessly integrate
your own programs with the ASReview framework. These extensions can extend the
software with new classifiers, query strategies, balance strategies, and feature
extraction techniques. This template can be used to write such an extension
(add a new SKLearn naive Bayes classifier with default settings in this case).

See the section [Extensions](https://asreview.readthedocs.io/en/latest/extensions_dev.html) on ReadTheDocs for more information on writing extensions.

## Getting started

Click the `Use this template` button and add/modify the algorithms. Install your new classifier with

```bash
pip install .
```

or

```bash
pip install git+https://github.com/{USER_NAME}/{REPO_NAME}.git
```

and replace `{USER_NAME}` and `{REPO_NAME}` by your own details.

## Usage

The new classifier `nb_example` is defined in
[`asreviewcontrib/models/nb_default_param.py`](asreviewcontrib/models/nb_default_param.py) and can be used in a simulation.

```bash
asreview simulate example_data_file.csv -m nb_example
```

## License

MIT license
